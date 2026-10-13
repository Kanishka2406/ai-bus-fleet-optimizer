import math

def distance(point1, point2):
    x1, y1 = float(point1["x"]), float(point1["y"])
    x2, y2 = float(point2["x"]), float(point2["y"])
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_route_distance(route):
    return round(sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1)), 2)

def optimize_route(college, assigned_stops):
    if not assigned_stops:
        return [college]
    remaining = assigned_stops.copy()
    route = [college]
    current = college

    while remaining:
        nearest = min(remaining, key=lambda stop: distance(current, stop))
        route.append(nearest)
        current = nearest
        remaining.remove(nearest)

    route.append(college)
    return route

def allocate_buses(buses, stops, constraints):
    buses = sorted(buses, key=lambda b: int(b["capacity"]), reverse=True)
    stops = sorted(stops, key=lambda s: int(s["students"]), reverse=True)

    allocations = [{"bus": bus, "stops": [], "students": 0} for bus in buses]
    unassigned = []

    for stop in stops:
        best_bus = None
        best_remaining = None
        stop_students = int(stop["students"])

        for allocation in allocations:
            capacity = int(allocation["bus"]["capacity"])
            max_occupancy = int(constraints.get("max_bus_occupancy", capacity))
            usable_capacity = min(capacity, max_occupancy)
            remaining = usable_capacity - allocation["students"]

            if stop_students <= remaining:
                if best_bus is None or remaining < best_remaining:
                    best_bus = allocation
                    best_remaining = remaining

        if best_bus:
            best_bus["stops"].append(stop)
            best_bus["students"] += stop_students
        else:
            unassigned.append(stop)

    return allocations, unassigned

def optimize_fleet(buses, stops, constraints):
    college = {"id": "college", "name": "College", "x": 0, "y": 0, "students": 0}
    allocations, unassigned = allocate_buses(buses, stops, constraints)

    routes = []
    total_distance = 0
    total_students = 0
    used_buses = 0
    average_speed = float(constraints.get("average_speed", 30))

    for allocation in allocations:
        bus = allocation["bus"]
        assigned_stops = allocation["stops"]

        if not assigned_stops:
            continue

        used_buses += 1
        route = optimize_route(college, assigned_stops)
        route_distance = calculate_route_distance(route)
        students = allocation["students"]
        capacity = int(bus["capacity"])
        occupancy = round((students / capacity) * 100, 2)
        estimated_time = round((route_distance / average_speed) * 60, 1)

        total_distance += route_distance
        total_students += students

        routes.append({
            "bus_id": bus["id"],
            "bus_name": bus["name"],
            "capacity": capacity,
            "students": students,
            "occupancy": occupancy,
            "distance": route_distance,
            "estimated_time": estimated_time,
            "stops": [
                {"id": s["id"], "name": s["name"], "students": int(s["students"])}
                for s in assigned_stops
            ],
            "route": [item["name"] for item in route]
        })

    total_capacity = sum(int(bus["capacity"]) for bus in buses)
    total_requested_students = sum(int(stop["students"]) for stop in stops)

    overall_occupancy = round((total_students / total_capacity) * 100, 2) if total_capacity else 0
    served_percentage = round((total_students / total_requested_students) * 100, 2) if total_requested_students else 0

    return {
        "summary": {
            "total_buses": len(buses),
            "used_buses": used_buses,
            "total_stops": len(stops),
            "served_stops": len(stops) - len(unassigned),
            "total_students": total_requested_students,
            "served_students": total_students,
            "overall_occupancy": overall_occupancy,
            "served_percentage": served_percentage,
            "total_distance": round(total_distance, 2)
        },
        "routes": routes,
        "unassigned_stops": [
            {"id": s["id"], "name": s["name"], "students": int(s["students"])}
            for s in unassigned
        ]
    }

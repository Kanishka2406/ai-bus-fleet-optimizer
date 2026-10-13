from flask import Flask, render_template, request, jsonify
from optimizer import optimize_fleet

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data = request.get_json()
        buses = data.get("buses", [])
        stops = data.get("stops", [])
        constraints = data.get("constraints", {})

        if not buses:
            return jsonify({"success": False, "error": "Please add at least one bus."}), 400
        if not stops:
            return jsonify({"success": False, "error": "Please add at least one pickup stop."}), 400

        result = optimize_fleet(buses, stops, constraints)
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

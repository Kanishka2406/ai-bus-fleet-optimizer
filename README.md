# AI College Bus Fleet Optimizer

![Demo Screenshot](./static/screenshot.png)

## Overview
A local web application that helps colleges optimise their bus fleet. It uses classic AI algorithms (A*, Hill‑Climbing, CSP) to allocate buses, generate routes, and minimise total distance, fuel consumption and cost. The UI is built with a premium dark‑mode design (glass‑morphism, gradients, smooth micro‑animations) and runs entirely on the user's machine – no external cloud services are required.

## Features
- **Add / edit buses** – set capacity, name, ID.
- **Add pickup stops** – specify coordinates and student count.
- **Constraints** – maximum bus occupancy, average speed, etc.
- **Optimization** – runs the fleet optimiser and returns:
  - per‑bus routes
  - distance, estimated time and occupancy
  - summary statistics (total buses, used buses, overall occupancy, served percentage, total distance)
  - list of unassigned stops
- **Responsive UI** – works on desktop and mobile.
- **Premium look** – dark theme with glass‑morphism cards, gradient background, Inter font and subtle hover animations.

## Tech Stack
- **Backend**: Python 3.10+, Flask
- **Frontend**: HTML, vanilla CSS (custom dark‑mode design), vanilla JavaScript
- **Algorithms**: Custom implementation in `optimizer.py`
- **Package manager**: `pip` (see `requirements.txt`)

## Quick Start
```bash
# 1. Clone / copy the project folder
cd d:/users/Downloads/college_bus_optimizer

# 2. (Optional) set up a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
```
Open your browser and navigate to **http://127.0.0.1:5000**.

## Project Structure
```
college_bus_optimizer/
├── app.py                # Flask entry point
├── optimizer.py          # Core optimisation logic
├── requirements.txt      # Python dependencies
├── static/
│   ├── style.css         # Premium dark‑mode CSS
│   ├── script.js         # Front‑end interaction logic
│   └── screenshot.png    # (optional) demo image
└── templates/
    └── index.html        # Main UI page
```

## How It Works
1. **Data entry** – Users add buses and stops via the UI.
2. **Constraints** – Set maximum occupancy and average speed.
3. **Optimization** – Clicking **🚀 OPTIMIZE FLEET** sends a POST request to `/optimize`.
4. **Backend** – `optimizer.optimize_fleet` allocates buses, builds routes using a nearest‑neighbor heuristic, calculates distances and performance metrics.
5. **Result display** – The front‑end renders summary cards, route cards and a list of any unassigned stops.

## Customisation
- **Algorithms** – Replace the `optimize_route` / `allocate_buses` functions in `optimizer.py` with more advanced AI techniques (e.g., full A* search, genetic algorithms).
- **Styling** – Modify `static/style.css` to change colours, fonts or add more animations.
- **Deployment** – For production, run the app behind a WSGI server such as Gunicorn or uWSGI.

## License
This project is released under the MIT License – feel free to use, modify and distribute.

## Acknowledgements
- Flask – lightweight WSGI web framework.
- Google Fonts – Inter typeface.
- Inspiration from classic AI textbooks and bus‑routing case studies.

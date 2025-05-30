# 🧠 MCP Pokémon Server with Frontend

A beginner-friendly project that uses Flask (Python) for backend and a simple HTML/CSS/JavaScript frontend. It connects to the Open Pokémon API to retrieve, compare, and analyze Pokémon data in a modular and interactive way.

---

## 🌟 Features

- 🔍 View detailed Pokémon data
- ⚖️ Compare two Pokémon
- 🧠 Get type-based strategy suggestions
- 👥 Analyze Pokémon team strength
- 🌐 Simple web interface using HTML/CSS/JS

---

## 🗂️ Project Structure

- MCP_Pokemon_Project/
│
├── pokemon_modules/ # Modular backend logic
│ ├── init.py
│ ├── comparison.py
│ ├── info_retrieval.py
│ ├── strategy.py
│ └── team.py
│
├── pokemon-frontend/ # Frontend code
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── venv/ # Virtual environment (optional)
├── main.py # Flask backend entry point
├── requirements.txt # Python dependencies
└── README.md # Project documentation
## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mcp-pokemon-server.git
cd mcp-pokemon-server

### 2. Create & Activate Virtual Environment (Optional)
python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate
### 3. Install Required Packages
pip install -r requirements.txt
### 4. Run the Backend Server
python main.py
Server runs at: http://127.0.0.1:5000/

🌐 Using the Frontend
Open pokemon-frontend/index.html in your browser.

Interact with the interface to get Pokémon data, comparison, strategies, etc.

Ensure the Flask backend is running in the background.

🔁 Backend API Endpoints
Endpoint	Method	Description
/get-info/<pokemon>	GET	Get Pokémon details
/compare	POST	Compare two Pokémon
/strategy	POST	Get strategy based on types
/team-analyze	POST	Analyze a team of up to 6 Pokémon

🧪 Example: Compare Endpoint
POST /compare
Request:
{
  "pokemon1": "pikachu",
  "pokemon2": "charizard"
}
Response:
{
  "pokemon1": {"name": "pikachu", "height": 4, "weight": 60, "types": ["electric"]},
  "pokemon2": {"name": "charizard", "height": 17, "weight": 905, "types": ["fire", "flying"]},
  "height_difference": 13,
  "weight_difference": 845,
  "common_types": [],
  "stronger": "charizard"
}

🎓 What You’ll Learn
Flask basics and API design

Modular Python coding

Connecting frontend with backend

Working with public APIs

Full-stack project structure

📚 Requirements
Python 3.x

Flask

requests

flask-cors

Install using:
pip install -r requirements.txt

✨ Author
Kavita – Data Science Student | Beginner Developer

📜 License
MIT License — Free to use and modify.







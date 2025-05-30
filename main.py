# main.py

from flask import Flask, request, jsonify
from flask_cors import CORS

from pokemon_modules.info_retrieval import get_pokemon_info
from pokemon_modules.comparison import compare_pokemon
from pokemon_modules.strategy import recommend_strategy
from pokemon_modules.team import analyze_team

app = Flask(__name__)
CORS(app)

# ✅ Home Route - for checking server status
@app.route('/')
def home():
    return "✅ MCP Pokémon Server is Running!"

# 📌 Get info about a single Pokémon
@app.route('/api/info', methods=['POST'])
def info():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'error': 'No Pokémon name provided'}), 400
    result = get_pokemon_info(name)
    return jsonify(result)

# 📌 Compare two Pokémon
@app.route('/api/compare', methods=['POST'])
def compare():
    data = request.json
    name1 = data.get('name1')
    name2 = data.get('name2')
    if not name1 or not name2:
        return jsonify({'error': 'Both Pokémon names required'}), 400
    result = compare_pokemon(name1, name2)
    return jsonify(result)

# 📌 Recommend battle strategy
@app.route('/api/strategy', methods=['POST'])
def strategy():
    data = request.json
    name1 = data.get('name1')
    name2 = data.get('name2')
    if not name1 or not name2:
        return jsonify({'error': 'Both Pokémon names required'}), 400
    result = recommend_strategy(name1, name2)
    return jsonify(result)

# 📌 Analyze a Pokémon team
@app.route('/api/team', methods=['POST'])
def team():
    data = request.json
    team_list = data.get('team')
    if not team_list or not isinstance(team_list, list):
        return jsonify({'error': 'A list of Pokémon names is required'}), 400
    result = analyze_team(team_list)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

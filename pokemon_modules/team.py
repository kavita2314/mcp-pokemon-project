# team.py

from pokemon_modules.info_retrieval import get_pokemon_info

def analyze_team(pokemon_names):
    team_data = []
    total_attack = 0
    total_defense = 0
    total_speed = 0
    total_stats = 0

    for name in pokemon_names:
        info = get_pokemon_info(name)
        if "error" in info:
            return {"error": f"Could not retrieve info for {name}"}

        stats = info.get("stats", {})
        attack = stats.get("attack", 0)
        defense = stats.get("defense", 0)
        speed = stats.get("speed", 0)
        total = sum(stats.values())

        team_data.append({
            "name": info["name"],
            "types": info["types"],
            "abilities": info["abilities"],
            "attack": attack,
            "defense": defense,
            "speed": speed,
            "total_stats": total
        })

        total_attack += attack
        total_defense += defense
        total_speed += speed
        total_stats += total

    # Team strategy analysis
    team_strength_type = "Balanced"
    if total_attack > total_defense and total_attack > total_speed:
        team_strength_type = "Offensive"
    elif total_defense > total_attack and total_defense > total_speed:
        team_strength_type = "Defensive"
    elif total_speed > total_attack and total_speed > total_defense:
        team_strength_type = "Speed-Based"

    return {
        "team": team_data,
        "total_stats": {
            "attack": total_attack,
            "defense": total_defense,
            "speed": total_speed,
            "overall": total_stats
        },
        "team_type": team_strength_type,
        "summary": f"This team is primarily {team_strength_type.lower()} based on the overall stat distribution."
    }

# strategy.py

from pokemon_modules.info_retrieval import get_pokemon_info

# Simple type chart
type_chart = {
    "fire": {"weak": ["water", "rock", "ground"], "strong": ["grass", "bug", "ice", "steel"]},
    "water": {"weak": ["electric", "grass"], "strong": ["fire", "rock", "ground"]},
    "electric": {"weak": ["ground"], "strong": ["water", "flying"]},
    "grass": {"weak": ["fire", "ice", "poison", "flying", "bug"], "strong": ["water", "rock", "ground"]},
    "rock": {"weak": ["water", "grass", "fighting", "ground", "steel"], "strong": ["fire", "ice", "flying", "bug"]},
    "ground": {"weak": ["water", "grass", "ice"], "strong": ["fire", "electric", "poison", "rock", "steel"]},
    "psychic": {"weak": ["bug", "ghost", "dark"], "strong": ["fighting", "poison"]},
    "fighting": {"weak": ["flying", "psychic", "fairy"], "strong": ["normal", "ice", "rock", "dark", "steel"]},
    "flying": {"weak": ["electric", "ice", "rock"], "strong": ["grass", "fighting", "bug"]},
}

def analyze_stats(stats):
    return {
        "attack": stats.get("attack", 0),
        "defense": stats.get("defense", 0),
        "speed": stats.get("speed", 0),
        "total": sum(stats.values())
    }

def recommend_strategy(pokemon1, pokemon2):
    info1 = get_pokemon_info(pokemon1)
    info2 = get_pokemon_info(pokemon2)

    if "error" in info1 or "error" in info2:
        return {"error": "One or both Pokémon not found."}

    types1 = info1["types"]
    types2 = info2["types"]
    stats1 = analyze_stats(info1.get("stats", {}))
    stats2 = analyze_stats(info2.get("stats", {}))

    advantage1 = []
    advantage2 = []

    for t1 in types1:
        if t1 in type_chart:
            for strong in type_chart[t1]["strong"]:
                if strong in types2:
                    advantage1.append((t1, strong))

    for t2 in types2:
        if t2 in type_chart:
            for strong in type_chart[t2]["strong"]:
                if strong in types1:
                    advantage2.append((t2, strong))

    # Strategy reasoning
    summary = []

    if advantage1:
        summary.append(f"{pokemon1.title()} has type advantage.")
    if advantage2:
        summary.append(f"{pokemon2.title()} has type advantage.")

    if stats1["total"] > stats2["total"]:
        summary.append(f"{pokemon1.title()} has stronger overall stats.")
    elif stats2["total"] > stats1["total"]:
        summary.append(f"{pokemon2.title()} has stronger overall stats.")
    else:
        summary.append("Both Pokémon have equal total stats.")

    # Determine winner based on multiple factors
    if len(advantage1) > len(advantage2) and stats1["total"] >= stats2["total"]:
        recommendation = f"🎯 {pokemon1.title()} is more likely to win based on type advantage and stats."
    elif len(advantage2) > len(advantage1) and stats2["total"] >= stats1["total"]:
        recommendation = f"🎯 {pokemon2.title()} is more likely to win based on type advantage and stats."
    else:
        recommendation = "🤝 It's a balanced match. Battle could depend on move choices and levels."

    return {
        "pokemon1": {
            "name": info1["name"],
            "types": types1,
            "abilities": info1["abilities"],
            "stats": stats1
        },
        "pokemon2": {
            "name": info2["name"],
            "types": types2,
            "abilities": info2["abilities"],
            "stats": stats2
        },
        "type_advantage": {
            pokemon1: advantage1,
            pokemon2: advantage2
        },
        "summary": summary,
        "strategy": recommendation
    }

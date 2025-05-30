# comparison.py

from pokemon_modules.info_retrieval import get_pokemon_info

def compare_pokemon(pokemon1, pokemon2):
    """
    Compares two Pokémon based on their height, weight, and types.

    Parameters:
    - pokemon1 (str): Name of the first Pokémon.
    - pokemon2 (str): Name of the second Pokémon.

    Returns:
    - dict: A dictionary containing the comparison results or an error message.
    """
    info1 = get_pokemon_info(pokemon1)
    info2 = get_pokemon_info(pokemon2)

    # Check if both Pokémon were found
    if "error" in info1 or "error" in info2:
        return {"error": "One or both Pokémon not found."}

    # Calculate differences
    height_diff = abs(info1["height"] - info2["height"])
    weight_diff = abs(info1["weight"] - info2["weight"])
    common_types = list(set(info1["types"]) & set(info2["types"]))

    # Determine which Pokémon is stronger based on combined height and weight
    score1 = info1["height"] + info1["weight"]
    score2 = info2["height"] + info2["weight"]
    stronger = pokemon1 if score1 > score2 else pokemon2

    # Prepare the comparison result
    comparison = {
        "pokemon1": {
            "name": info1["name"],
            "height": info1["height"],
            "weight": info1["weight"],
            "types": info1["types"]
        },
        "pokemon2": {
            "name": info2["name"],
            "height": info2["height"],
            "weight": info2["weight"],
            "types": info2["types"]
        },
        "height_difference": height_diff,
        "weight_difference": weight_diff,
        "common_types": common_types,
        "stronger": stronger
    }

    return comparison

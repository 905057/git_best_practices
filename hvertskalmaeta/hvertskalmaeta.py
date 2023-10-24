"""solution to the Hvert skal Maeta kattis problem
"""

__author__ = "Bryleigh Koci"


def answer(start_place: str) -> str:
    """solves problem

    Args:
        input (str): the municipality

    Returns:
        str: the closest contest site
    """
    municipality = ["Reykjavik", "Kopavogur", "Hafnarfjordur", "Reykjanesbaer",
                    "Akureyri", "Gardabaer", "Mosfellsbaer", "Arborg",
                    "Akranes", "Fjardabyggd", "Mulathing", "Seltjarnarnes"]
    distance_rey = [0, 6, 12, 48, 388, 9, 16, 64, 49, 659, 603, 4]
    distance_aku = [388, 387, 391, 427, 0, 389, 371, 428, 350, 290, 216, 390]
    place = 0

    for x in municipality:
        if x == start_place:
            break
        place += 1

    if distance_rey[place] > distance_aku[place]:
        return "Akureyri"
    else:
        return "Reykjavik"


def solve() -> None:
    """takes input and ansers
    """
    data = input()
    print(answer(data))


if __name__ == "__main__":
    solve()

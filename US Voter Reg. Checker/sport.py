"""
Sports Player Chooser

This script allows users to choose their favorite sport and player from a list.
"""


def choose_player(sport):
    """
    Prompt user to choose a favorite player from the selected sport.

    Args:
        sport (str): The chosen sport.

    Returns:
        None
    """
    players = {
        "football": ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé"],
        "basketball": ["LeBron James", "Stephen Curry", "Kevin Durant", "Giannis Antetokounmpo"],
        "tennis": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams"],
        "soccer": ["Megan Rapinoe", "Alex Morgan", "Ada Hegerberg", "Sam Kerr"],
        # Add more sports and players as needed
    }

    if sport in players:
        print(f"Great choice! Here are some players from {sport}:")
        for index, player in enumerate(players[sport], start=1):
            print(f"{index}. {player}")

        player_choice = int(input("Enter the number corresponding to your favorite player: "))
        if 1 <= player_choice <= len(players[sport]):
            favorite_player = players[sport][player_choice - 1]
            print(f"Your favorite player from {sport} is: {favorite_player}")
        else:
            print("Invalid choice.")
    else:
        print("Sorry, that sport is not in the list.")


def main():
    """
    Main function that allows users to choose their favorite sport and player.

    Returns:
        None
    """
    sports = ["football", "basketball", "tennis", "soccer"]

    print("Choose your favorite sport from the list:")
    for index, sport in enumerate(sports, start=1):
        print(f"{index}. {sport}")

    sport_choice = int(input("Enter the number corresponding to your favorite sport: "))
    if 1 <= sport_choice <= len(sports):
        chosen_sport = sports[sport_choice - 1]
        choose_player(chosen_sport)
    else:
        print("Invalid choice.")


if __name__ != "__main__":
    pass
else:
    main()

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
    }

    if sport in players:
        while True:
            print(f"Great choice! Here are some players from {sport}:")
            for index, player in enumerate(players[sport], start=1):
                print(f"{index}. {player}")

            try:
                player_choice = int(input("Enter the number corresponding to your favorite player: "))
                if 1 > player_choice or player_choice > len(players[sport]):
                    print(f"Invalid choice. Please enter a number between 1 and {len(players[sport])}.")
                else:
                    favorite_player = players[sport][player_choice - 1]
                    print(f"Your favorite player from {sport} is: {favorite_player}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")


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

    while True:
        try:
            sport_choice = int(input("Enter the number corresponding to your favorite sport: "))
            if 1 > sport_choice or sport_choice > len(sports):
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                chosen_sport = sports[sport_choice - 1]
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    choose_player(chosen_sport)


if __name__ == "__main__":
    main()

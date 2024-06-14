from io import BytesIO

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from PIL import Image

# the state data structure (list of dictionaries)
us_states = [
    {
        "name":
        "Alabama",
        "capital":
        "Montgomery",
        "population":
        196010,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/alabama/state-flower/camellia"
    },
    {
        "name":
        "Alaska",
        "capital":
        "Juneau",
        "population":
        31534,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/alaska/state-flower/alpine-forget-me-not"
    },
    {
        "name":
        "Arizona",
        "capital":
        "Phoenix",
        "population":
        1651344,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/arizona/state-flower/saguaro-cactus-blossom"
    },
    {
        "name":
        "Arkansas",
        "capital":
        "Little Rock",
        "population":
        201029,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/arkansas/state-flower/apple-blossom"
    },
    {
        "name":
        "California",
        "capital":
        "Sacramento",
        "population":
        528306,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/california/state-flower/california-poppy"
    },
    {
        "name":
        "Colorado",
        "capital":
        "Denver",
        "population":
        699288,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/colorado/state-flower/rocky-mountain-columbine"
    },
    {
        "name":
        "Connecticut",
        "capital":
        "Hartford",
        "population":
        119817,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/connecticut/state-flower/mountain-laurel"
    },
    {
        "name":
        "Delaware",
        "capital":
        "Dover",
        "population":
        37892,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/delaware/state-flower/peach-blossom"
    },
    {
        "name":
        "Florida",
        "capital":
        "Tallahassee",
        "population":
        198631,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/florida/state-flower/orange-blossom"
    },
    {
        "name":
        "Georgia",
        "capital":
        "Atlanta",
        "population":
        490270,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/georgia/state-flower/cherokee-rose"
    },
    {
        "name":
        "Hawaii",
        "capital":
        "Honolulu",
        "population":
        337088,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/hawaii/state-flower/lokelani"
    },
    {
        "name":
        "Idaho",
        "capital":
        "Boise",
        "population":
        240713,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/idaho/state-flower/syringa"
    },
    {
        "name":
        "Illinois",
        "capital":
        "Springfield",
        "population":
        111711,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/illinois/state-flower/violet"
    },
    {
        "name":
        "Indiana",
        "capital":
        "Indianapolis",
        "population":
        871449,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/indiana/state-flower/peony"
    },
    {
        "name":
        "Iowa",
        "capital":
        "Des Moines",
        "population":
        208734,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/iowa/state-flower/wild-prairie-rose"
    },
    {
        "name":
        "Kansas",
        "capital":
        "Topeka",
        "population":
        125353,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/kansas/state-flower/sunflower"
    },
    {
        "name":
        "Kentucky",
        "capital":
        "Frankfort",
        "population":
        28523,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/kentucky/state-flower/goldenrod"
    },
    {
        "name":
        "Louisiana",
        "capital":
        "Baton Rouge",
        "population":
        217665,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/louisiana/state-flower/iris"
    },
    {
        "name":
        "Maine",
        "capital":
        "Augusta",
        "population":
        19058,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/maine/state-flower-state-plant/white-pine-cone-and-tassle"
    },
    {
        "name":
        "Maryland",
        "capital":
        "Annapolis",
        "population":
        40397,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/maryland/state-flower/black-eyed-susan"
    },
    {
        "name":
        "Massachusett",
        "capital":
        "Boston",
        "population":
        617459,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/massachusetts/state-flower/mayflower"
    },
    {
        "name":
        "Michigan",
        "capital":
        "Lansing",
        "population":
        112460,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/michigan/state-flower/dwarf-lake-iris"
    },
    {
        "name":
        "Minnesota",
        "capital":
        "St. Paul",
        "population":
        299830,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/minnesota/state-flower/pink-white-lady-slipper"
    },
    {
        "name":
        "Mississippi",
        "capital":
        "Jackson",
        "population":
        143776,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/mississippi/state-flower/magnolia"
    },
    {
        "name":
        "Missouri",
        "capital":
        "Jefferson City",
        "population":
        42535,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/missouri/state-flower/white-hawthorn-blossom"
    },
    {
        "name":
        "Montana",
        "capital":
        "Helena",
        "population":
        34690,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/montana/state-flower/bitterroot"
    },
    {
        "name":
        "Nebraska",
        "capital":
        "Lincoln",
        "population":
        295222,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/nebraska/state-flower/goldenrod"
    },
    {
        "name":
        "Nevada",
        "capital":
        "Carson City",
        "population":
        59630,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/nevada/state-flower/sagebrush"
    },
    {
        "name":
        "New Hampshi",
        "capital":
        "Concord",
        "population":
        44606,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/new-hampshire/state-flower/pink-ladys-slipper"
    },
    {
        "name":
        "New Jersey",
        "capital":
        "Trenton",
        "population":
        90048,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/new-jersey/state-flower/violet"
    },
    {
        "name":
        "New Mexico",
        "capital":
        "Santa Fe",
        "population":
        89220,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/new-mexico/state-flower/yucca"
    },
    {
        "name":
        "New York",
        "capital":
        "Albany",
        "population":
        97593,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/new-york/state-flower-state-plant/lilac"
    },
    {
        "name":
        "North Carolina",
        "capital":
        "Raleigh",
        "population":
        472540,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/north-carolina/state-flower/dogwood"
    },
    {
        "name":
        "North Dakota",
        "capital":
        "Bismarck",
        "population":
        75073,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/north-dakota/state-flower/wild-prairie-rose"
    },
    {
        "name":
        "Ohio",
        "capital":
        "Columbus",
        "population":
        907865,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/ohio/state-flower/red-carnation"
    },
    {
        "name":
        "Oklahoma",
        "capital":
        "Oklahoma City",
        "population":
        697763,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/oklahoma/state-flower/mistletoe"
    },
    {
        "name":
        "Oregon",
        "capital":
        "Salem",
        "population":
        181620,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/oregon/state-flower/oregon-grape"
    },
    {
        "name": "Pennsylvania",
        "capital": "Harrisburg",
        "population": 50267,
        "flower_image_url": ""
    },
    {
        "name":
        "Rhode Island",
        "capital":
        "Providence",
        "population":
        188877,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-or-officially-designated-item/pennsylvania/state-flower/mountain-laurel"
    },
    {
        "name":
        "South Carolina",
        "capital":
        "Columbia",
        "population":
        137996,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/pennsylvania/state-plant/penngift-crownvetch"
    },
    {
        "name":
        "South Dakota",
        "capital":
        "Pierre",
        "population":
        13954,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/south-dakota/state-flower/pasque-flower"
    },
    {
        "name":
        "Tennessee",
        "capital":
        "Nashville",
        "population":
        658525,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/mississippi/state-flower/passion-flower"
    },
    {
        "name":
        "Texas",
        "capital":
        "Austin",
        "population":
        966292,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/texas/state-flower/nymphaea-texas-dawn"
    },
    {
        "name":
        "Utah",
        "capital":
        "Salt Lake City",
        "population":
        202272,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/utah/state-flower/sego-lily"
    },
    {
        "name":
        "Vermont",
        "capital":
        "Montpelier",
        "population":
        7988,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/vermont/state-flower/red-clover"
    },
    {
        "name":
        "Virginia",
        "capital":
        "Richmond",
        "population":
        226472,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol-official-item/virginia/state-flower/american-dogwood"
    },
    {
        "name":
        "Washington",
        "capital":
        "Olympia",
        "population":
        56510,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/washington/state-flower/coast-rhododendron"
    },
    {
        "name":
        "West Virginia",
        "capital":
        "Charleston",
        "population":
        46692,
        "flower_image_url":
        "https://statesymbolsusa.org/symbol/west-virginia/state-flower/rhododendron"
    },
    {
        "name":
        "Wisconsin",
        "capital":
        "Madison",
        "population":
        269897,
        "flower_image_url":
        "https://statesymbolsusa.org/wisconsin/flower/wood-violet"
    },
    {
        "name":
        "Wyoming",
        "capital":
        "Cheyenne",
        "population":
        64831,
        "flower_image_url":
        "https://statesymbolsusa.org/wyoming/flower/indian-paintbrush"
    },
]


def display_menu():
  """
    Display the menu options to the user.

    :returns: None
    """
  print("Welcome to the US States Information App")
  print("1. Display all U.S. States")
  print("2. Search for a specific state")
  print("3. Display top 5 populated states")
  print("4. Update state population")
  print("5. Exit")


def display_all_states():
  """
    Display information for all U.S. states.
    """
  print("\nList of U.S. States:")
  for state in us_states:
    print(
        f"{state['name']:20} | Capital: {state['capital']:15} | Population: {state['population']:10} | Flower: {state['flower_image_url']}"
    )


# Function to search for a specific state
def search_state():
    """
    Display information about a specific state and show its associated flower image.

    This function prompts the user to input the name of a state, searches for the
    provided state in the 'us_states' list, and displays information about the state's
    capital and population. It also shows an associated flower image using the provided
    'flower_image_url' for the state.

    Args:
        None

    Returns:
        None
    """
  state_name = input("\nEnter the name of the state: ")
  found: bool = False
  for state in us_states:
    if state['name'].lower() == state_name.lower():
      print(f"\n{state['name']} Information:")
      print(f"Capital: {state['capital']}")
      print(f"Population: {state['population']}")
      response = requests.get(state['flower_image_url'])
      img = Image.open(BytesIO(response.content))
      img.show()
      found = True
      break
  if not found:
    print("State not found.")


def display_top_states():
  """Display a bar graph of the top 5 populated states."""
  top_states = sorted(us_states, key=lambda x: x['population'],
                      reverse=True)[:5]
  state_names = [state['name'] for state in top_states]
  state_populations = [state['population'] for state in top_states]

  plt.bar(state_names, state_populations)
  plt.xlabel('State')
  plt.ylabel('Population')
  plt.title('Top 5 Populated States')
  plt.xticks(rotation=45)
  plt.show()


def update_population():
  """Update the population of a specific state."""
  state_name = input("\nEnter the name of the state: ")
  new_population = int(input("Enter the new population: "))
  for state in us_states:
    if state['name'].lower() == state_name.lower():
      state['population'] = new_population
      print("Population updated successfully.")
      break
  else:
    print("State not found.")


# Main program loop
while True:
  display_menu()
  choice = input("\nEnter your choice: ")

  if choice == '1':
    display_all_states()
  elif choice == '2':
    search_state()
  elif choice == '3':
    display_top_states()
  elif choice == '4':
    update_population()
  elif choice == '5':
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid choice. Please choose a valid option.")

from classes import airline
from helpers import user_input


def main():
  # Create an airline object with 25 airports
  air_x = airline.Airline(25)

  # Display the airports and connections the airline has
  air_x.display_airports()

  # Get the desired input and output airports
  target = user_input.get_user_airports(air_x.get_valid_codes())

  # Find the routes that connect both airports
  air_x.find_routes(target[0], target[1])


if __name__ == '__main__':
  main()

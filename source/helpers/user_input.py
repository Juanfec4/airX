# Validate user input
def get_user_airport_input(prompt, valid_codes, exclude=None):
  while True:
    # Take user input, strip any leading/trailing spaces, and convert to uppercase
    airport_code = input(prompt).strip().upper()

    # Check if the airport code is valid and not the excluded code
    if airport_code in valid_codes and airport_code != exclude:
      return airport_code
    else:
      print(
          "Invalid airport code! Please enter a different valid airport code.")


# Gather user input
def get_user_airports(valid_codes):
  # Print header for the input interface
  print("\n╔" + "═" * 40 + "╗")
  print("║" + "  AIRLINE ROUTE PLANNER  ".center(40) + "║")
  print("╚" + "═" * 40 + "╝\n")

  # Prompt user for starting and destination airport codes
  starting_airport = get_user_airport_input("🛫  Enter your starting airport: ",
                                            valid_codes)
  destination_airport = get_user_airport_input(
      "🛬  Enter your destination airport: ",
      valid_codes,
      exclude=starting_airport)
  print("\n")
  # Return gathered codes
  return starting_airport, destination_airport

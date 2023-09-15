import random
from helpers import output_formatter


#Node Data Structure
class Node:
  # Node will have an airport code and a list of connections (nodes).
  def __init__(self, code=None):
    self.code = code
    self.connections = []

  # Method to add a connection (node) to the connections list.
  def add_connection(self, connection_node):
    if (connection_node != self):
      self.connections.append(connection_node)
      connection_node.connections.append(self)

  # Print connections list (nodes)
  def show_connections(self):
    output_string = ", ".join(
        [connection.code for connection in self.connections])
    return output_string


# Graph Representation (Using adjacency list)
class Airline:

  def __init__(self, airport_qty):
    self.airport_qty = airport_qty
    self.airports = []
    self.add_random_airports(airport_qty)

  # Populate graph with random airports
  def add_random_airports(self, num, max_connections=2):
    airports = []

    AIRPORT_CODES = [
        'ATL', 'LAX', 'ORD', 'DFW', 'DEN', 'SFO', 'SEA', 'LAS', 'MCO', 'EWR',
        'CLT', 'PHX', 'IAH', 'MIA', 'BOS', 'MSP', 'FLL', 'DTW', 'PHL', 'LGA',
        'BWI', 'SLC', 'SAN', 'IAD', 'DCA', 'MDW', 'TPA', 'PDX', 'HNL', 'SJU'
    ]

    # Itereate for an X number of times, as specified in the arguments
    for _ in range(num):

      # Get a random airport code
      code = random.choice(AIRPORT_CODES)
      AIRPORT_CODES.remove(code)

      # Create a new airport node with the random code & add to the airport list
      new_airport = Node(code)
      airports.append(new_airport)

      # Get the possible connections (excluding this airport)

      possible_connections = [
          airport for airport in airports if airport != new_airport
      ]

      # If there are no possible connections, continue to the next iteration
      if len(possible_connections) == 0:
        continue

      # Add connections to the newly created airport (randomly)
      num_connections = random.randint(
          1, min(max_connections, len(possible_connections)))
      connections = random.sample(possible_connections, num_connections)

      for connection in connections:
        new_airport.add_connection(connection)

    # add the newly created airports list to the object's adjacency list
    self.airports = self.airports + airports
    return

  # Print airports adjacency list
  def display_airports(self):
    # Header
    print("=" * 60)
    print("Available Airports".center(60))
    print("=" * 60)

    # Print table headers
    print("{:<5} {:<10} {:<30}".format("No.", "Airport", "Connected To"))
    print("-" * 60)

    # Airports
    for index, airport in enumerate(self.airports, 1):
      connections = airport.show_connections()
      print(f"{index:<5} {airport.code:<10} {connections:<30}")

    # Footer
    print("=" * 60)

  # Find routes method (from airport 1 to airport 2)
  def find_routes(self, code_1, code_2):

    # Breadth First Search (Traversal)
    def bfs(start_node):
      found = False
      queue = [(start_node, [])]
      visited = set()
      route_num = 1

      # While there are nodes to visit, execute
      while queue:
        airport, path = queue.pop(0)

        # If the airport was found, print the route
        if airport.code == code_2:
          route = ' -> '.join([node.code for node in path] + [code_2])
          print(output_formatter.format_route(route, route_num))
          route_num += 1
          found = True

        # Add the airport to the visited set, to keep track
        visited.add(airport)

        # Loop through the connections of the airport and visit non-visited airports
        for connection in airport.connections:
          if connection not in visited:
            new_path = path + [airport]
            queue.append((connection, new_path))

      # Return True or False, depending on whether it was possible or not
      return found

    # Find the starting node
    found = False
    for node in self.airports:
      if node.code == code_1:
        found = bfs(node)

        # If there are no routes, print default message
    if not found:
      print('There are no routes supported for the desired airports.')

  # Get valid airport codes
  def get_valid_codes(self):
    codes = []

    for airport in self.airports:
      codes.append(airport.code)

    return codes

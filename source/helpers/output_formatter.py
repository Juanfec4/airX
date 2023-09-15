def format_route(route, num):
  width = max(len(route + str(num)), 10) + 10
  output = f"""
╔{'═' * width}╗
║ Route {num}: {route.ljust(width - 10)}║
╚{'═' * width}╝
"""
  return output

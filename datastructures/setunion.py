pets = {"davor", "bianca", "lu", "luna", "max", "lupe", "jorge"}
owners = {"daniel", "zulay", "stefani", "Nanes", "jorge"}

union = pets | owners
intersection = pets & owners
difference = pets - owners
print(f"union: {union}")  # union
print(f"intersection: {intersection}")
print(f"difference: {difference}")

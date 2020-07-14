# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

wp1 = Waypoint(name='Catacombs', lat = 41.70505, lon = -121.51521)
print(f'"{wp1.name}", {wp1.lat}, {wp1.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        
    def __str__(self):
    # def __str__(self, lat, lon, name):
        return(f"""
Name      = "{wp1.name}"
Latitude  = {wp1.lat}
Longitude = {wp1.lon}""")
        # return(f'"{wp1.name}", {wp1.lat}, {wp1.lon}')
        # return(self, wp1.name, wp1.lat, wp1.lon)

# Waypoint = Waypoint()
Waypoint = Waypoint(wp1.name, wp1.lat, wp1.lon)
print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

gc1 = Geocache(name="Newberry Views", difficulty='diff 1.5', 
          size='size 2', lat=44.052137, lon=-121.41556)

# Print it--also make this print more nicely

# I had to redefine all the classes since 'Waypoint' is assigned to
# a variable from the previous question

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
        
    def __str__(self):
        return(f"""
Name       = "{gc1.name}"
Difficulty = {gc1.difficulty} 
Size       = {gc1.size}
Latitude   = {gc1.lat}
Longitude  = {gc1.lon}""")

Geocache = Geocache(gc1.name, gc1.difficulty, gc1.size, gc1.lat, gc1.lon)
print(Geocache)

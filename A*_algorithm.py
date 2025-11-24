# ⭐ A* (A-Star) Algorithm — The Complete Guide
# 🎯 1. What Is A*? (Simple Explanation)

# A* is a pathfinding algorithm used to find the shortest, fastest, most optimal path between two points.

# It is a smarter version of Dijkstra.

# Dijkstra explores everywhere

# A* explores only where the goal actually is

# This makes A* VERY fast, which is why:

# Uber

# Google Maps

# Lyft

# Self-driving cars

# Robotics

# Game AI

# all use it.

# 🧠 2. The Core Equation (The Heart of A*)

# A* evaluates each possible next step with:

# f(n) = g(n) + h(n)

# Where:

# g(n)

# Cost from start → current node

# h(n)

# Estimated cost from current node → goal
# (This is what makes A* "smart")

# f(n)

# Total estimated cost of a path through node n
# → A* always chooses the node with the lowest f(n).

# 🕹️ 3. How A* Works (Step-by-step)

# 1️⃣ Add start node to open set
# 2️⃣ While open set is not empty:
# 3️⃣ Pick the node with smallest f(n)
# 4️⃣ If it’s the goal → DONE
# 5️⃣ Otherwise, expand its neighbors
# 6️⃣ Update costs (g, h, f)
# 7️⃣ Move current to closed set
# 8️⃣ Repeat

# 🧩 4. Heuristics (The Magic Part)

# The “smart guess” is your heuristic.

# For real-world maps, the best heuristic is:

# → Haversine Distance (based on latitude & longitude)

# This predicts the straight-line distance between two points on Earth.

# Other common heuristics:

# Manhattan Distance (grid maps)

# Euclidean Distance (flat maps)

# A good heuristic makes A*:

# faster

# optimal

# scalable

# 🚦 5. A* in Real Apps Like Uber

# Uber uses A* but enhanced with:

# ✔ Traffic weight adjustments
# ✔ ETA prediction models
# ✔ Road type penalties (highway vs small street)
# ✔ One-way streets
# ✔ Dynamic weighting (accidents, rush hour)
# ✔ Multiple A* layers
# ✔ Precomputed road hierarchies

# Your routing becomes:

# cost = road_distance
#      + traffic_delay
#      + road_condition_penalty
#      + predicted_congestion

# 📦 6. Python Implementation (Clean + Easy)
# import heapq
# import math

# # Haversine distance for heuristic
# def haversine(a, b):
#     lat1, lon1 = a
#     lat2, lon2 = b
#     R = 6371  # Earth radius in KM
    
#     d_lat = math.radians(lat2 - lat1)
#     d_lon = math.radians(lon2 - lon1)
    
#     a = (math.sin(d_lat/2)**2 +
#          math.cos(math.radians(lat1)) *
#          math.cos(math.radians(lat2)) *
#          math.sin(d_lon/2)**2)
    
#     return 2 * R * math.asin(math.sqrt(a))

# def a_star(graph, start, goal, coordinates):
#     open_set = []
#     heapq.heappush(open_set, (0, start))

#     g = {node: float('inf') for node in graph}
#     g[start] = 0

#     came_from = {}

#     while open_set:
#         _, current = heapq.heappop(open_set)

#         if current == goal:
#             break

#         for neighbor, dist in graph[current].items():
#             temp_g = g[current] + dist

#             if temp_g < g[neighbor]:
#                 g[neighbor] = temp_g
#                 f = temp_g + haversine(coordinates[neighbor], coordinates[goal])
#                 heapq.heappush(open_set, (f, neighbor))
#                 came_from[neighbor] = current

#     return g, came_from

# # 🧭 7. Reconstructing the Path
# def get_path(came_from, start, goal):
#     path = [goal]
#     while path[-1] != start:
#         path.append(came_from[path[-1]])
#     return list(reversed(path))


# # Example graph and coordinates
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }   

# coordinates = {
#     'A': (52.5200, 13.4050),  # Berlin
#     'B': (48.8566, 2.3522),   # Paris
#     'C': (51.5074, -0.1278),  # London
#     'D': (40.7128, -74.0060)  # New York
# }

# g, came_from = a_star(graph, 'A', 'D', coordinates)



import heapq
import math

# --------------------------------------
# Haversine Distance (Heuristic)
# --------------------------------------
def haversine(a, b):
    lat1, lon1 = a
    lat2, lon2 = b
    R = 6371  # Earth radius in KM
    
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    h = (math.sin(d_lat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(d_lon/2)**2)

    return 2 * R * math.asin(math.sqrt(h))


# --------------------------------------
# A* Algorithm
# --------------------------------------
def a_star(graph, start, goal, coordinates):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g = {node: float('inf') for node in graph}
    g[start] = 0

    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for neighbor, dist in graph[current].items():
            temp_g = g[current] + dist

            if temp_g < g[neighbor]:
                g[neighbor] = temp_g
                f = temp_g + haversine(coordinates[neighbor], coordinates[goal])
                heapq.heappush(open_set, (f, neighbor))
                came_from[neighbor] = current

    return g, came_from


# --------------------------------------
# Reconstruct shortest path
# --------------------------------------
def get_path(came_from, start, goal):
    if goal not in came_from:
        return None  # No path
    
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    return path[::-1]


# --------------------------------------
# TEST GRAPH + COORDINATES
# --------------------------------------
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

coordinates = {
    'A': (52.5200, 13.4050),  # Berlin
    'B': (48.8566, 2.3522),   # Paris
    'C': (51.5074, -0.1278),  # London
    'D': (40.7128, -74.0060)  # New York
}

# Run A*
g, came_from = a_star(graph, 'A', 'D', coordinates)

# Build path
path = get_path(came_from, 'A', 'D')

print("Shortest path:", path)
print("Cost:", g['D'])
print("Detailed costs:", g)




# *************************************************




# 🧠 1. Importing Required Libraries

# import heapq
# import math
# ✔ heapq
# Provides a priority queue (min-heap).

# A* uses this to always expand the most promising node first.

# The priority is based on the f-score = g + h.

# ✔ math
# Needed to use trigonometric functions (sin, cos, asin, radians).

# Required for the Haversine formula.

# 🌍 2. Haversine Distance (Heuristic Function)
# def haversine(a, b):
#     lat1, lon1 = a
#     lat2, lon2 = b
#     R = 6371  # Earth radius in KM
    
#     d_lat = math.radians(lat2 - lat1)
#     d_lon = math.radians(lon2 - lon1)

#     h = (math.sin(d_lat/2)**2 +
#          math.cos(math.radians(lat1)) *
#          math.cos(math.radians(lat2)) *
#          math.sin(d_lon/2)**2)

#     return 2 * R * math.asin(math.sqrt(h))

# ✔ Purpose

# This computes the straight-line distance between two coordinates on Earth.

# A* uses this as h(n) (heuristic estimate).

# ✔ Why Haversine?

# Because Uber-like apps need:

# Accurate geospatial distance

# Over a sphere (Earth), not a flat grid

# ✔ Breakdown:

# Convert degrees → radians

# Apply the Haversine formula

# Multiply by Earth radius (in km)

# This gives a realistic geolocation distance.

# ⭐ 3. A* Algorithm Function
# def a_star(graph, start, goal, coordinates):


# This function finds the shortest path from start → goal.

# 🟦 3.1. Priority Queue Initialization
# open_set = []
# heapq.heappush(open_set, (0, start))

# ✔ open_set

# Nodes we still need to explore

# A priority queue sorted by f-score

# We push (0, start) meaning:

# f-score = 0

# node = start

# 🟦 3.2. Initialize g-scores
# g = {node: float('inf') for node in graph}
# g[start] = 0

# ✔ g-score

# g[n] = cost of cheapest known path from start → n

# Everyone starts at infinity

# Except the start node = 0

# 🟦 3.3. Keep track of parents (path reconstruction)
# came_from = {}


# This dictionary stores:

# child → parent


# Example:

# C came from B
# D came from C

# 🟦 3.4. Main Loop
# while open_set:


# Keep running as long as there are nodes left to explore.

# 🟦 3.5. Pop the best node
# _, current = heapq.heappop(open_set)


# This gives us:

# the node with the smallest f-score

# call it current

# 🟦 3.6. Stop if we reached the goal
# if current == goal:
#     break


# A* works because once the goal is popped from the queue, it's the optimal path.

# 🟦 3.7. Explore neighbors
# for neighbor, dist in graph[current].items():


# For each connected node:

# neighbor is the node

# dist is the actual travel cost (g-score addition)

# 🟦 3.8. Calculate temporary g-score
# temp_g = g[current] + dist


# This is:

# cost to reach current

# plus cost from current → neighbor

# 🟦 3.9. If this path is better, update it
# if temp_g < g[neighbor]:
#     g[neighbor] = temp_g


# Only update if you found a cheaper path.

# 🟦 3.10. Compute total f-score
# f = temp_g + haversine(coordinates[neighbor], coordinates[goal])

# ✔ f = g + h

# g = real cost so far

# h = estimated distance to goal (Haversine)

# 🟦 3.11. Push to open set
# heapq.heappush(open_set, (f, neighbor))


# This makes A* always expand the node with the lowest total estimated cost.

# 🟦 3.12. Track parent for path
# came_from[neighbor] = current


# This is used later to rebuild the path.

# 🪢 4. Path Reconstruction
# def get_path(came_from, start, goal):
#     if goal not in came_from:
#         return None
    
#     path = [goal]
#     while path[-1] != start:
#         path.append(came_from[path[-1]])
#     return path[::-1]

# ✔ How it works:

# If the path is:

# A -> B -> C -> D


# came_from contains:

# B came from A
# C came from B
# D came from C


# You start from goal:

# path = [D]
# then C, then B, then A


# Reverse it to get:

# ['A', 'B', 'C', 'D']

# 🌐 5. Example graph

# This is a fake graph just for testing.

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }


# Edges = weighted distances
# Nodes = A, B, C, D

# 🧭 6. Coordinates

# These are real-world geolocations of major cities.

# 🧪 7. Running A*
# g, came_from = a_star(graph, 'A', 'D', coordinates)
# path = get_path(came_from, 'A', 'D')

# print("Shortest path:", path)
# print("Cost:", g['D'])

# 🎉 Final Output:

# You’ll get something like:

# Shortest path: ['A', 'C', 'D']
# Cost: 5

###############################################################################################

# 1. A* on REAL MAPS (OpenStreetMap API)

# A* using real city roads, real GPS coordinates, real distances.
# You give a city → I give you full runnable code.


# Nice — below is a complete, runnable A* pipeline that uses real OpenStreetMap data for any city you give.
# It:

# downloads the road network for the city (via osmnx)

# snaps (map-matches) arbitrary lat/lon start & end to the nearest road nodes

# runs A* using real edge length (meters) and a great-circle/haversine heuristic (also in meters)

# returns the node path, route distance, and plots the route on a map

# I include two A* options:

# astar_networkx() — uses networkx.astar_path (fast, robust)

# astar_custom() — a readable custom A* that works directly on the graph (educational)

# Pick whichever you like. Copy–paste and run locally.

# Requirements / Install

# Run this once in your environment (Linux/Windows/Mac):

# pip install osmnx networkx matplotlib geopandas


# osmnx will download OSM data from the internet the first time you run it.

# Full runnable script
# """
# A* on REAL MAPS (OpenStreetMap)
# - Give a city name (e.g. "Nairobi, Kenya" or "San Francisco, California, USA")
# - Script downloads the city's road graph (osmnx)
# - Snaps start/end coordinates to nearest road nodes
# - Runs A* (NetworkX or custom)
# - Prints path and distance, plots route

# Dependencies:
#     pip install osmnx networkx matplotlib geopandas
# """

# import osmnx as ox
# import networkx as nx
# import math
# import heapq
# import matplotlib.pyplot as plt

# ox.config(use_cache=True, log_console=True)


# # -------------------------
# # Helpers: haversine (meters)
# # -------------------------
# def haversine_m(a, b):
#     """Return great-circle distance between (lat, lon) tuples in meters."""
#     lat1, lon1 = a
#     lat2, lon2 = b
#     R = 6371000  # Earth radius in meters
#     phi1 = math.radians(lat1)
#     phi2 = math.radians(lat2)
#     dphi = math.radians(lat2 - lat1)
#     dlambda = math.radians(lon2 - lon1)

#     x = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
#     return 2 * R * math.asin(math.sqrt(x))


# # -------------------------
# # Build/prepare graph
# # -------------------------
# def get_city_graph(place_name, network_type='drive'):
#     """
#     Download or load the OSM graph for `place_name`.
#     network_type: 'drive' / 'drive_service' / 'walk' / 'bike' etc.
#     Returns a NetworkX MultiDiGraph with edge 'length' in meters.
#     """
#     print(f"Downloading graph for: {place_name}  (this may take a few seconds)...")
#     G = ox.graph_from_place(place_name, network_type=network_type)
#     # ensure every edge has 'length' attribute (osmnx gives length by default)
#     return G


# # -------------------------
# # Snap coordinates to graph nodes (map-matching)
# # -------------------------
# def snap_to_graph(G, point):
#     """
#     point = (lat, lon)
#     returns nearest node id in G (uses osmnx's built-in function)
#     """
#     # osmnx expects (lon, lat) for some functions, but nearest_nodes takes x=lon, y=lat
#     lon, lat = point[1], point[0]
#     node = ox.distance.nearest_nodes(G, X=lon, Y=lat)
#     return node


# # -------------------------
# # Custom A* implementation (works with networkx MultiDiGraph)
# # -------------------------
# def astar_custom(G, source, target, coord_attr=('y', 'x'), weight='length'):
#     """
#     Custom A* returning node path and total cost.
#     G: NetworkX graph with edges having attribute `weight` (e.g., 'length' in meters).
#     coord_attr: node attribute names for latitude and longitude; osmnx nodes use 'y' (lat), 'x' (lon).
#     """

#     # Heuristic function using node coordinates (meters)
#     def heuristic(u, v):
#         u_lat, u_lon = G.nodes[u][coord_attr[0]], G.nodes[u][coord_attr[1]]
#         v_lat, v_lon = G.nodes[v][coord_attr[0]], G.nodes[v][coord_attr[1]]
#         return haversine_m((u_lat, u_lon), (v_lat, v_lon))

#     # g-score
#     g = {n: float('inf') for n in G.nodes}
#     g[source] = 0

#     # parent map to reconstruct path
#     came_from = {}

#     # priority queue with f-score and node id
#     open_heap = []
#     heapq.heappush(open_heap, (heuristic(source, target), source))

#     visited = set()

#     while open_heap:
#         f_current, current = heapq.heappop(open_heap)
#         if current == target:
#             # reconstruct path
#             path = [current]
#             while path[-1] != source:
#                 path.append(came_from[path[-1]])
#             path.reverse()
#             return path, g[target]
#         if current in visited:
#             continue
#         visited.add(current)

#         # iterate neighbors: for directed MultiDiGraph, use G[current]
#         for nbr, nbr_data in G[current].items():
#             # MultiDiGraph: nbr_data is a dict keyed by edge key -> attributes
#             # iterate each parallel edge
#             for key, attr in nbr_data.items():
#                 w = attr.get(weight, 1.0)  # default to 1.0 if missing
#                 tentative_g = g[current] + w
#                 if tentative_g < g[nbr]:
#                     g[nbr] = tentative_g
#                     came_from[nbr] = current
#                     f = tentative_g + heuristic(nbr, target)
#                     heapq.heappush(open_heap, (f, nbr))

#     # no path found
#     return None, float('inf')


# # -------------------------
# # NetworkX A* wrapper (recommended for production/test)
# # -------------------------
# def astar_networkx(G, source, target, weight='length', coord_attr=('y', 'x')):
#     """
#     Use networkx.astar_path with a great-circle heuristic.
#     Returns path (list of nodes) and path length (meters).
#     """
#     def h(u, v):
#         u_lat, u_lon = G.nodes[u][coord_attr[0]], G.nodes[u][coord_attr[1]]
#         v_lat, v_lon = G.nodes[v][coord_attr[0]], G.nodes[v][coord_attr[1]]
#         return haversine_m((u_lat, u_lon), (v_lat, v_lon))

#     try:
#         path = nx.astar_path(G, source, target, heuristic=h, weight=weight)
#         # compute length
#         length = nx.path_weight(G, path, weight=weight)
#         return path, length
#     except nx.NetworkXNoPath:
#         return None, float('inf')


# # -------------------------
# # Helper to plot route
# # -------------------------
# def plot_route(G, path, figsize=(10, 10), show=True, save_to=None):
#     fig, ax = ox.plot_graph_route(G, path, figsize=figsize, route_linewidth=4, node_size=0, show=False)
#     if save_to:
#         fig.savefig(save_to, bbox_inches='tight', dpi=150)
#     if show:
#         plt.show()
#     plt.close(fig)


# # -------------------------
# # Example usage function
# # -------------------------
# def route_between_points(city_name, start_point, end_point,
#                          method='networkx', network_type='drive', plot=True):
#     """
#     city_name: string for osmnx (e.g., 'Nairobi, Kenya' or 'San Francisco, California, USA')
#     start_point, end_point: (lat, lon) tuples
#     method: 'networkx' or 'custom'
#     """

#     # 1. load graph for city
#     G = get_city_graph(city_name, network_type=network_type)

#     # 2. snap start & end to nearest graph nodes
#     start_node = snap_to_graph(G, start_point)
#     end_node = snap_to_graph(G, end_point)
#     print("Start node:", start_node, "End node:", end_node)

#     # 3. run chosen A*
#     if method == 'networkx':
#         path, length = astar_networkx(G, start_node, end_node)
#     else:
#         path, length = astar_custom(G, start_node, end_node)

#     if path is None:
#         print("No path found between these nodes.")
#         return None

#     print(f"Found path of {len(path)} nodes, distance ≈ {length:.1f} meters")

#     # 4. Optional plot
#     if plot:
#         plot_route(G, path)

#     # 5. Return human-friendly route: list of (lat, lon) and distance
#     route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
#     return {
#         'node_path': path,
#         'coordinates': route_coords,
#         'distance_m': length
#     }


# # -------------------------
# # If run as script: example (change city and coordinates as you want)
# # -------------------------
# if __name__ == "__main__":
#     # Example: Nairobi center coords (change to any start/end)
#     city = "Nairobi, Kenya"

#     # Example start/end: you can put arbitrary lat/lon within city bounds
#     # Use any real lat/lon coords — they will be snapped to nearest road nodes
#     start = ( -1.286389, 36.817223 )  # Nairobi CBD (lat, lon)
#     end   = ( -1.292066, 36.821946 )  # a nearby point in Nairobi

#     print("Running route search ...")
#     result = route_between_points(city, start, end, method='networkx', plot=True)

#     if result:
#         print("Distance (m):", result['distance_m'])
#         print("Node path (first 6 nodes):", result['node_path'][:6])
#         print("Coordinates (first 6):", result['coordinates'][:6])

# Notes & explanations (short)

# osmnx fetches and builds a routable road graph — nodes have 'y' = latitude, 'x' = longitude, edges have 'length' in meters. That makes weights consistent with our Haversine heuristic (also in meters).

# We snap arbitrary user GPS coords to the nearest road node (snap_to_graph) — that’s the essential map-matching step.

# For production you’ll want to:

# cache city graphs and preprocess (contraction hierarchies or CH, or use routing engines like OSRM/Valhalla)

# use bidirectional search, turn penalties, live traffic weights

# handle edge cases (no path, islands, disconnected regions)

# For visualization we use ox.plot_graph_route, which draws a nice map with the route polyline.



# Sweet — I’ll build the FastAPI routing service for you right now.
# It exposes a POST /route endpoint that:

# downloads / caches an OpenStreetMap road graph for a city (osmnx)

# map-matches start/end lat/lon to nearest road nodes

# runs A* (NetworkX implementation) on the graph (uses real edge length in meters)

# returns node path, coordinates (lat/lon), and distance in meters

# accepts optional params (method, network_type, traffic_multiplier)

# I also add sensible caching so repeated requests for the same city don’t re-download the map every call.

# Files you’ll get

# main.py — the FastAPI app (copy–paste and run)

# requirements.txt — packages to install

# Example curl and uvicorn commands to run & test

# 1) requirements.txt
# fastapi
# uvicorn[standard]
# osmnx
# networkx
# geopandas
# shapely
# matplotlib


# Install with:
# pip install -r requirements.txt
# (On some systems osmnx/geopandas require system packages — see osmnx docs if you hit install errors.)

# 2) main.py (copy–paste this)
# # main.py
# from functools import lru_cache
# from typing import Tuple, Optional, Dict, Any
# import math
# import heapq

# import osmnx as ox
# import networkx as nx
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, conlist
# import uvicorn

# ox.config(use_cache=True, log_console=False)

# # -----------------------------
# # Request / Response Models
# # -----------------------------
# class RouteRequest(BaseModel):
#     city: str
#     start: conlist(float, min_items=2, max_items=2)  # [lat, lon]
#     end: conlist(float, min_items=2, max_items=2)    # [lat, lon]
#     method: Optional[str] = "networkx"               # "networkx" or "custom"
#     network_type: Optional[str] = "drive"            # 'drive', 'walk', etc.
#     traffic_multiplier: Optional[float] = 1.0        # multiplier applied to edge lengths (>=0.0)


# class RouteResponse(BaseModel):
#     node_path: Optional[list]
#     coordinates: Optional[list]
#     distance_m: float
#     message: Optional[str] = None


# # -----------------------------
# # Helpers: haversine in meters
# # -----------------------------
# def haversine_m(a: Tuple[float, float], b: Tuple[float, float]) -> float:
#     lat1, lon1 = a
#     lat2, lon2 = b
#     R = 6371000  # meters
#     phi1 = math.radians(lat1)
#     phi2 = math.radians(lat2)
#     dphi = math.radians(lat2 - lat1)
#     dlambda = math.radians(lon2 - lon1)
#     x = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
#     return 2 * R * math.asin(math.sqrt(x))


# # -----------------------------
# # Cache graphs per (city, network_type)
# # -----------------------------
# @lru_cache(maxsize=8)
# def get_city_graph_cached(city_name: str, network_type: str = "drive"):
#     """
#     Downloads / loads and returns a NetworkX MultiDiGraph from osmnx.
#     Cached in memory via lru_cache keyed by (city_name, network_type).
#     """
#     print(f"[graph] downloading/creating graph for: {city_name} ({network_type})")
#     G = ox.graph_from_place(city_name, network_type=network_type)
#     # osmnx provides 'length' on edges by default; ensure symmetric weights for easy usage
#     return G


# # -----------------------------
# # Snap to graph node (map-match)
# # -----------------------------
# def snap_to_graph(G: nx.Graph, point: Tuple[float, float]) -> int:
#     # ox.distance.nearest_nodes expects X=lon, Y=lat
#     lon, lat = point[1], point[0]
#     node = ox.distance.nearest_nodes(G, X=lon, Y=lat)
#     return node


# # -----------------------------
# # NetworkX A* wrapper
# # -----------------------------
# def astar_networkx(G: nx.Graph, source: int, target: int, weight: str = "length", coord_attr: tuple = ('y', 'x')) -> Tuple[Optional[list], float]:
#     def h(u, v):
#         u_lat, u_lon = G.nodes[u][coord_attr[0]], G.nodes[u][coord_attr[1]]
#         v_lat, v_lon = G.nodes[v][coord_attr[0]], G.nodes[v][coord_attr[1]]
#         return haversine_m((u_lat, u_lon), (v_lat, v_lon))
#     try:
#         path = nx.astar_path(G, source, target, heuristic=h, weight=weight)
#         length = nx.path_weight(G, path, weight=weight)
#         return path, length
#     except nx.NetworkXNoPath:
#         return None, float('inf')


# # -----------------------------
# # Custom A* (educational fallback)
# # -----------------------------
# def astar_custom(G: nx.Graph, source: int, target: int, weight: str = "length", coord_attr: tuple = ('y', 'x')) -> Tuple[Optional[list], float]:
#     def heuristic(u, v):
#         u_lat, u_lon = G.nodes[u][coord_attr[0]], G.nodes[u][coord_attr[1]]
#         v_lat, v_lon = G.nodes[v][coord_attr[0]], G.nodes[v][coord_attr[1]]
#         return haversine_m((u_lat, u_lon), (v_lat, v_lon))

#     g = {n: float('inf') for n in G.nodes}
#     g[source] = 0
#     came_from = {}
#     open_heap = []
#     heapq.heappush(open_heap, (heuristic(source, target), source))
#     visited = set()

#     while open_heap:
#         f_current, current = heapq.heappop(open_heap)
#         if current == target:
#             path = [current]
#             while path[-1] != source:
#                 path.append(came_from[path[-1]])
#             path.reverse()
#             return path, g[target]
#         if current in visited:
#             continue
#         visited.add(current)
#         for nbr, nbr_dict in G[current].items():
#             # handle MultiDiGraph: each key has attributes
#             for key, attr in nbr_dict.items():
#                 w = attr.get(weight, 1.0)
#                 tentative_g = g[current] + w
#                 if tentative_g < g[nbr]:
#                     g[nbr] = tentative_g
#                     came_from[nbr] = current
#                     f = tentative_g + heuristic(nbr, target)
#                     heapq.heappush(open_heap, (f, nbr))
#     return None, float('inf')


# # -----------------------------
# # FastAPI app
# # -----------------------------
# app = FastAPI(title="Simple A* Routing Service (OSMnx)")

# @app.post("/route", response_model=RouteResponse)
# def route(req: RouteRequest):
#     # Basic validation
#     if req.traffic_multiplier < 0:
#         raise HTTPException(status_code=400, detail="traffic_multiplier must be >= 0")

#     # Load / get graph
#     try:
#         G = get_city_graph_cached(req.city, req.network_type)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to load graph for city: {e}")

#     # Snap start/end to nodes
#     try:
#         start_node = snap_to_graph(G, tuple(req.start))
#         end_node = snap_to_graph(G, tuple(req.end))
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Failed to snap coordinates: {e}")

#     # Optionally modify edge weights by traffic multiplier (non-destructive in-memory shallow copy)
#     if req.traffic_multiplier != 1.0:
#         # Create a temporary view with adjusted 'length' accessible at 'tmp_length' attribute
#         # We'll feed the 'tmp_length' into the A* call as weight if multiplier != 1
#         for u, v, k, data in G.edges(keys=True, data=True):
#             base = data.get('length', 1.0)
#             data['_tmp_length'] = base * req.traffic_multiplier
#         weight_attr = '_tmp_length'
#     else:
#         weight_attr = 'length'

#     # Choose method
#     method = req.method.lower()
#     if method not in ('networkx', 'custom'):
#         raise HTTPException(status_code=400, detail="method must be 'networkx' or 'custom'")

#     # Run A*
#     if method == 'networkx':
#         path, length = astar_networkx(G, start_node, end_node, weight=weight_attr)
#     else:
#         path, length = astar_custom(G, start_node, end_node, weight=weight_attr)

#     if path is None:
#         return RouteResponse(node_path=None, coordinates=None, distance_m=float('inf'), message="No path found")

#     route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
#     return RouteResponse(node_path=path, coordinates=route_coords, distance_m=length, message="OK")


# # -----------------------------
# # Run with uvicorn for local dev
# # -----------------------------
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# 3) How to run locally

# create virtual env, install deps:

# python -m venv venv
# source venv/bin/activate        # or venv\Scripts\activate on Windows
# pip install -r requirements.txt


# run the server:

# uvicorn main:app --host 0.0.0.0 --port 8000


# First time a city is requested the server will download OSM data (may take 5–30s depending on city size & connection). Cached for repeated calls.

# 4) Example curl test
# curl -X POST "http://127.0.0.1:8000/route" \
#   -H "Content-Type: application/json" \
#   -d '{
#     "city": "Nairobi, Kenya",
#     "start": [-1.286389, 36.817223],
#     "end": [-1.292066, 36.821946],
#     "method": "networkx",
#     "network_type": "drive",
#     "traffic_multiplier": 1.0
#   }'


# Response example:

# {
#   "node_path": [123456789, 987654321, ...],
#   "coordinates": [[-1.2865,36.8171],[...]],
#   "distance_m": 620.5,
#   "message": "OK"
# }

# 5) Production notes & next steps (quick)

# Scale / performance: for city-level production, use a dedicated routing engine (OSRM, Valhalla) or preprocess with contraction hierarchies. OSMnx is great for prototyping.

# Traffic: we applied a simple traffic_multiplier to edge lengths. For production you'd have a real-time traffic feed that updates edge travel times.

# Turn penalties / restrictions: use OSM turn restrictions or enrich edges with turn-costs.

# Bidirectional search: NetworkX A* is one-way; OSRM/Valhalla support optimized bidirectional and CH.

# Map-matching: currently nearest node snapping; for noisy GPS use a map-matching library (valhalla/match or own HMM-based matcher).

# Caching: lru_cache keeps graphs in memory; for many cities use a persistent store or pre-download and load from disk.

# Security: validate user input, rate-limit endpoints, and secure the API.

# If you want, I’ll next:

# convert this into a Dockerfile + docker-compose for easy deploy, OR

# add a FastAPI HTML page where you paste start/end and it plots the returned polyline on a Leaflet/Mapbox map, OR

# show how to switch to OSRM (faster, production-grade) and demo requests.
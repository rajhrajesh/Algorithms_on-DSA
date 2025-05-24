# Step 1: Define the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Step 2: Define the cost table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Step 3: Define the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Step 4: Track processed nodes
processed = []

# Step 5: Function to find the lowest-cost unprocessed node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Step 6: Main loop of Dijkstra's algorithm
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost           # ✅ FIXED: update the cost
            parents[n] = node             # ✅ FIXED: update the parent
    processed.append(node)
    node = find_lowest_cost_node(costs)

# Step 7: Output the final costs and parents
print("Final Costs:", costs)
print("Final Parents:", parents)

# Step 8 (Optional): Reconstruct the shortest path
def reconstruct_path(parents, end):
    path = [end]
    while end in parents and parents[end] is not None:
        end = parents[end]
        path.insert(0, end)
    return path

shortest_path = reconstruct_path(parents, "fin")
print("Shortest Path:", " -> ".join(shortest_path))

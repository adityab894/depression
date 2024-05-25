import heapq

# Define grid size
rows = 6
cols = 4

# Define obstacle coordinates
obstacles = [(3, 3), (1, 4), (4, 2)]

# Define heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Define A* algorithm
def astar(start, goal):
    # Initialize open list and closed list
    open_list = []
    closed_list = set()

    # Add start node to open list
    heapq.heappush(open_list, (0, start))

    # Initialize cost and parent dictionaries
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        # Get node with lowest cost from open list
        current_cost, current_node = heapq.heappop(open_list)

        # Check if goal reached
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]

        # Add current node to closed list
        closed_list.add(current_node)

        # Generate neighbors
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current_node[0] + dx, current_node[1] + dy)

            # Check if neighbor is within bounds
            if (0 <= neighbor[0] < rows) and (0 <= neighbor[1] < cols):
                # Check if neighbor is not an obstacle and not in closed list
                if neighbor not in obstacles and neighbor not in closed_list:
                    # Calculate tentative cost
                    new_cost = cost[current_node] + 1

                    # Check if neighbor is not in open list or new cost is lower
                    if neighbor not in cost or new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        priority = new_cost + heuristic(neighbor, goal)
                        heapq.heappush(open_list, (priority, neighbor))
                        parent[neighbor] = current_node

    # If no path found
    return None

# Define start and goal coordinates
start = (4, 6)
goal = (1, 1)

# Find shortest path
path = astar(start, goal)
if path:
    print("Shortest Path:", path)
else:
    print("No path found")
```

This code defines a grid, obstacle coordinates, heuristic function, and implements the A* algorithm to find the shortest path from the start to the goal while avoiding obstacles.
import heapq
import math

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula to calculate distance
    slat = lat2 - lat1
    Elon = lon2 - lon1
    a = math.sin(slat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(Elon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return c * r

def determine_direction(lat1, lon1, lat2, lon2):
    lat_Diff = lat2 - lat1
    lon_Diff = lon2 - lon1

    if lat_Diff > 0 and lon_Diff > 0:
        return 'NE'
    elif lat_Diff > 0 > lon_Diff:
        return 'NW'
    elif lat_Diff < 0 < lon_Diff:
        return 'SE'
    elif lat_Diff < 0 and lon_Diff < 0:
        return 'SW'
    elif lat_Diff > 0:
        return 'N'
    elif lon_Diff < 0:
        return 'S'
    elif lon_Diff > 0:
        return 'E'
    else:
        return 'W'


def dijikstra(graph, start, end):
    queue = [(0, start, [])]
    heapq.heapify(queue)

    visited = set()
    min_dist = {start: 0}
    heading_direction = {start: [('N', 'N')]}
    node_info = {start: (graph[start][0][0], 0)}

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return cost, path, heading_direction[node], node_info

        for next_node, distance, direction, in graph.get(node, []):
            if next_node in visited:
                continue
            prev = min_dist.get(next_node, None)
            next_dist = cost + distance
            if prev is None or next_dist < prev:
                heapq.heappush(queue, (next_dist, next_node, path))
                heading_direction[next_node] = heading_direction[node] + [(next_node, direction)]
                node_info[next_node] = (next_node, next_dist)

    return float("intf"), [], [], {}

def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))

    for _ in range(num_edges):
        start_node = input("Enter the starting node: ")
        while True:
            end_node = input("Enter the ending node: ")
            lat1 = float(input(f"Enter the latitude of {start_node}: "))
            lon1 = float(input(f"Enter the longitude of {start_node}: "))
            lat2 = float(input(f"Enter the latitude of {end_node}: "))
            lon2 = float(input(f"Enter the longitude of {end_node}: "))

            distance = haversine(lat1, lon1, lat2, lon2)
            direction = determine_direction(lat1, lon1, lat2, lon2)

            if start_node not in graph:
                graph[start_node] = []

            graph[start_node].append((end_node, distance, direction))

            add_node = input("Do you want to add another connection from this node? (y/n): ")
            if add_node.lower() != 'y':
                break

    return graph

def main():
    graph = create_graph()

    start = input("Enter the start point: ")
    end = input("Enter the end point: ")

    distance, path, heading, node_info = dijikstra(graph, start, end)

    if path:
        path_output = " ----> ".join([f"{node} ({direction})" for node, direction in heading[1:]])
        print(f"Path: {start} (N) ----> {path_output}")
        print(f"Shortest distance covered: {distance:.2f} km")

        print("\nVertex\t\tDistance from Source")
        for node, info in node_info.items():
            lat_lon, dist = info
            print(f"{lat_lon}\t\t{dist:.2f} km")

    else:
        print("No path found")

if __name__ == "__main__":
    main()
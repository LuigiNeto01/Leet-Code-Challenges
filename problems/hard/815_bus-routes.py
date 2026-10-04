from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        # If source and target are the same, no bus is needed.
        if source == target:
            return 0

        # Build a mapping: stop -> list of bus indices that serve that stop.
        stop_to_buses = defaultdict(list)
        for bus_idx, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus_idx)

        # BFS queue: (current_stop, number_of_buses_taken)
        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = [False] * len(routes)  # mark bus routes once used

        while queue:
            stop, buses_taken = queue.popleft()

            # If we reached target, return the count of buses taken.
            if stop == target:
                return buses_taken

            # Iterate over all buses that serve this stop.
            for bus_idx in stop_to_buses[stop]:
                if visited_buses[bus_idx]:
                    continue
                visited_buses[bus_idx] = True

                # Add all unvisited stops of this bus to the queue.
                for next_stop in routes[bus_idx]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))

        # If BFS finishes without reaching target, it's impossible.
        return -1
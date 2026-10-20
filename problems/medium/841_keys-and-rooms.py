class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n          # track which rooms we have entered
        stack = [0]                    # start from room 0 (unlocked)
        visited[0] = True
        count = 1                      # number of visited rooms (room 0 counted)

        # DFS using a stack (iterative to avoid recursion depth issues)
        while stack:
            room = stack.pop()
            for key in rooms[room]:    # each key is a room number
                if not visited[key]:
                    visited[key] = True
                    count += 1
                    stack.append(key)  # we can now explore the newly opened room

        # we visited all rooms if count equals total number of rooms
        return count == n
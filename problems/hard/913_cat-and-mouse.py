from collections import deque

class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n = len(graph)

        # dp[m][c][t]:
        #   m = mouse position, c = cat position
        #   t = 0: mouse's turn, t = 1: cat's turn
        #   0 = unknown/draw, 1 = mouse wins, 2 = cat wins
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # Number of legal moves from each state.
        # It helps detect when every move leads to a loss.
        deg = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        q = deque()

        for m in range(n):
            for c in range(1, n):  # cat can never be at hole 0
                for t in range(2):
                    if t == 0:
                        deg[m][c][t] = len(graph[m])
                    else:
                        deg[m][c][t] = sum(1 for x in graph[c] if x != 0)

                    # Terminal states:
                    # Mouse reaches the hole -> mouse wins.
                    if m == 0:
                        dp[m][c][t] = 1
                        q.append((m, c, t))
                    # Cat catches the mouse -> cat wins.
                    elif m == c:
                        dp[m][c][t] = 2
                        q.append((m, c, t))

        while q:
            m, c, t = q.popleft()
            result = dp[m][c][t]

            if t == 0:
                # Current state was reached by a cat move from pc to c.
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if dp[m][pc][1] != 0:
                        continue

                    if result == 2:
                        # Cat can move into a winning state.
                        dp[m][pc][1] = 2
                        q.append((m, pc, 1))
                    elif result == 1:
                        # This child is bad for the cat parent.
                        deg[m][pc][1] -= 1
                        if deg[m][pc][1] == 0:
                            dp[m][pc][1] = 1
                            q.append((m, pc, 1))
            else:
                # Current state was reached by a mouse move from pm to m.
                for pm in graph[m]:
                    if dp[pm][c][0] != 0:
                        continue

                    if result == 1:
                        # Mouse can move into a winning state.
                        dp[pm][c][0] = 1
                        q.append((pm, c, 0))
                    elif result == 2:
                        # This child is bad for the mouse parent.
                        deg[pm][c][0] -= 1
                        if deg[pm][c][0] == 0:
                            dp[pm][c][0] = 2
                            q.append((pm, c, 0))

        return dp[1][2][0]
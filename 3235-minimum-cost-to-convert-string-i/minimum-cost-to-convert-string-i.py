class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = 26

        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            if w < dist[u][v]:
                dist[u][v] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')

            if dist[u][v] == INF:
                return -1

            ans += dist[u][v]

        return ans
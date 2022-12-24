import sys

maxnum = 10000000
queue = list()

to = 6
where = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

n = int(input())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
visited = [[maxnum] * n for i in range(n)]
queue.append([r1, c1, 0])


def bfs():
    while len(queue):
        cur = queue[0]
        queue.pop(0)
        x = cur[0]
        y = cur[1]
        step = cur[2]


        # 만약 현재 step이 최종 목적지 방문했을 때보다 더 크다면 삭제
        if step > visited[r2][c2]:
            continue

        # 만약 현재 위치를 방문했던 것보다 더 크면 삭제
        if step >= visited[cur[0]][cur[1]]:
            continue

        visited[x][y] = step

        if x == r2 and y == c2:
            if step < visited[r2][c2]:
                visited[r2][c2] = step
            continue

        for i in where:
            if 0 <= x + i[0] < n and n > y + i[1] >= 0:
                queue.append([x + i[0], y + i[1], step + 1])


def showdata():
    for i in range(n):
        print(visited[i])


bfs()
if visited[r2][c2] == maxnum:
    print("-1")
else:
    print(visited[r2][c2])

segments = []

with open("data_prog_contest_problem_1.txt", "r", encoding='utf-8') as file:
    n = int(file.readline())
    for _ in range(n):
        start, end = map(int, file.readline().split())
        segments.append((start, end))
    segments.sort(key=lambda x: x[1])

points = []
last_point = -1

for start, end in segments:
    if start > last_point:
        last_point = end
        points.append(last_point)

print(f"Минимальное количество точек: {len(points)}")
print(f"Сами точки: {points}")

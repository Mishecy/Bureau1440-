f0, f1 = 1, 3
A = [f0, f1]

while len(A) < 40:
    next_f = 5 * f1 + f0
    if next_f % 2 == 1:
        A.append(next_f)
    f0, f1 = f1, next_f

print(A[39])
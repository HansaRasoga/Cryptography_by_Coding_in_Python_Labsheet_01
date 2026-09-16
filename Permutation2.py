def faculty(n):
    if n<=1:
        return n
    else:
        return faculty(n-1)*n
for i in range(10):
    print(faculty(i))
    
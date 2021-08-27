def select(t):
  n = len(t)
  for i in range(n):
    minimum = i
    for j in range(i+1, n):
      if t[minimum] > t[j]:
        minimum = j
    t[i], t[minimum] = t[minimum], t[i]
  return t
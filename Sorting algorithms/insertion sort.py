def insert_sort(t):
  n = len(t)
  for i in range(1,n):
    key = t[i]
    j=i-1
    while j>=0 and key<t[j]:
      t[j+1]=t[j]
      j-=1
    t[j+1]=key
  return t


def tribonacci(x, n):
  nx = [i for i in x]
  tribonaci = []
  if n == 3:
    for i in range(n):
      new_element = sum(nx)
      nx.append(new_element)
      tri = nx.pop(0)
      tribonacci.append(tri)
    return(tribonacci)
  else:
    return(nx)

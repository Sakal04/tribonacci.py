def tribonacci(x, n):
  
  tribonaci = []
  if len(x) == 3:
    nx = [i for i in x]
    for i in range(n):
      new_element = sum(nx)
      nx.append(new_element)
      tri = nx.pop(0)
      tribonacci.append(tri)
    return(tribonacci)
  else:
    return(nx)

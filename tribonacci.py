def tribonaci(lis_t, n):
	if len(lis_t) == 3:
		tri = []
		xlis_t = [int(i) for i in lis_t]
	for i in range(n):
		new_element = sum(xlis_t)
		xlis_t.append(new_element)
		elem = xlis_t.pop(0)
		tri.append(elem)
  print(tri) 
tribonaci(lis, n)

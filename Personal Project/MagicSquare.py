def Square(n):

	magicSq = [[0 for x in range(n)]
				for y in range(n)]
	i = n // 2
	j = n - 1
	a = 1

	while a <= (n * n):
		if i == -1 and j == n: 
			j = n - 2
			i = 0
		else:
			if j == n:
				j = 0
			if i < 0:
				i = n - 1

		if magicSq[int(i)][int(j)] != 0: 
			j = j - 2
			i = i + 1
			continue
		else:
			magicSq[int(i)][int(j)] = a
			a = a + 1

		j = j + 1
		i = i - 1


	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magicSq[i][j]),
				end='')
			if j == n - 1:
				print()    
    


n=13
print("Sum of each row or column",
	 n * (n * n + 1) // 2, "\n")  
Square(n)
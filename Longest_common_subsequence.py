def lcs(x,y):
	m , n = len(x) , len(y)
	mat = [[0 for i in range(m+1)] for i in range(n+1)]
	for indx , i in enumerate(y):
		for indy , j in enumerate(x):
			if i==j:
				mat[indx+1][indy+1] = mat[indx][indy] + 1
			else:
				mat[indx+1][indy+1] = max(mat[indx+1][indy] , mat[indx][indy+1])

	print(mat[n][m])

x = str(input())
lcs(x,x[::-1])

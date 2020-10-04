x = 'ABBDCACB'
y = x[::-1]

def lcs(x,y,n,mat):
	
	for indx , i in enumerate(x):
		for indy , j in enumerate(y):
			if i==j:
				mat[indx+1][indy+1] = mat[indx][indy] + 1
			else:
				mat[indx+1][indy+1] = max(mat[indx+1][indy] , mat[indx][indy+1]) 
	# print(mat[n][n])
	for i in mat:
		print(i)

	p=q=n
	# print(s)

def print_lps(x , y , m , n , mat):
	if m==0 or n==0:
		return ""

	if x[m-1] == y[n-1]:
		return print_lps(x , y , m-1 , n-1 , mat) + x[m-1]

	if mat[m-1][n] > mat[m][n-1]:
		return print_lps(x , y , m-1 , n , mat)

	return print_lps(x , y , m , n-1 , mat)



n = len(x)
mat = [[0 for i in range(n+1)] for j in range(n+1)]
lcs(x,y,n,mat)
print(print_lps(x,y,n,n,mat))

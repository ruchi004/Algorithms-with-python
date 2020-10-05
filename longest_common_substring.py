x = 'abc'
y = 'baba'

def lcs(x,y,mat):
	print(x,y)
	maxlength = 0                         #stores the maximum length of substring
	endindex = len(x)                     #stores ending index of lcs within x

	for indx , i in enumerate(x):
		for indy , j in enumerate(y):

			if i==j:
				mat[indx+1][indy+1] = mat[indx][indy] + 1
				if mat[indx+1][indy+1] > maxlength:
					maxlength = mat[indx+1][indy+1]
					endindex = indx

			else:
				mat[indx+1][indy+1] = 0 

	for i in mat:
		print(i)
	print(x[endindex-maxlength+1 : endindex+1])

mat = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
lcs(x,y,mat)
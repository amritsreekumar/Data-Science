x = []
bias = 0
print(" Enter the number of inputs")
n = int(input())
print("Enter the number of input vectors")
n1 = int(input())
w = [0] * n1
for i in range(0,n):
	for j in range(0,n1):
		print ("Enter input number: " + str(j+1))
		x.insert(j, int(input()))
	print("Enter the output")
	y = int(input())
	for k in range(0,n1):
		dw = x[k]*y
		w[k] = w[k] + dw
	db = y
	bias = bias + db


    

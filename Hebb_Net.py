import numpy as np 
import matplotlib.pyplot as plt
x = []
bias = 0
print(" Enter the number of inputs")
n = int(input())
print("Enter the number of input vectors")
n1 = int(input())
w = [0] * n1
for i in range(0,n):
	for j in range(0,n1):
		print ("Enter input number " + str(j+1) + " of " + str(i+1))
		x.insert(j, int(input()))
	print("Enter the output")
	y = int(input())
	if y == 1:
		plt.plot(x[0], x[1], 'bo')
	else:
		plt.plot(x[0], x[1], 'ro')
	for k in range(0,n1):
		dw = x[k]*y
		w[k] = w[k] + dw
	db = y
	bias = bias + db
print("The values of updated weights are:")
for j in range(0,n1):
	print(w[j])
print("The final value of the bias is: " + str(bias))
x = np.arange(-4,4)
y = (-bias/w[1])-(x*(w[0]/w[1]))
plt.plot(x, y)
plt.show()


   

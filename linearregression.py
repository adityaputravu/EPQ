import numpy as np
from constants import *
from random import randint, shuffle
import matplotlib.pyplot as plt
from sklearn import preprocessing

def simple_linear_regression(x_dataset_train, y_dataset_train, n):
	x_bar = sum(x_dataset_train[:n]) / n
	y_bar = sum(y_dataset_train[:n]) / n
	sxx,sxy,syy = 0,0,0

	for i in range(n):
		sxx += pow(x_dataset_train[i]-x_bar, 2)
		syy += pow(y_dataset_train[i]-y_bar, 2)
		sxy += (x_dataset_train[i]-x_bar) * (y_dataset_train[i]-y_bar)

	r = sxy / pow(sxx * syy, 0.5)
	m = sxy / sxx
	c = y_bar - m*x_bar

	# r -> correlation
	# m -> gradient
	# c -> y-intercept

	return r, m, c

def linear_regression_accuracy(m, c, x_dataset_test, y_dataset_test, n):
	predicted = lambda _m, x, _c: _m*x + _c
	y_bar = sum(y_dataset_test[:n]) / n

 	# The deviation from the predicted line
 	# If this is small, the deviation is small so the line is a better fit
	SE_line = sum([pow(y_dataset_test[i] - predicted(m, x_dataset_test[i], c), 2) for i in range(n)])

	# The total deviation of the (testing) dataset
	SE_y_bar = sum([pow(y_dataset_test[i] - y_bar, 2) for i in range(n)])

	# 1 - (SE_line / SE_y_bar) gives the accuracy that the line DOES work rather than when it DOESNT work
	return pow(1-(SE_line / SE_y_bar), 0.5)


def gradient_descent_linear_regression(x_dataset_train, y_dataset_train, n, epochs, gamma=0.01):
	m, c = 0, 0
	for _ in range(epochs):
		y_pred = [y_dataset_train[i] - m*x_dataset_train[i] - c for i in range(n)]
		d_m = -2 * sum([y_pred[i] * x_dataset_train[i] for i in range(n)]) / n
		d_c = -2 * sum(y_pred) / n

		#print(f'm: {m}, c: {c}, d_c: {d_c}, d_m: {d_m}')
		m = m - (gamma * d_m)
		c = c - (gamma * d_c)

	return m, c

def normalise(dataset, min_int=-1, max_int=1):
	min_dat = min(dataset)
	max_dat = max(dataset)
	return [((max_int-min_int)*(i-min_dat)/(max_dat-min_dat)) + min_int for i in dataset]

def standardise(dataset):
	n = len(dataset)
	x_bar = sum(dataset) / n
	sigma = pow(sum([pow(x,2) for x in dataset]), 0.5)
	return [(x - x_bar) / sigma for x in dataset]

# x = dates
# y = open
n = 300
train_x, train_y = DATES[:n], OPEN[:n]
test_x, test_y = DATES[n:2*n], OPEN[n:2*n]
train_x, train_y = [i for i in range(n)], [i*4 + randint(-0.3 * n, 0.3 * n) for i in range(n)]
test_x, test_y = [n+i for i in range(n)], [(n+i)*4 + randint(-0.3 * n, 0.3 * n) for i in range(n)]

train_x, train_y = normalise(train_x), normalise(train_y)
test_x, test_y = normalise(test_x), normalise(test_y)



m, c = gradient_descent_linear_regression(train_x, train_y, n, 1000)
a, m1, c1 = simple_linear_regression(train_x, train_y, n)

print(f'Simple:   y = {m1}x + {c1}')
print(f'Gradient: y = {m}x + {c}')
 
plt.figure(1)
plt.ylabel('open / USD') 
plt.xlabel('Time (unix timestamp) / s') 
plt.title("Linear Regression Example")

plt.plot(train_x, train_y, label='open_train')

y = [(train_x[i]*m) + c for i in range(n)]
plt.plot(train_x, y, label='predicted_train_gradient_descent')

y = [(train_x[i]*m1) + c1 for i in range(n)]
#plt.plot(train_x, y, label='predicted_train_simple')

plt.legend()
plt.show()

plt.figure(2)
plt.ylabel('open / USD') 
plt.xlabel('Time (unix timestamp) / s') 
plt.title("Linear Regression Example")

plt.plot(test_x, test_y, label='open_test')
y = [(test_x[i]*m) + c for i in range(n)]
#print(f'\nt_x: {test_x}\nt_y: {test_y}\n\ny: {y}')
plt.plot(test_x, y, label='predicted_test_gradient_descent')
y = [(test_x[i]*m1) + c1 for i in range(n)]
#plt.plot(test_x, y, label='predicted_test_simple')
plt.legend()
plt.show()

print(f'Accuracy: {linear_regression_accuracy(m, c, test_x, test_y, n)*100}%')
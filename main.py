from constants import *
import matplotlib.pyplot as plt

def linear_regression(x_dataset, y_dataset, n):
	x_bar = sum(x_dataset[:n]) / n
	y_bar = sum(y_dataset[:n]) / n
	sxx,sxy = 0,0

	for i in range(n):
		sxx += pow(x_dataset[i]-x_bar, 2)
		sxy += (x_dataset[i]-x_bar) * (y_dataset[i]-y_bar)

	r = sxy / pow(sxx * sxy, 0.5)
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

# print(f"Dates: {dates[1:5]}, {dates[-5:-1]}")
# print(f"Open: max: {max(OPEN)} min: {min(OPEN)}")
# print(f"High: max: {max(HIGH)} min: {min(HIGH)}")
# print(f"Low:  max: {max(LOW)} min: {min(LOW)}")
# print(f"Close:max: {max(CLOSE)} min: {min(CLOSE)}")
# print(f"Vol:  max: {max(VOLUME)} min: {min(VOLUME)}")
# print(f"Div:  max: {max(DIV)} min: {min(DIV)}")

n = 100

#print(json.dumps(weekly, indent=4))
plt.plot(DATES[:n], OPEN[:n], label='open_train')
plt.plot(DATES[n:n+n], OPEN[n:n+n], label='open_test')
#plt.scatter(dates[:-100], HIGH[:-100], label='high', marker='_', color='green')
#plt.scatter(dates[:-100], LOW[:-100], label='low', marker='_', color='red')
#plt.plot(dates, CLOSE, label='close')
#plt.bar(dates, VOLUME, label='volume')
#plt.plot(dates, DIV, label='div')

plt.ylabel('open / USD') 
plt.xlabel('Time (unix timestamp) / s') 
plt.title("Linear Regression Example")

# x = dates
# y = open
r, b, a = linear_regression(DATES[:n], OPEN[:n], n)
print(f'y = {b}x + {a}')

y = [(DATES[i]*b) + a for i in range(n)]
plt.plot(DATES[:n], y, label='predicted_train')

y = [(DATES[n+i]*b) + a for i in range(n)]
plt.plot(DATES[n:n+n], y, label='predicted_test')

print(f"Accuracy on training data: {linear_regression_accuracy(b, a, DATES[:n], OPEN[:n], n)}")
print(f"Accuracy on testing data: {linear_regression_accuracy(b, a, DATES[n:n+n], OPEN[n:n+n], n)}")

plt.legend()
plt.show()
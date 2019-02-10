X = list(map(int, input("Enter x values : ").split()))
Y = list(map(int, input("Enter y values : ").split()))
x_ = (sum(X)/len(X))
y_ = (sum(Y)/len(Y))
xy = [(a-x_)*(b-y_) for a,b in zip(X,Y)]
x2 = [(a-x_)**2 for a in X]
y2 = [(b-y_)**2 for b in Y]
r = sum(xy)/(sum(x2)*sum(y2))**0.5
print("Coefficient of correlation (r) : %.4f" % r)

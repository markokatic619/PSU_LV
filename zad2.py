import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
 
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# make polynomial features
poly1 = PolynomialFeatures(degree=2)
poly2 = PolynomialFeatures(degree=6)
poly3 = PolynomialFeatures(degree=15)
xnew1 = poly1.fit_transform(x)
xnew2 = poly2.fit_transform(x)
xnew3 = poly3.fit_transform(x)
    
np.random.seed(12)
indeksi = np.random.permutation(len(xnew1))
indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew1)))]
indeksi_test = indeksi[int(np.floor(0.7*len(xnew1)))+1:len(xnew1)]

xtrain1 = xnew1[indeksi_train,]
xtrain2 = xnew2[indeksi_train,]
xtrain3 = xnew3[indeksi_train,]

ytrain = y_measured[indeksi_train]

xtest1 = xnew1[indeksi_test,]
xtest2 = xnew2[indeksi_test,]
xtest3 = xnew3[indeksi_test,]

ytest = y_measured[indeksi_test]

linearModel1 = lm.LinearRegression()
linearModel2 = lm.LinearRegression()
linearModel3 = lm.LinearRegression()
linearModel1.fit(xtrain1,ytrain)
linearModel2.fit(xtrain2,ytrain)
linearModel3.fit(xtrain3,ytrain)

ytest_p = linearModel1.predict(xtest1)
ytest_p = linearModel2.predict(xtest2)
ytest_p = linearModel3.predict(xtest3)
MSE_test = mean_squared_error(ytest, ytest_p)

plt.figure(1)
plt.plot(xtest1[:,1],ytest_p,'o',label='predicted1')
plt.plot(xtest1[:,1],ytest,'o',label='test1')
plt.plot(xtest2[:,1],ytest_p,'o',label='predicted2')
plt.plot(xtest2[:,1],ytest,'o',label='test2')
plt.plot(xtest3[:,1],ytest_p,'o',label='predicted3')
plt.plot(xtest3[:,1],ytest,'o',label='test3')
plt.legend(loc = 4)
plt.show()

#pozadinska funkcija vs model
plt.figure(2)
plt.plot(x,y_true,label='f')
plt.plot(x, linearModel1.predict(xnew1),label='model1')
plt.plot(x, linearModel2.predict(xnew2),label='model2')
plt.plot(x, linearModel3.predict(xnew3),label='model3')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xtrain1[:,1],ytrain,'o',label='train1')
plt.legend(loc = 4)
plt.show()
import matplotlib.pyplot as plt
import quandl
import numpy as np
import pandas as pd
from numpy.fft import fft, ifft
from numpy import polyfit, polyval, pi, cos, sin
import scipy.optimize as opt


api_key = "xSTwmsveRxyLnz7f3GeV"
tick_symbol = "WIKI/KO"


data = quandl.get("WIKI/KO", start_date="2017-9-23", end_date="2018-01-01", api_key)

mydata = quandl.get("EIA/PET_RWTC_D", returns="numpy")



print(data)
print(data['Close'])

datalist = data['Close'].tolist()
index = np.arange(0,len(datalist),1)

p1 = polyfit(index, datalist, 1)
p2 = polyfit(index, datalist, 2)
p3 = polyfit(index, datalist, 3)
p4 = polyfit(index, datalist, 4)


p1vals = polyval(p1, index)
p2vals = polyval(p2, index)
p3vals = polyval(p3, index)
p4vals = polyval(p4, index)

print(p1vals)

print(p1)

plt.title('Polynomial Fits(Order 1,2) of Stock Price')
plt.xlabel('Days')
plt.ylabel('Scores')

plt.plot(index,datalist)
plt.plot(index,p1vals)
plt.plot(index,p1vals)
plt.plot(index,p3vals)
plt.plot(index,p4vals)

print(p4vals)
plt.show()

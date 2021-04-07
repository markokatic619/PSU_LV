import pandas as pd 
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')
sortedList=mtcars.sort_values(by=['wt'])
sortedA=sortedList[(sortedList.am==1)]
sortedM=sortedList[(sortedList.am==0)]
plt.plot(sortedA.wt,sortedA.mpg,'r-',label='Automatik')
plt.plot(sortedM.wt,sortedM.mpg,'b-',label='Rucni')
plt.xlabel("weight")
plt.ylabel("mpg")
sortedList=mtcars.sort_values(by=['hp'])
sortedA=sortedList[(sortedList.am==1)]
sortedM=sortedList[(sortedList.am==0)]
plt.plot(sortedA.hp,sortedA.qsec,'p-',label='ubrzanje automatika')
plt.plot(sortedM.hp,sortedM.qsec,'o-',label='ubrzanje rucnog')
plt.legend()
plt.show()
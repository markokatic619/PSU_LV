import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
sortedList=mtcars.sort_values(by=['mpg'])
print(sortedList.head(5))#1.
print(sortedList[(mtcars.cyl==8)].tail(3))#2.
mt = mtcars[(mtcars.cyl==6)]
print(mt["mpg"].mean())#3.
mr4 = mtcars[(mtcars.cyl==4)&(mtcars.wt>=2)&(mtcars.wt<=2.2)]
print(mr4["mpg"].mean())#4.
am=mtcars[(mtcars.am==1)]
rm=mtcars[(mtcars.am==0)]
rm.am=1
print(am["am"].sum())#5.
print(rm["am"].sum())#5.
sumam=am[(am.hp>100)].sum()
print(sumam["am"])#6.
mtcars.wt=mtcars.wt*453.592
print(mtcars.wt)#7.
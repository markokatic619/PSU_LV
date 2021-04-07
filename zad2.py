import pandas as pd 
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')
imena=["4 cilindra","6 cilindara","8 cilindara"]
cyl4=mtcars[(mtcars.cyl==4)].mean()
cyl6=mtcars[(mtcars.cyl==6)].mean()
cyl8=mtcars[(mtcars.cyl==8)].mean()
polje=[cyl4.mpg ,cyl6.mpg, cyl8.mpg]
plt.bar(imena,polje)
plt.ylabel("mpg")
plt.show()  #1.

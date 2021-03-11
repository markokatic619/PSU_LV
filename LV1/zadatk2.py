try:
    ocijena=float(input("unesite ocijenu: "))
except:
    print("pogreska!")
    exit()
if ocijena < 0.6: print("F")
if ocijena >= 0.6 and ocijena < 0.7:print("D")
if ocijena >= 0.7 and ocijena <0.8: print ("C")
if ocijena >=0.8 and ocijena<0.9:print("B")
if ocijena >=0.9:print("A")
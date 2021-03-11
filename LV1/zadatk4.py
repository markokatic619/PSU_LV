suma=0
while 1:
    print("upisite neki broj ili Done: ")
    brojevi = input()
    if brojevi == 'Done':
       print(suma)
       exit()
    if brojevi != 'Done':
        try:
            brojevi = int(brojevi)
            suma = suma + brojevi
        except:
            print("pogreska!")
            exit()

        
x = input("Insert a number: ")
y = len(x)
i = 0
add = ''
summ = 0
if y == 4:
     if int(x):
        while i < y:
          print("num" + str(i) + " = " + x[i])
          add = add+x[i]
          summ = summ + int(x[i])
          i = i + 1
        print("add = "+add)
        print("summ = "+str(summ))
else:
   print("Error len!")


##--------------------------------------------------------------------

x = int(input("Insert a number: "))
digit1 = int(int(x)//1000)
print(digit1)

digit2 = int(int(x)%1000//100)
print(digit2)

digit3 = int(int(x)%100//10)
print(digit3)

digit4 = int(int(x)%10)
print(digit4)
        
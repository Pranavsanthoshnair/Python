temp = float(input("Enter Temparature : "))
c_or_f = input("Enter if the temparature is in celsius(C) or fahrenheit(F) : ")
f_to_c = (5/9)*(temp-32)
c_to_f = (9/5)*temp+32

if(c_or_f == "c" or c_or_f == "C"):
    print(temp ,"celsius is ",c_to_f ,"fahrenheit")
elif(c_or_f == "f" or c_or_f == "F"):
    print(temp ,"fahrenheit is ",f_to_c ,"celsius")
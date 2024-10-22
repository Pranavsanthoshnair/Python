temp = float(input("Enter Temparature : "))
scale = input("Enter if the temparature is in celsius(C) or fahrenheit(F) : ")
f_to_c = (5/9)*(temp-32)
c_to_f = (9/5)*temp+32

if(scale == "c" or scale == "C"):
    print(temp ,"celsius is ",c_to_f ,"fahrenheit")
elif(scale == "f" or scale == "F"):
    print(temp ,"fahrenheit is ",f_to_c ,"celsius")

Amount= int(input("Please enter the amount to be widthdrawn"))
n100=Amount//100
n50=(Amount%100)//50
n10=((Amount%100)%50)//10
print("number of notes of 100",n100)
print("number of notes of 50",n50)
print("number of notes of 10",n10)
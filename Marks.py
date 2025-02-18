#take input from user
print("Enter marks obtained in 4 subjects:")
maths= int(input("maths:-"))
science= int(input("science:-"))
english= int(input("english:-"))
sst= int(input("sst:-"))
sum= maths+science+english+sst
perc= (sum/400)*100
print (perc)
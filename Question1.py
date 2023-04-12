#Taking input from user
l = 0 
num = int(input("enter number of year: "))
while (l < num):
  Month = 0
  Rainfall = 0
  total = 0
  #Starting while 
  while (Month < 12):
    print("enter the rainfall for the  month:", Month + 1, "")
    Rainfall = int(input())
    total = total + Rainfall
    Month += 1
    #Ending while 
  l = l + 1
  #Calculating and printing the total and average.
avg = total / 12
print("totally :", total, "")
print("Average monthly rainfall:",avg,"")
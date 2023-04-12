a = []
b = int(input("Enter Number: "))
i = 0
#start while
while(i<b):
  a.append(int(input("Enter Element: ")))
  i=i+1
print(a)

c=[]
i=0
#end while
while (i < b):
  if(a[i] > 5):
    c.append(a[i])
  else:
    pass

  i = i+1
# printing the list
print("List of numbers which are larger than 5:",c,"")
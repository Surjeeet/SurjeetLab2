# user input

a=int(input("Average daily percentage increase:")) 
b=int(input("Starting number of organisms:"))                                  
                      
c=int(input("Enter the number of the days to display the finaly data:")) 


print("Day approximate                     population")
print("--------------------------------------------")
for i in range(1,c):
    b=b+(b*(a/100))                           
    # Printing average
    
    print(b,"\n")                          

# print(x,"\n")
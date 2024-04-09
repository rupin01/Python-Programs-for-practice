#N largest elements
#sorting
#function
def N_max_elements(list, N):
    list.sort()     
    return list[-N: ]

#input
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
n=int(input("Enter N"))
print(n, "max elements in ",li)
  
# Calling and printing the function
print(N_max_elements(li, n))
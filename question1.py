#  sum of 1 to n (using recursion) 

# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return (n+sum(n-1))  
# n=int(input("enter any numbers:-")) 
# z=sum(n)
# print(z)  
       
# print string in reverse order using recursion

# def xyz(s,n):
#     if n==0:
#         print(s[0])
#     else:
#         print(s[n],end="") 
#         xyz(s,n-1)
# s=input("enter string:-")
# xyz(s,len(s)-1) 
       
# programe to find xy using recursion

# def findpower(x,y):
#     if y==0:
#         return 1
#     else:
#         return(x*findpower(x,y-1))
# x=int(input("enter any number:-"))  
# y=int(input("enter exponent:-"))   
# z=findpower(x,y)
# print("calculated value=",z)       


# finding factorial using recursion

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return (n*fact(n-1))  
# n=int(input("enter no to find factorial:-"))
# z=fact(n) 
# print("factorial=",z) 
        
# calculate gcd using recursion

# def gcd(p,q):
#     if q==0:
#         return p
#     else:
#         return (gcd(q,p%q))  
# p=int(input("enter any number:-"))  
# q=int(input("enter any number:-")) 
# z=gcd(p,q) 
# print("gcd=",z)     
 
# Fibonacci Series Using Recursion 

# def fibo(n):
#     if n==1:
#         return 0
#     if n== 2:
#         return 1
#     return (fibo(n-1)+fibo(n-2))
# n=int(input("enter any number:-")) 
# for i in range(1,n+1):
#     print(fibo(i))

# Binary Search using recursion

# def Binary_Search(a,size,key):
#     flag=0
#     i=0
#     j=size-1
#     while i<=j and flag==0:
#         mid=(i+j)//2
#         if a[mid]==key:
#             flag=1
#             pos=mid+1
#         if a[mid]<key:
#             i=mid+1
#         if a[mid]>key:
#            j=mid-1
#     if flag==1:
#         print("number found at",pos,"position")  
#     else:
#         print("number not found")
# a=[]
# size=int(input("enter size of the list:-"))
# for i in range(size):
#     va1=int(input("enter value for the list in asending order:-"))
#     a.append(va1)
# key=int(input("enter number to search:-")) 
# Binary_Search(a,size,key)





# def recursivebinary(a,key,low,high):
#     if low>high:
#         return -999
#     mid=int((low+high)/2) 
#     if a[mid]==key:
#         return mid
#     if a[mid]>key:
#         recursivebinary(a,key,low,mid-1)
#     if a[mid]<key:
#         recursivebinary(a,key,mid+1,high) 
# a=[3,5,8,10,15,18,20,25,27,30]  
# key=int(input("enter number to search:-"))   
# x=recursivebinary(a,key,0,9)
# if x== -999:
#     print("not faund")   
# else:
#     print("no found at",x,"position")             


        
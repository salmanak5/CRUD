# # # for i in range(1,101):
# # #     print(i)
    
# # j=['salman','salman'] 
# # for item in range(501):
    
# #     print(int(j))
# # else:
# #     print("hogya khtm")
        
    
# # i=input("enter number")
# # sum=0
# # while i>0:
# #     sum=sum+i%10
# #     i=i//10 
# #     print(sum)    

# i=1
# while i<=5:
#     j=1

#     while j<=i:
#         print("*",end=' ')
#         j+=1
#     print()
#     i+=1      


# for i in range(1,4):
#     for j in range(1,3):
#         print(j)


# for i in range(6,1,1):
#     for j in range(6,i+1):
#         print("*",end="")
#     print("")    



n=int(input("enter number"))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1):
            print("*",end='')
print()     





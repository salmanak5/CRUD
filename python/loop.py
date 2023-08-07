
# #list in the loop
# # # # thislist=["salman","akbar","akhund"]
# # # # i = 0
# # # # while i < 3:
# # # #   print(thislist[i],end=' ')
# # # #   i += 1
# # # # #print(type(str(100)))

# #list in loop 

# # # thislist=["apple","bannna","grapes","falari"]
# # # i=3
# # # while i>=0:
# # #   print(thislist[i],end=" ")
  
# # #   if thislist[i]=='grapes':
# # #     print("you eat mango")
# # #   else:
# # #     print(" ")
# # #   i -= 1

# #formated string  
# # # name='salman'
# # # age=55
# # # print(f'hi my name is {name} and {age} years old ') 


# #formatedstring
# # name= 'falaro'
# # age=101
# # print(f'the name is {name} and the {age} years old')
# # print(f'the name is {name} and the {age} years old')
# # print('the name is {1} and the {0}years old'.format(name,age))
# # print('hi the name is {0}. and the {1} years old'.format(name,age))
# # print('hey this is {newname}. and the kuch is {age}etro'.format(newname='salman',age=99))



# # while True:
# #     a= input("say something:").lower()
# #     if a=="hello":
# #         break
    
# i=["salman"]
# for item in i:
#     print(item) 
#     continue
picture = [
    [1, 2, 3, 4, 5],
    [0, 0, 6, 0, 0],
    [0, 0, 7, 0, 0],
    [0, 0, 8, 0, 0],
    [0, 0, 9, 0, 0]
]
for row in picture:
    for pixel in row:
        if pixel==1:
        
            print("*",end=(" "))
            
        if pixel==2:
        
            print("*",end=(" "))
            
        if pixel==3:
        
            print("*",end=(" "))
            
        if pixel==4:
        
            print("*",end=(" "))
            
        if pixel==5:
        
            print("*",end=(" "))
           
        if pixel==6:
        
            print("    *",end=(" "))
            
        if pixel==7:
        
            print("    *",end=(" "))
            
        if pixel==8:
        
            print("    *",end=(" "))
            
           
        if pixel==9:
        
            print("    *",end=(" "))
        
        else:
            print(" ",end=(" "))
    print("")
        
        
        
    
        
    
    
    
   
    
a=input('python or java').lower()
if a == 'python':
    b=input('what is python').lower()
    if b=='highlevel':
        print("correct")
    else:
        print("wrong")
        c=input('what is function in python').lower()
        if c== 'function':
            print('correct')
        else:
            print("wrong")
            d=input('who invented python') .lower()
            if d=='me':
                print("correct")  
            else:
                print("wrong")
elif a=='java':
    b=input('what is java').lower()
    if b=='highlevel':
        print("correct")
    else:
        print("wrong")
        c=input('what is function in java').lower()
        if c== 'function':
            print('correct')
        else:
            print("wrong")
            d=input('who invented java').lower()
            if d=='me':
                print("correct")  
            else:
                print("wrong")
    
     
else:
    print("choose correct one")
def fruitlist():
    fruitlists=["apple","mango","cherry","langro amb"]
    i=0
    while i<4:
        print(fruitlists[i])
        i +=1
    a=input('write fruit name if it is in this yo can avail : ')#you can use .lower()function here 
    
    if a.lower() in fruitlists:
        print("congratulations you can avail")
    else:
        print("sorry for inconvience")
    
    return fruitlist()
fruitlist()
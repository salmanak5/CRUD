class form:
 def __init__(self,name,fname,phone,age,email):
   self.name=name
   self.fname=fname
   self.phone=phone
   self.age=age
   self.email=email


name=input("write name")
fname=input("write fname")
phone=input("write phone")
age=input("write AGE")
email=input("write email")

a=form(name,fname,phone,age,email)
if a=="name,fname,phone,age,email":
   print("submitted")
elif a=="name,fname,phone,age,email":
    print("submited")
elif a=="name,fname,phone,age,email":
    print("submited") 
elif a=="name,fname,phone,age,email":
    print("submited")
else:
    print("ok")   
    

# while a==a :
#     print("submitted")
#     a+=1


   
print(f"name:{a.name}\nfathername:{a.fname}\nphone number: {a.phone} \nage :{a.age}\nemail: {a.email}")
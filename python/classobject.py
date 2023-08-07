import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b


























# class person:
#     def __init__(self,name,occupation,salary):
#         self.name=name
#         self.occupation= occupation
#         self.salary= salary
        
#     def info(self):
#         print(f"{self.name } is a {self.occupation} and his salary {self.salary}")
# a=person("salman","wandho","10")
# b=person("akbar","engineer","10000000000")  
# a.info()
# b.info()



















# # class person:
# #     def __init__(self,name,occupation,salary):
# #         print("hey iam a person")
# #         self.name=name
# #         self.occupation=occupation
# #         self.salary=salary
# #     def info(self):
# #         print(f"{self.name} is a {self.occupation} his salary is {self.salary}")
# # a=person
# # a=person("salman","wandho","1000")
# # b=person("faraz","developer","25000")
# # a.info()
# # b.info()
        
























# # # class maiin:
# # #     name="salaman" 
# # #     occupation="wandho"
# # #     salary=10000
    
# # #     def info(self):
# # #         print(f"{self.name} is a {self.occupation} his salary is {self.salary}")
    
# # # a=maiin()
# # # a.info()
    
    
# # # # akbar=maiin()
# # # # akbar.name="akbar"
# # # # akbar.occupation="electrical engineer"
# # # # akbar.salary=700000
# # # # # print(f"name: {akbar.name}\n occupation: {akbar.occupation}\n salary: {akbar.salary}")
# # # # akbar.info()  
    
    
    
# # #     # class kuch:
# # # #     name="salman"
# # # #     occupation="wandho"
# # # #     salary="bikamanga"
# # # #     print(f"name :{name}\noccupation :{occupation}\nsalaray :{salary}")
    
# # # #a=kuch()
# # # #a.name="faraz"
# # # #a.occupation="developer"
# # # #a.salary="zyda"
# # #     #print()
        
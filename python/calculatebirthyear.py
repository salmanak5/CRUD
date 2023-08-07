# birth_year=input(" what year is your birth")
# age=2023-int(birth_year)
# print(age)
def age_calculator():#userdefined function
    birth_year = input("What year were you born? ")
    birth_month = input("What is your birth month? ")
    birth_date = input("What is your birth date? ")

    age = 2023 - int(birth_year)
    print("Your birth date is: " + birth_month + " " + birth_date)
    print("Your age is:", age)

    return age_calculator()

age_calculator()
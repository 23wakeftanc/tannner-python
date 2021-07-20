age=input("What grade are you?: ")
age=int(age)
if age<=4:
    print("Too young for school")
elif age>=5 and age<=6:
    print("Go to Kindergarten")
elif age>=7 and age<=18:
    print("Go to Grade", age-5)
elif age>=19:
    print("Go to college")

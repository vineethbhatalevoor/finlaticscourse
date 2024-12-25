# ------------------------------------
# If statement
# #uses indentation to define code block
#
# Example
# if condition:
#   #code block starts here
#    statement1
#   #code block ends here
# -----------------------------------
# Example
age=int(input("Enter age:"))
if age>=18:
   print("You are eligible to vote.")
#-------------------------------------------
#If else Statement
#Give output based on condition
#Example
#if condition:
#    #code block starts here for the true condition
#   Statement_1
#else:
#   #code block starts here for the false statement
#   Statement_2
#---------------------------------------------
#Lets understand with an example
age=int(input("enter age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("Not eligible to vote.")
#----------------------------------------------   
#If-elif-else
#used for multiple conditions
#Example
#if condition_1:
#   #code block for condition_1 being true
#    Statement_1
#elif condition_2:
#    #code block for condition_2 being true
#    Statement_2
#else:
#   #code block when no condition are true
#    Statement_3
#------------------------------------------------
#lets evaluate student performance based on their marks
marks=int(input("Enter marks:"))
if marks>=90:
   print("Excellent")
elif marks>=70:
   print("Good job!")
else:
    print("Keep up the good and hard work!")
#-------------------------------------------------
#Nested if statements
#complex decision making structures
#Example
#if condition_1:
#   if condition_2:
#       #code block when both condition_1 and condition_2 are true
#       statement_1
#   else:
#       #code block when contion_1 is true,but condition_2 is false
#       statement_2
#else:
#   #code block when condition_1 is false
#   statement_3
#--------------------------------------------------
#Check students age and their grade to give feedback ontheir achievement.
age=18
grade="A"
if age>=18:
   if grade=="A":
        print("Congratulations on your achievement!")
   else:
        print("You need to keep striving for excellence!")
else:
    print("You need to be atleast 18 years old to qualify")
#------------------------------------------------------------
#Lets see another example
#gets the input from the user
age=int(input("Enter your age:"))
#Check age conditions using nested if statements
if age>=16:
    print("You are eligible to apply for learner's permit to drive.")
#    #Nested if statement for additional condition
    if age>=18:
        print("You are eligible for a full driver's license.")
    else:
        print("You can drive with a provisional license under supervision")
else:
    print("Sorry,you must be atleast 16 years old to apply for a learner's permit.")
#--------------------------------------------------------------------------------------------------
#dictionary are versatile data structures that store key-value pairs 
'''dictionaries can be compared for equality. Two dictionaries are considered equal if they have the same set of keys and the corresponding values for each key are equal'''
dict1={'a':1,'b':2,'c':3}
dict2={'a':1,'b':2,'c':3}
if dict1==dict2:
    print("Dictionaries are equal.")
else:
   print("Dictionaries are not equal")
#----------------------------------------------------------------------------------------------------
#Comparing tuples
tuple1=(1,2,3)
tuple2=(1,2,3)
if tuple1==tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")
#----------------------------------------------------------------------------------------------------
#Now lets modify the above code and change the value of tuple 2
tuple1=(1,2,3)
tuple2=(3,2,1)
if tuple1==tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")
#------------------------------------------------------------------------------------------------------
#Sets in python are unordered collection 
#when comparing sets the order of elements is not a factor

set1={1,2,3}
set2={1,2,3}
#comparing sets
if set1==set2:
    print("Sets are equal.")
else:
    print("Sets are not equal.")
#It see contents of set and not the order of element 
#For list,tuple and strings elements are required in the same order.
#for dictionaries and sets they see the number of elements.
#----------------------------------------------------------------------------------------------------
#Lets see the Logical Operator(and,or,not) to combine multiple conditions.
#Example
age=25
is_student=False
if age>18 and not is_student:
    print("Eligible for voting")
#--------------------------------------------------------------------------------------------------------
age=25
is_student=False
has_job=True
if age>18 and not is_student or has_job:
    print("Eligible for some opportunities")
#--------------------------------------------------------------------------------------------------------
day=input("Enter a day of the week:")
if day=="saturday" or day=="sunday":
    print("It's the weekend.")
else:
    print("Not a weekend.")
#--------------------------------------------------------------------------------------------------------
#ternary operator in python.
#it has if-else statements into a single line
#syntax
#result_if_true if condition else result_if_false
#Lets see an example
age=20
Eligible_Status="Eligible" if age>=18 else "Not eligible"
print(Eligible_Status)
#-------------------------------------------------------------------------------------------------------
Score=75
result="Pass" if Score>=50 else ("Retake" if Score>=40 else "Fail")
print(result)
#------------------------------------------------------------------------------------------------------
'''Created a simple Python script that engages with the user to plan an exciting weekend.Now , Let's dive into the details of this code 
and explore how it engages with user input to create a personalized and interactive experience.'''

name=input("Enter your name: ")
print("Hello, " + name +"! Let's plan a exciting weekend activity.")
print("You have a free weekend ahead.How would you like to spend it?")
print("1: Go for a hike in the mountains")
print("2: Attend a music concert in the city")
print("3: Have a relaxing day at the beach")

choice=input("Enter the number corresponding to your prefered activity (1,2, or 3): ")
if choice=="1":
    print("What difficulty level of hike do you prefer?")
    print("a: easy")
    print("b: moderate")
    print("c: challenging")
    difficulty_level = input("Enter the number corresponding to your difficulty level (a,b, or c) ")
    if difficulty_level=="a":
        print("You enjoyed  a scenic hike with breathtaking views.")
    elif difficulty_level=="b":
        print("The moderate hike provided a good balance of challenge and enjoyment.")
    elif difficulty_level=="c":
        print("You conquered a challenging hike and felt a great sense of accomplishment.")
    else:
        print("Invalid difficulty Level choice.")
elif choice=="2":
        genre=input("You spent a relaxing day at the beach,enjoying the sun,sand,and waves.")
        print(f"You attended a {genre} concert and had a fantastic time.")
elif choice=="3":
        print("You spent a relaxing day at the beach,enjoying the sun,sand, and waves.")
else:
        print("Not a valid choice.Please enter either '1','2', or '3' based on your preffered activity.")
print("Thank you for planning your weekend with us,"+name+"!")
#----------------------------------------------------------------------------------------------------------------------
#Truthy or Falsy values in python 
#Truthy is logically true and a False is logically false.
#Lets see an example
a=0
if a:
    print(a)
    
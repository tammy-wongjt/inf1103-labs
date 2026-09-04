# Activity 1
# print("==============================")
# print("Welcome here")
# print("My first post!")
# print("==============================")

# Activity 2
# username = "cool_creater"
# bio = "Fun Blogger"
# followers = 100

# print("Username: ", username)
# print("Bio: ", bio)
# print("followers: ", followers)

# # Activity 3
# followers = 100

# followers += 50
# print("Day 1: ", followers)

# followers += 20
# print("Day 2: ", followers)

# followers -= 10
# print("Day 3: ", followers)

# Activity 4: Interactive profile creator
# username = input("Enter Username: ")
# age = input("Enter Age: ")
# category = input("Enter Content Category:")

# print("\nInstagram Profile")
# print("==============================")
# print("Username: ", username)
# print("Age: ", age)
# print("Category: ", category)

# Activity 5
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile") #\n is called an escape sequence - it creates a new line in the output.
print("==============================")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)

if age>40 and category == "fun":
    print ("You are old what is fun for you?")
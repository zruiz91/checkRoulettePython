# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


num_of_people = len(names)

random_choice = random.randint(0, num_of_people - 1)

chosen_person = names[random_choice]


print(chosen_person + " is going to buy the meal today!")
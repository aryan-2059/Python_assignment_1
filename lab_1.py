#Name: Aryan Solanki
#BTech AI/ML - A
#2501730347
#Date: 28 october 2025
# calorie tracker
import datetime
print('''***** WELCOME TO CALORIE TRACKER *****
      You can track your daily calorie intake here.''')
n = int(input("Enter number of meals:\t"))
total_calories = 0
avg_cal=0 
meals=[] 
calories=[] 

for i in range(n):
    m=input("Enter meal name:\t") 
    c=float(input(f"Enter calories for {m}:\t")) 
    meals.append(m) 
    calories.append(c) 

lim = float(input("Enter your daily calorie limit:\t"))
total_calories= sum(calories)
avg_cal= total_calories / n 

print("\n***** DAILY CALORIE INTAKE SUMMARY *****")
print("\t\tMeal Name\tCalories")
print("\t\t-------------------------")
for i in range(n):
    print(f"\t\t{meals[i]}\t{calories[i]}")
print(f"\t\tTotal:\t{total_calories}")
print(f"\t\tAverage per meal:\t{avg_cal}")
print("\t\t-------------------------")

if avg_cal > lim:
    print('''***WARNING***
          YOU HAVE EXCEEDED YOUR DAILY CALORIE LIMIT!!!''')
else: 
    print("You are within your daily calorie limit :)")
print(total_calories)

wish = input("Do you want to save this summary to a file? (yes/no):\t").lower()
if wish == 'yes':
    filename = 'data.txt'
    timestamp= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, 'a') as file:
        file.write(f"\n***** DAILY CALORIE INTAKE SUMMARY ({timestamp}) *****\n")
        file.write("\t\tMeal Name\tCalories\n")
        file.write("\t\t-------------------------\n")
        for i in range(n):
            file.write(f"\t\t{meals[i]}\t{calories[i]}\n")
        file.write(f"\t\tTotal:\t{total_calories}\n")
        file.write(f"\t\tAverage per meal:\t{avg_cal}\n")
        file.write("\t\t-------------------------\n")
        if total_calories > lim:
            file.write('''***WARNING***
          YOU HAVE EXCEEDED YOUR DAILY CALORIE LIMIT!!!\n''')
        else:
            file.write("You are within your daily calorie limit :)\n")
    print(f"Summary saved to {filename}")
else:
    print("Summary not saved.")

# calorie tracker
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

if total_calories > lim:
    print('''***WARNING***
          YOU HAVE EXCEEDED YOUR DAILY CALORIE LIMIT!!!''')
else: 
    print("You are within your daily calorie limit :)")
print(total_calories)

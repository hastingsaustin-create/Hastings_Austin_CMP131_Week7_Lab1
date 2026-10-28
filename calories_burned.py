#Austin Hastings
#CMP 131 86520
#Week 7
#Lab 1
#Calories Burned
#27 OCT 2026
print("Calories Burned")
print("-------------")

calories_per_minute = 3.6

for minutes in range(5, 31, 5):
    calories_burned = minutes * calories_per_minute
    print(minutes, "minutes =", calories_burned, "calories")
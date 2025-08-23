import random

# Number of rolls
rolls = 20

count_6 = 0
count_1 = 0
count_two_6s = 0
prev_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and prev_roll == 6:
        count_two_6s += 1
        
    prev_roll = roll

print("\nStatistics:")
print(f"Total 6s rolled: {count_6}")
print(f"Total 1s rolled: {count_1}")
print(f"Two 6s in a row: {count_two_6s}")

# Task 4: Average Temperature
temps = []

for i in range(1, 6):
    temp = float(input(f"Enter temperature for Day {i}: "))
    temps.append(temp)

average = sum(temps) / len(temps)
print(f"\nAverage Temperature over 5 days: {average:.2f}°C")

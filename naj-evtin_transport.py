kilo = int(input("Enter how muany kilometers you go: "))
period = input("Enter night or day: ")
sum = 0
if kilo < 20:
    if period == "day":
        sum = 0.70 + kilo * 0.79
    if period == "night":
        sum = 0.70 + kilo * 0.90
if kilo > 20:
    sum = kilo * 0.09
if kilo > 100:
    sum = kilo * 0.06
print(f"The sum is {sum}")
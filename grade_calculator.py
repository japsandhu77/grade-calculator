mark1 = float(input("Enter the first mark: "))
mark2 = float(input("Enter the second mark: "))
if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100):
    raise SystemExit("Both marks must be between 0 and 100.")

average = (mark1 + mark2) / 2
print(f"Average: {average:.1f}%")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Letter grade: {grade}")

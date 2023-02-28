# Write your solution here
import math
course = int(input("How many students on the course?"))
group = int(input("Desired group size?"))

number = math.ceil(course / group)

print(f"Number of groups formed: {number}")
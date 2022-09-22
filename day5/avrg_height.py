#!/usr/bin/python
total_height = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# The aim is to calculate the average height of the list without using len() and sum()

#Write your code below this row 
	r = n
	
	total_height += student_heights[n]
average_height = total_height/(r +1)
print(f"The average height of these {r + 1} people is {average_height}")

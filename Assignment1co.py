#Male and Female Percentages
#Write a program that asks the user for the number of males and the number of females registered in a class. 
#The program should display the percentage of males and females in the class.
#Expected Output 
#The total number of students: 		100
#The number of males	and females 		40 		60
#The percentage of males and females	40.00%		60.00%
#Run your program multiple times with different input values

number_of_males = int(input('Enter number of males:  '))
number_of_females = int (input('Enter number of females:  '))

total_number_of_students = number_of_males + number_of_females
percentage_of_males = number_of_males / total_number_of_students
percentage_of_females = number_of_females / total_number_of_students

print ("total number of students =", (total_number_of_students))
print ("percentage of males =", format(percentage_of_males, '.0%'))
print ("percentage of females =", format(percentage_of_females, '.0%'))

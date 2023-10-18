#Create a variable called 'number' and assign it the three-digit number.
number = 789
#Find the 'number' first digit and assign to x1.
n1 = number%10 #9
#Find the 'number' second digit and assign to x2.
n2 = number//10%10 #8
#Find the 'number' third digit and assign to x3.
n3 = number//100 #7
#Create a variable called 'answer' and assign it the sum of the three digits x1, x2, x3.
print(n1 + n2+ n3)
#Print the value of the 'answer.
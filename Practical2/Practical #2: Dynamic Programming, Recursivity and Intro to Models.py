import time

f = open("Quetion_answer.txt", "w+")
f.write("1. Dynamic Programming, Recursivity: Rabbits and Recurrence Relations\n\nQ1:\nThe initial elements are a pair of newborn baby rabbits at month 1. The recurrence relation of the Fibonacci sequence Fn is :\nFn = Fn-1 + Fn-2 \nI have heard about Fibonacci recurrence relation before in the exact same example. Last year our computer science teacher showed us this example in the Rosalind exercises list. \n\nQ2:\nCan be found in the Python script. The execution time of my 2 functions is different. It seems that iterative function is always faster. I think it is because the recursive function calls itself each time it needs to execute, so it takes more time. \n\nQ3:\nCan be found in the Python script. \n\nQ4:\nCan rabbits become extinct in this model?\nRabbits can not become extinct in this model because there is no mortality factor, the only option for the rabbits is to create new rabbits. To allow the rabbits population to reach extinction, we need to add a mortality factor, an option that will be able to diminuish the number of rabbit as it grows. It can be death from natural factors like old age, or it can be by introducing a predator to your rabbit population. To implement such changes, we need to add new conditions.\n\n\n2. Mortal Fibonacci Rabbits\n\nQ1:\nAfter 6 months, if the rabbits lifespan is 3 months, the rabbits population is of 4 rabbits. I discovered this by drawing a graph.\nQ2:\nThe execution time of my 2 functions is different. It seems that iterative function is always faster. I think it is because the recursive function calls itself each time it needs to execute, so it takes more time.\nQ3: Rabbit extinction, Rabbit apocalypse:\nRabbits can not grow extinct in this model, indeed, even while running the model with 2 months of lifespan, the rabbits population still grows. Howhever, compared to the previous model, it still grows much slower. To make a rabbit population complitely disapear, we would need to add predators factor, or another factor that would kill rabbits faster that they would reproduce. We could add a function that would randomly remove rabbits from the population and see how the population evolve.\nIn the opposit situation, rabbits can reproduce so much that they would take over the world. Counsidering the average lifespan of a rabbit in the wild is 2 years (so m = 24), after only 10 years (n = 120) we obtain 5356099397629197464730564 rabbits pair.\n\n\n3. Tumour cell growth\n\nQ1:\nIn the code\n\nQ2:\nI run the program bellow for multiples r values from 1.5 to 3.9, with set Nt = 0.005 and n = 50. We can observe that for low r values we have a logistic growth. For r = 1.5, there is a quick growth in the first months, with small oscillations around 5 months, than the population stagnateafter less than 10 months.\nReaching r = 2.5, we observe a quick growth, than oscillation (a lot more than for r = 1.5). We could hypothesise that there is a bifurcation due to a change of stability of the fixed points in the sequence. At r = 3, the population growth is chaotic. For the heigher the r value (3.5 and 3.9), the population will stagnates to 0 and collapses after 12 months. We can hypothesise that 0 has become the only attractive positive fixed point.\n\nQ3:\nWe can estimate the parameters of the initial equation by looking at the graph produced. n is given by the x axis. Nt can be identified by looking at the origin ordinate of the graph. r by looking at the tangente of the curve at n = 0.\n\n\n4. Dynamic Programming: Point Mutations\n\nIn the code...")
f.close()

n = 5		  # n is the number of months.

print("\nExercise 1:\n")
def Ex1_Q2_Iterative_Function(n):
    # 0 correspond to the number of rabbits pair at month 0, 1 coreespond to the number of rabbits pair at month 1, which correspond to 1 pair of non sexualy mature rabbits.
    List_of_rabbits = [0, 1]

    # This is my first condition 
    if n <= 1:  
       	return n  

    for i in range(n):	
        # This is my second condition to make sure the function stops after reaching n months
        if i == n-1:			# I use n - 1 operation because in Python the range of a number n itterates from 0 to n-1. So i will never reach n
            break

        else:
        	Fn = List_of_rabbits[-1] + List_of_rabbits[-2]      # Fibonacci sequence, itterates the month.
        	List_of_rabbits.append(Fn)         # I itterate my list of rabbits number
    return Fn

def Ex1_Q2_Recursive_Function(n):  
   if n <= 1:  
       return n  
   else:  
       return(Ex1_Q2_Recursive_Function(n-1) + Ex1_Q2_Recursive_Function(n-2))


print("Result of iterative function after", n, "months : ", Ex1_Q2_Iterative_Function(n))
print("Result of recursive function after", n, "months : ", Ex1_Q2_Recursive_Function(n))

# The lines bellow allow me to compare the execution time of the 2 functions
start_time = time.clock()
Ex1_Q2_Iterative_Function(n)
time1 = time.clock() - start_time
print ("\nThe iterative Function takes :", time1, "seconds to run.")

start_time = time.clock()
Ex1_Q2_Recursive_Function(n)
time2 = time.clock() - start_time
print ("The recursive Function takes :", time2, "seconds to run.")

if time2 < time1 :
	print("The recursive function takes", time2/time1, " less time to run than the iterative function")
else:
	print("The iterative function takes", time1/time2, " less time to run than the recursive function")


k = 3

def Ex1_Q3 (n, k):
   if n <= 1:  
       return n  
   else:  
       return Ex1_Q3(n-1,k) + k * Ex1_Q3(n-2,k)

print("\nProduction of a litter of ", k, " rabbit pairs with recursive function after", n, "months : ",Ex1_Q3(n, k))


print("\nExercise 2:")

m = 3 		# Number of month afterward a rabbit dies
def Ex2_Q2_Iterative_Function(n, m):
    # I create a list containing m number which each correspond to the number of rabbits at each stages of its life.
    List_of_rabbits = [1] + [0]*(m-1)

    for i in range(n-1):
    	List_of_rabbits = [sum(List_of_rabbits[1:])] + List_of_rabbits[:-1]		# I itterate my list
    return sum(List_of_rabbits)		# The sum gives us the total number of rabbits at each time

def Ex2_Q2_Recursive_Function(n, m):
	if n > 2:
		return(Ex2_Q2_Recursive_Function(n-1, m) + Ex2_Q2_Recursive_Function(n-2, m) - Ex2_Q2_Recursive_Function(n-m-1,m))
	if n < 0 :
		return 0
	else :
		return 1    

print("\nResult of iterative function after ", n, "months and with a ", m, "months lifespan : ", Ex2_Q2_Iterative_Function(120,24))
print("Result of recursive function after ", n, "months and with a ", m, "months lifespan : ", Ex2_Q2_Recursive_Function(6,3))

# The lines bellow allow me to compare the execution time of the 2 functions
start_time = time.clock()
Ex2_Q2_Iterative_Function(n,m)
time1 = time.clock() - start_time
print ("\nThe iterative Function takes :", time1, "seconds to run.")

start_time = time.clock()
Ex2_Q2_Recursive_Function(n,m)
time2 = time.clock() - start_time
print ("The recursive Function takes :", time2, "seconds to run.")

if time2 < time1 :
	print("The recursive function takes", time2/time1, " less time to run than the iterative function")
else:
	print("The iterative function takes", time1/time2, " less time to run than the recursive function")




print("\nExercise 3:\n")

import matplotlib.pyplot as plt
from numpy import random as random

K = 1		# Number of cancer cells per petri dish
r = 1.5		# Cells' growth rate
n = 0		# number of itterations
Nt = 0.05	# fraction of the total population of cancer cells that can be sustained in the cell culture container

list_n = []		# list of n containing its historic
list_Nt = []	# list of Nt containing its historic
steps = 50

def Ex3_Q1 (Nt, r, n):
	for i in range(steps):
		Nt += r * Nt * (1 - (Nt/K))		# Incrementing the value of Nt, according to the logistic growth followed by the cells
		n += 1							# Incrementing the value of n
		list_Nt.append(Nt)				# Appending the list to increment with the values of Nt at each new iteration
		list_n.append(n)				# same but with n

	# Plotting the lists
	plt.plot(list_n, list_Nt, label = "Cell population")
	plt.legend()
	plt.xlabel("Number of itterations")
	plt.ylabel("Number of Cells")
	plt.title("Evolution of cell population")
	plt.show()
	return

Ex3_Q1(Nt, r, n)


print("\nExercise 4:\n")

def Counting_point_mutations(s, t):
    result = 0      # Number of mutations
    tbis = list(t)
    sbis = list(s)
    for i in sbis:	
    	if i in tbis:
    		tbis.remove(i)
    		sbis.remove(i)
    for i in sbis:	
    	if i not in tbis:
    		result +=1

    return(result)

s = "PLEASANTLY"
t = "MEANLY"

print ("The edit distance between", s, "and ", t, "is :", Counting_point_mutations(s, t), "\n")

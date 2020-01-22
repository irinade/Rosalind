f = open("Quetion_answer.txt", "w+")
f.write("1. Dynamic Programming, Recursivity: Rabbits and Recurrence Relations\n\nQ1:\nThe initial elements are a pair of newborn baby rabbits at month 1. The recurrence relation of the Fibonacci sequence Fn is :\nFn = Fn-1 + Fn-2 \nI have heard about Fibonacci recurrence relation before in the exact same example. Last year our computer science teacher showed us this example in the Rosalind exercises list. \n\nQ2:\nCan be found in the Python script.")
f.close()

n = 11		  # n is the number of months.

def Q2_Iterative_Function(n):
    List_of_rabbits = [0, 1]
    # 0 correspond to the number of rabbits pair at month 0, 1 coreespond to the number of rabbits pair at month 1, which correspond to 1 pair of non sexualy mature rabbits.
    for i in range(n):		
        # This is my first condition to make sure the function stops after reaching n months
        if i == n-1:			# I use n - 1 operation because in Python the range of a number n itterates from 0 to n-1. So i will never reach n
            break

        # This is my second condition to itterates the first months
        elif n <= 1:  
       		return n  

        elif i > 1 and i < n:
	        Fn = List_of_rabbits[-1] + List_of_rabbits[-2]      # Fibonacci sequence, itterates the month.
	        List_of_rabbits.append(Fn)         # I itterate my list of rabbits number
	        return Fn

def Q2_Recursive_Function(n):  
   if n <= 1:  
       return n  
   else:  
       return(Q2_Recursive_Function(n-1) + Q2_Recursive_Function(n-2))


print(Q2_Iterative_Function(n))
print(Q2_Recursive_Function(n))


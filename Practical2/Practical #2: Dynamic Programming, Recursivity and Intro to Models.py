f = open("Quetion_answer.txt", "w+")
f.write("1. Dynamic Programming, Recursivity: Rabbits and Recurrence Relations\nQ1:\nThe initial elements are a pair of newborn baby rabbits at month 1. The recurrence relation of the Fibonacci sequence Fn is :\nFn = Fn-1 + Fn-2 \nI have heard about Fibonacci recurrence relation before in the exact same example. Last year our computer science teacher showed us this example in the Rosalind exercises list. \nQ2:\nCan be found in the Python script.")
f.close()


def Q2_Iterative_Function(n):
    # n is the number of months.
    List_of_rabbits = [0, 1]
    # 0 correspond to the number of rabbits pair at month 0, 1 coreespond to the number of rabbits pair at month 1, which correspond to 1 pair of non sexualy mature rabbits.
    for i in range(n - 1):      # I use n -  operation because in Python the range of a number n itterates from 0 to n-1.
        if i == n - 1:
            break
        Fn = List_of_rabbits[-1] + List_of_rabbits[-2]      # Fibonacci sequence, itterates the month.
        List_of_rabbits.append(Fn)         # I itterate my list of rabbits number

    return Fn


n = 4
print(Q2_Iterative_Function(n))

from random import randrange 

# Exercice 1

def lottery():
    """
    This programme generate randomly 6 numbers for a lottery ticket.
    Each number should be between 1 and 49.
    There shouldn't be a duplicate number among those 6.
    Display them in ascending order
    """
    # Generate a list of 6 numbers between 1 and 49 included
    # we use the famous randrange function of the random library
    # randrange(1,50) return a random number between 1 and 49 

    generated_numbers=[]
    i=0
    while i <6:
        res=randrange(1,50)
        # check if there is no duplicate in the curent list
        if res not in generated_numbers:
            i=i+1
            #once the generated number is not a duplicate we add it to the list
            generated_numbers.append(res)
        
    # sorting the list in ascending order
    # we will be using the python function sort
    generated_numbers.sort()
    return generated_numbers

def main():
    print("The generated lottery ticket:")
    print(lottery())

main()

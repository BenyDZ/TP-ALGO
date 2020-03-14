def isPrime(number):
    """
    Function that verify if a number is a prime number
    """
    counter = 2
    test = True
    #test if the number is egal to 0 or 1
    if number == 0 or number == 1:
        #change the value of test from true to false
        test = False
    #test if the number is even
    if number % 2 == 0:
        halfNumber = number//2
    else:
        halfNumber = (number//2) + 1
    #browse all numbers from 2 to halfNumber
    for counter in range(2,halfNumber+1):
        if number % counter == 0 :
            test = False
    
    return test

def sumTableElt(table = []):
    """
        Function to sum all numbers of a table, take a table return the sums
    """
    sums = 0
    #condition to browse all elements of a table
    for counter in range (len(table)):
        sums = sums + table[counter]
    
    return sums

def average(sums, table = []):
    """
        Function to calculate av5erage, return the average
    """
    aver = sums/len(table)
    
    return round(aver,1)

def sumOfDividers(number):
    """
    Function that sum the dividers of a number
    """
    sumDividers = 0
    for counter in range (1,number):
        if number % counter == 0:
            sumDividers = sumDividers + counter
    
    return sumDividers

def tri_Bulles(tab = []):
    #get size of the table
    tableSize = len(tab)
    #verify if tableSize is more than 1
    if tableSize >= 2:
        # browse all elements of the table
        for counter in range(tableSize):
            for counter1 in range(0, tableSize-counter-1):
                # change the elements if the first one is more than the second one
                if tab[counter1] > tab[counter1+1] :
                    tab[counter1], tab[counter1+1] = tab[counter1+1], tab[counter1]

    return tab


def tri_Insertion(tab = []):
    # browse all elements of the table
    for counter in range(1, len(tab)): 
        k = tab[counter] 
        j = counter-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
        
    return tab

    

def tri_selection(tab = []):
    if len(tab)>=2:
        for i in range(len(tab)):
            # Trouver le min
            min = i
            for j in range(i+1, len(tab)):
                if tab[min] > tab[j]:
                    min = j
                        
            tmp = tab[i]
            tab[i] = tab[min]
            tab[min] = tmp
            
    return tab
#Code compares runtimes of linear and binary search
#
from algorithms import *
import time

def main():
    print("Code to look at runtime for linear vs. binary search.")
    data = readData("dataSorted.txt")
    numDig = 5 #number of digits to output


    #small list of information
    print("\n" + "-" * 10)
    print("\nList with " + str(len(data)) + " elements.\n")
    
    print("Find " + str(data[0]) + " - beginning of list")
    start = time.time()
    isInLinear(data[0], data)
    end = time.time()
    print("Linear ->  " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[0], data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind " + str(data[len(data)//2]) + " middle of list")
    start = time.clock()
    isInLinear(data[len(data)//2], data)
    end = time.clock()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[len(data)//2], data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind " + str(data[-1]) + " - end of list")
    start = time.clock()
    isInLinear(data[-1], data)
    end = time.clock()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[-1], data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind  " + str(data[-1]+1) + " - not in list")
    start = time.time()
    isInLinear(data[-1]+1, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[-1]+1, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    #Number of elements in the list is a bit over 'last'
    last = 10001000 #adds integers between 50 and 'last' 
    data = list(range(50, last))
    print("\n" + "-" * 10)
    print("\nList with " + str(len(data)) + " elements.\n")
    
    print("Find 57 - beginning of list")
    start = time.time()
    isInLinear(57, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(57, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 500000 - middle of list")
    start = time.time()
    isInLinear(500000, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(500000, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")
    
    print("\nFind " + str(data[-1]) + " - end of list")
    start = time.time()
    isInLinear(data[-1], data)
    end = time.time()
    print("Linear - " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[-1], data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind " + str(data[-1]+1) + " - not in list")
    start = time.time()
    isInLinear(data[-1]+1, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(data[-1]+1, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

main()

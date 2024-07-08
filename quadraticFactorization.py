import math

def QuadraticFunctionfactorization():
    equation = input("input:")
    index_of_xsquared = equation.find("x^")
    if index_of_xsquared != -1:
        partA = equation[:index_of_xsquared].strip()
        if partA == '':
            partA = '1'
    else:
        partA = '1'

    equation = equation[index_of_xsquared + len("x^") + 1:]
    
    index_of_x = equation.find("x")
    partB = equation[:index_of_x]
 
    equation = equation[index_of_x + len('x'):]
    partC = equation
    partA = int(partA)
    partB = int(partB)
    partC = int(partC)
    
    productOfAC = partA * partC
    print(productOfAC)
    factors = []
    for i in range(1,productOfAC + 1):
        if productOfAC % i == 0:
            factors.append(i)
            factors.append(-i)
    for factor in factors:
        for factor2 in factors:
            if factor + factor2 == partB:
                print("Factors are:", factor, "and" , factor2)
                return
    print("No factors of", productOfAC, "sum to", partB)
           

        
QuadraticFunctionfactorization()
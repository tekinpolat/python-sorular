""" 
Task:

Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers, and False - otherwise.
Examples:

two_are_positive(2, 4, -3) == True
two_are_positive(-4, 6, 8) == True
two_are_positive(4, -6, 9) == True
two_are_positive(-4, 6, 0) == False
two_are_positive(4, 6, 10) == False
two_are_positive(-14, -3, -4) == False

"""

def two_are_positive(sayi1, sayi2, sayi3):
    positif_sayi = 0
    
    if sayi1 > 0:
        positif_sayi += 1
        
    if sayi2 > 0:
        positif_sayi += 1
        
    if sayi3 > 0:
        positif_sayi += 1
        
    #if positif_sayi == 2:
    #    return True 
    #return False

    #ternary  (kısa if else)
    return True if positif_sayi == 2 else False
    


two_are_positive(2, 4, -3)
    
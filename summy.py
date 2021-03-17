""" 
Write a function that takes a string which has integers inside it separated by spaces, 
and your task is to convert each integer in the string into an integer and return their sum.
Example

summy("1 2 32 4")  ==> 6

"""

#cast --> dönüştürmek

def summy(string_of_ints):
    sayilar_list = string_of_ints.split() 
    
    toplam = 0
    
    for sayi in sayilar_list:
        toplam += int(sayi)
        
    return toplam


toplam = summy("1 2 32 43")
print(toplam)

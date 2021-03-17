"""  
Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given.
def no_odds(values):
"""
# 2+4                ok
# "tekin" + "polat"  ok
# "tekin" + [24]     error 


def no_odds(values):
    cift_sayilar_list = []
    for sayi in values:
        if sayi%2 == 0:
            cift_sayilar_list += [sayi]
            
    return cift_sayilar_list



#filter
def cift_sayi_mi(sayi):
    if sayi %2 == 0:
        return True
    
    return False

def no_odds_2(values):
    return list(filter(cift_sayi_mi, values))

#lambda 
def no_odds_3(values):
    return filter(lambda sayi : sayi%2 == 0 , values)



#def cift_sayi_mi(sayi) == lambda sayi

#lambda 
#tek satırda çözebilecek fonksiyonları lambda şeklinde tanımlayabiliriz
#o anda kullanacam başka yerde kullanmıyacam dediğin yerde lambda kullanabilir

cift_sayi_mi(4)

cift_sayilar_list = no_odds_2([0, 1, 2, 3])   #[0, 2]
print(cift_sayilar_list)
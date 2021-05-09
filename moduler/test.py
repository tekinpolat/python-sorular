import func 
import func as fn     #as --> alias = takma ad

print(func.ad)
print(fn.ad)

print(func.test())
print(fn.test())
print(fn.yazdir("Tekin"))



from func import *
print(ad)
print(test())
print(yazdir("Mervan"))


from func import ad 
print(ad)


from func import ad as isim


#modul dahil etmede takma isim 
# 1- isim uzun olduğunda 
# 2- aynı isimde daha önceden dahil edilmişse farklı isimdirmek için kullanılır



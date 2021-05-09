import mod.my_func 
import mod.my_func as fn

print(mod.my_func.yas)
print(fn.yas)
print(dir(fn))


#değişken, fonksiyon, class
from mod.my_func import * 


yas = 20
from mod.my_func import yas as ys

print(yas)


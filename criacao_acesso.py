frutas= ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)#imprime["maca", "banana" , "laranja", "pera"]
  
  
frutas.insert(1,"uva")     
print(frutas)#imprime["maca", "uva", "banana", "laranja", "pera"]   


frutas.remove("banana")
print(frutas)#imprime["maca", "uva", "laranja", "pera"]


fruta_removida=frutas.pop(2)
print(frutas)#imprime["maca", "uva", "pera"]
print(fruta_removida)#imprime "laranja"

frutas.sort()
print(frutas)#imprime["maca", "pera", "uva"]


frutas.reverse()
print(frutas)#imprime["uva", "pera", "maca"]
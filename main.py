#probando
from cliente import cliente
from trabajador import trabajador
from objeto import objeto
from evento import evento
from lugar import lugar


l1 = lugar(567, "Habitaciones A1", "Habitacion", "21B-64")
e1 = evento(456, "Estadia" , 2, l1.nombre)
c1 = cliente(123, "luis", "castro", "calle 402", "6631231", "luis@test.com", 2, e1.nombre, [l1.nombre])
t1 = trabajador(234, "jose", "martinez", "calle 305", "6218372", "jose@test.com" ,"jose123", "0000", [c1.nombre] , True)
o1 = objeto(345, "Computador", "laptop pequena", [l1.nombre], "Funcional")


print(l1)
print(e1)
print(c1)
print(t1)
print(o1)

#funciones





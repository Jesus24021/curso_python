#edad = 16

#if edad >= 18:
 #   print("Tienes acceso")
    
#else:
#    print("Aun no se cumple la mayoria de edad")     



ingreso_mensual = 81000
gasto_mensual = 80000


if ingreso_mensual > 9500:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en la miseria")
    elif ingreso_mensual - gasto_mensual < 3000:
        print("Bien pa, estas bien")
    else:
        print("Hay que practicar el ahorro para que te alcance")
elif ingreso_mensual > 1000:
    print("Estas econonicamente estable en Latinoamerica")
elif ingreso_mensual > 500 :
    print("Estas econonicamente estable en CDMX")
elif ingreso_mensual > 200 :
    print("Estas econonicamente estable en Honduras")          
    
else:                      
    print("Eres pobre ):")
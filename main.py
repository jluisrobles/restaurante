#Reto 3
print("----------- RETO 3 ----------")
"""Piensa un escenario en el que se quiere decidir un restaurante para una celebración.
Los organizadores quieren que cumpla uno de los siguientes puntos:
• Que haya 3 platos en el menú, que incluya DJ y dos horas de barra libre.
• Que haya cóctel de bienvenida, menú con dos platos y una hora de barra libre.
Utilizar los bloques try-except-finally para las posibles excepciones que se produzcan"""

# Restaurante 1
platos_menu1 = 3
dj_presente1 = True
horas_barra_libre1 = 2
coctel_bienvenida1 = False
platos_menu21 = 2
horas_barra_libre21 = 1


# Comprobación del restaurante
try:
    if (platos_menu1 == 3 and dj_presente1 and horas_barra_libre1 == 2) or (coctel_bienvenida1 and platos_menu21 == 2 and horas_barra_libre21 == 1):
        print("El restaurante cumple con una de las condiciones.")
    else:
        raise Exception("El restaurante no cumple con ninguna de las condiciones.")
except Exception as e:
    print("Excepción:", str(e))
finally:
    print("A disfrutar del evento.")

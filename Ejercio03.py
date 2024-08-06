def calcular_media(puntuaciones):
    return sum(puntuaciones) / len(puntuaciones)

def determinar_califacion(media):
    if 90 <= media <= 100:
        return "A"
    elif 80 <= media < 90:
        return "B"
    elif 70 <= media < 80:
        return "C"
    elif 60 <= media < 70:
        return "D"
    elif 60<= media < 70:
        return "E"
    
puntuaciones = []
for i in range(4):
    puntuacion = int(input(f"Ingresa la puntuacion{i+1}: "))
    puntuaciones.append(puntuacion)
    
media = calcular_media(puntuaciones)

calificacion = determinar_califacion(media)

print(f"Las puntuaciones ingresadas son: {puntuaciones}")
print(f"La media de las puntuaciones es: {media}")
print(f"La calificacion correspondiente es: {calificacion}")
                       
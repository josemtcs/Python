calificaciones= [85,90,78,92,88]
calificaciones.append(100)
calificaciones.append(65)
calificaciones[2]=55
calificaciones[3]=77
calificaciones.pop(0)
prom= sum(calificaciones)/len(calificaciones)
calificacionesmin= min(calificaciones)
calificacionesmax= max(calificaciones)

print(calificaciones)
print(f'Esta es la calificacion mas baja: {calificacionesmin}')
print(f'Esta es la calificnacion mas alta: {calificacionesmax}')
print(f'Este es el promedio de las calificaciones: {prom}')
for calificacion in calificaciones:
    calificacion_mayorprom=[calificacion]
    if calificacion > prom:
        print(f'Estas son las calificaciones arriba del promedio : {calificacion_mayorprom}')
calificaciones.sort()
print(calificaciones)
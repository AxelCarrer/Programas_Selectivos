#Calcular la nota final
parcial = float(input("Nota de parciales (0-100): "))
proyecto = float(input("Nota de proyecto (0-100): "))
examen = float(input("Nota de examen final (0-100): "))

if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
    print("ERROR: las notas deben estar entre 0 y 100")
else:
    calificacion_final = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)

print("Nota final: ", calificacion_final)
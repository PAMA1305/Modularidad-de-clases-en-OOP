# main.py
from mi_clase import MiClase
from alumno import Alumno

def main():
    persona = MiClase("Carlos")
    print(persona.saludar())
alumno1 = Alumno()
alumno1.set_nombre("Pedro")
alumno1.set_apellido_paterno("Morales")
alumno1.set_apellido_materno ("Lopez")
alumno1.set_no_control(12345678)
alumno1. set_semestre (5)

alumno = Alumno()
registro_alumnos = {}
alumnos_dict = {}

registro_alumnos [0] = alumno1
print (f"Nombre: {registro_alumnos [0].get_nombre()}")
print(alumno1.mostrar_info())
print( "Nombre:", alumno1.get_nombre())
print("Apellido Paterno:", alumno1.get_apellido_paterno())
print("Apellido Materno:", alumno1.get_apellido_materno())
print("No. Control:", alumno1.get_no_control())
print ("Semestre:", alumno1.get_semestre())
print ("Nombre Completo:", alumno1.get_nombre_completo())



for i in range(1, 51):
    nombre = f"Nombre{i}"
    apellido_paterno = f"Apellido Paterno{i}"
    apellido_materno = f"Apellido Materno{i}"
    no_control = f"20{i:02d}00{i}"  # Ejemplo de no. control
    semestre = i % 8 + 1  # Semestre de 1 a 8




for no_control, alumno in alumnos_dict.items():
    print(alumno.mostrar_info())

for i in range(3):
    alumno1.set_nombre (input("introduce el Nombre: "))
    alumno1.set_apellido_paterno (input("introduce el apellidopaterno: "))
    alumno1.set_apellido_materno (input("introduce el apellido materno: "))
    alumno1.set_no_control (input("introduce el numero de control: "))
    alumno1.set_semestre (int(input("Semestre: ")))

    registro_alumnos[i] = alumno1
for i in range (3):
    print(f"nombre:{registro_alumnos[i].get_nombre()}")
if __name__ == "__main__":
    main()

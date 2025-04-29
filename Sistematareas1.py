# Estructuras de datos principales
tareas = []  # Lista para almacenar las tareas normales
historial = []  # Lista que actúa como pila para el historial de acciones
tareasUrgentes = []  # Lista que actúa como cola para tareas urgentes (FIFO)
arbolTareas = {  # Árbol para organizar tareas jerárquicamente
    "Proyecto Principal": {
        "Frontend": ["Diseño UI", "Revisión de estilos"],
        "Backend": ["API Login", "Gestión de BD"]
    }
}

# Función para agregar una tarea normal
def agregarTarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)  # Agrega la tarea al final de la lista
    historial.append(f"Tarea agregada con éxito: {tarea}")  # Registra en el historial
    print("Tarea agregada correctamente.")

# Función para mostrar todas las tareas normales
def mostrarTareas():
    print("\nTareas actuales:")
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, t in enumerate(tareas):
            print(f"{i+1}. {t}")

# Función para editar una tarea existente
def editarTarea():
    mostrarTareas()  # Primero muestra las tareas actuales
    try:
        indice = int(input("Ingrese el número de la tarea a editar: ")) - 1
        if 0 <= indice < len(tareas):
            nueva = input("Ingrese el nuevo nombre de la tarea: ")
            historial.append(f"Tarea editada: {tareas[indice]} -> {nueva}")  # Guarda en historial
            tareas[indice] = nueva  # Actualiza la tarea
            print("Tarea actualizada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Función para eliminar una tarea
def eliminarTarea():
    mostrarTareas()
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            historial.append(f"Tarea eliminada: {tareas[indice]}")  # Guarda en historial
            tareas.pop(indice)  # Elimina tarea de la lista
            print("Tarea eliminada con éxito.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Función para agregar una tarea urgente
def agregarUrgencia():
    urgente = input("Ingrese una tarea urgente: ")
    tareasUrgentes.append(urgente)  # Añade tarea urgente al final de la cola
    historial.append(f"Tarea urgente agregada: {urgente}")
    print("Tarea urgente registrada.")

# Función para procesar (resolver) la primera tarea urgente
def procesarUrgente():
    if tareasUrgentes:
        tarea = tareasUrgentes.pop(0)  # Elimina y toma la primera tarea de la cola
        print(f"Procesando tarea urgente: {tarea}")
        historial.append(f"Tarea urgente procesada: {tarea}")
    else:
        print("No hay tareas urgentes.")

# Función para ver la primera y última tarea urgente
def verColaUrgente():
    print("\nTareas urgentes:")
    if tareasUrgentes:
        print(f"Primera tarea urgente: {tareasUrgentes[0]}")
        print(f"Última tarea urgente: {tareasUrgentes[-1]}")
    else:
        print("No hay tareas urgentes.")

# Función para mostrar el árbol de organización de tareas
def mostrarArbol():
    print("\nOrganización jerárquica del proyecto:")
    for area, subtareas in arbolTareas["Proyecto Principal"].items():
        print(f"- {area}:")  # Muestra área principal
        for sub in subtareas:
            print(f"  * {sub}")  # Muestra subtareas dentro del área

# Función para mostrar el historial de cambios (últimos 5)
def mostrarHistorial():
    print("\nHistorial de cambios (últimos 5):")
    if historial:
        for item in reversed(historial[-5:]):  # Solo muestra las 5 últimas acciones
            print(f"- {item}")
    else:
        print("No hay historial aún.")

# Menú principal que permite interactuar con el sistema
def menu():
    while True:
        # Opciones disponibles para el usuario
        print("\n=== Menú del Sistema de Gestión de Tareas ===")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Agregar tarea urgente")
        print("6. Procesar tarea urgente")
        print("7. Mostrar historial de cambios")
        print("8. Ver estructura de árbol de tareas")
        print("9. Ver primera y última tarea urgente")
        print("10. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregarTarea()
            elif opcion == 2:
                editarTarea()
            elif opcion == 3:
                eliminarTarea()
            elif opcion == 4:
                mostrarTareas()
            elif opcion == 5:
                agregarUrgencia()
            elif opcion == 6:
                procesarUrgente()
            elif opcion == 7:
                mostrarHistorial()
            elif opcion == 8:
                mostrarArbol()
            elif opcion == 9:
                verColaUrgente()
            elif opcion == 10:
                print("Hasta la vista.")
                break  # Termina el ciclo y cierra el programa
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Iniciar el programa
menu()

# Ejercicio 1— “Caja del Kiosco”

nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Cliente: ")

# 2. Pedir cantidad de productos a comprar (entero positivo > 0)
cant_str = input("Cantidad de productos: ")
while not cant_str.isdigit() or int(cant_str) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cant_str = input("Cantidad de productos: ")

cantidad_productos = int(cant_str)

total_sin_descuentos = 0.0
total_con_descuentos = 0.0

# 3. Por cada producto usar for
for i in range(1, cantidad_productos + 1):
    print(f"\nProducto {i}")
    
    # Pedir precio
    precio_str = input("Precio: ")
    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: El precio debe ser un número entero positivo.")
        precio_str = input("Precio: ")
    
    precio = float(precio_str)
    
    # Pedir si tiene descuento (S/N)
    descuento_opt = input("Descuento (S/N): ").lower()
    while descuento_opt != "s" and descuento_opt != "n":
        print("Error: Ingrese 'S' o 'N'.")
        descuento_opt = input("Descuento (S/N): ").lower()
    
    total_sin_descuentos += precio
    
    if descuento_opt == "s":
        total_con_descuentos += precio * 0.90
    else:
        total_con_descuentos += precio

# 4. Cálculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad_productos

# Mostrar resultados
print("\n" + "="*30)
print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#------------------------------------------------------
# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#------------------------------------------------------

# Credenciales fijas
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

intentos = 0
acceso_concedido = False

# Proceso de Login (Máximo 3 intentos)
while intentos < 3 and not acceso_concedido:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    usuario_input = input("Usuario: ")
    clave_input = input("Clave: ")
    
    if usuario_input == USUARIO_CORRECTO and clave_input == CLAVE_CORRECTA:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("\nCuenta bloqueada.")
else:
    # Menú repetitivo
    opcion = ""
    clave_actual = CLAVE_CORRECTA
    
    while opcion != "4":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")
        
        opcion = input("Opción: ")
        
        # Validaciones de la opción
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            if opcion == "1":
                print("Estado: Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirme nueva clave: ")
                    if nueva_clave == confirmacion:
                        clave_actual = nueva_clave
                        print("Clave cambiada con éxito.")
                    else:
                        print("Error: las claves no coinciden.")
            elif opcion == "3":
                print("Mensaje: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día.'")
            elif opcion == "4":
                print("Saliendo del sistema...")

#---------------------------------------------------------
#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
#---------------------------------------------------------

# Variables individuales para turnos del Lunes (4 turnos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables individuales para turnos del Martes (3 turnos)
martes1 = ""
martes2 = ""
martes3 = ""

# Pedir nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: El nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")

opcion = ""
while opcion != "5":
    print("\n" + "="*30)
    print("--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Elija una opción: ")
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: Opción inválida.")
        continue

    # 1. RESERVAR TURNO
    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: Día inválido.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")
            
        paciente_lower = paciente.lower()
        
        if dia == "1":
            # Verificar repetido
            if (lunes1.lower() == paciente_lower or lunes2.lower() == paciente_lower or 
                lunes3.lower() == paciente_lower or lunes4.lower() == paciente_lower):
                print(f"Error: {paciente} ya tiene un turno reservado para el Lunes.")
            else:
                # Guardar en primer espacio libre
                if lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes (Turno 4).")
                else:
                    print("Error: No hay turnos disponibles para el Lunes.")

        elif dia == "2":
            # Verificar repetido
            if (martes1.lower() == paciente_lower or martes2.lower() == paciente_lower or 
                martes3.lower() == paciente_lower):
                print(f"Error: {paciente} ya tiene un turno reservado para el Martes.")
            else:
                # Guardar en primer espacio libre
                if martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes (Turno 3).")
                else:
                    print("Error: No hay turnos disponibles para el Martes.")

    # 2. CANCELAR TURNO
    elif opcion == "2":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: Día inválido.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            
        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")
            
        paciente_lower = paciente.lower()
        cancelado = False
        
        if dia == "1":
            if lunes1.lower() == paciente_lower:
                lunes1 = ""
                cancelado = True
            elif lunes2.lower() == paciente_lower:
                lunes2 = ""
                cancelado = True
            elif lunes3.lower() == paciente_lower:
                lunes3 = ""
                cancelado = True
            elif lunes4.lower() == paciente_lower:
                lunes4 = ""
                cancelado = True
        elif dia == "2":
            if martes1.lower() == paciente_lower:
                martes1 = ""
                cancelado = True
            elif martes2.lower() == paciente_lower:
                martes2 = ""
                cancelado = True
            elif martes3.lower() == paciente_lower:
                martes3 = ""
                cancelado = True
                
        if cancelado:
            print(f"Turno de {paciente} cancelado exitosamente.")
        else:
            print(f"Error: No se encontró al paciente {paciente} en ese día.")

    # 3. VER AGENDA DEL DÍA
    elif opcion == "3":
        dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: Día inválido.")
            dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ")
            
        if dia == "1":
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # 4. RESUMEN GENERAL
    elif opcion == "4":
        occ_lunes = 0
        if lunes1 != "": occ_lunes += 1
        if lunes2 != "": occ_lunes += 1
        if lunes3 != "": occ_lunes += 1
        if lunes4 != "": occ_lunes += 1
        disp_lunes = 4 - occ_lunes

        occ_martes = 0
        if martes1 != "": occ_martes += 1
        if martes2 != "": occ_martes += 1
        if martes3 != "": occ_martes += 1
        disp_martes = 3 - occ_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes : {occ_lunes} ocupados, {disp_lunes} disponibles.")
        print(f"Martes: {occ_martes} ocupados, {disp_martes} disponibles.")
        
        if occ_lunes > occ_martes:
            print("Día con más turnos ocupados: Lunes")
        elif occ_martes > occ_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos ocupados: Empate entre Lunes y Martes")

print("\nSistema cerrado. ¡Hasta luego!")

#-------------------------------------------------
#Ejercicio 4 — “Escape Room: La Bóveda”
#-------------------------------------------------

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

# Pedir nombre del agente
agente = input("Nombre del Agente: ")
while not agente.isalpha():
    print("Error: El nombre del agente solo debe contener letras.")
    agente = input("Nombre del Agente: ")

print(f"\n¡Bienvenido Agente {agente}! La misión comienza.")

# Ciclo del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Verificación de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        break  # Se activa el bloqueo por alarma
        
    print("\n" + "="*35)
    print(f"ESTADO | Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")
    print("1. Forzar cerradura (Costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (Costo: -10 energía, -3 tiempo)")
    print("3. Descansar (Costo: +15 energía, -1 tiempo)")
    
    opc = input("Seleccione una opción: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 3:
        print("Error: Ingrese un número válido (1-3).")
        opc = input("Seleccione una opción: ")
        
    opcion = int(opc)

    # OPCIÓN 1: FORZAR CERRADURA
    if opcion == 1:
        forzar_seguidos += 1
        energia -= 20
        tiempo -= 2
        
        # Regla Anti-Spam
        if forzar_seguidos == 3:
            print("\n¡La cerradura se trabó por intentar forzarla consecutivamente! Se activó la alarma.")
            alarma = True
        else:
            # Riesgo por energía baja
            if energia < 40:
                print("\n¡Riesgo de alarma por baja energía!")
                num_riesgo = input("Elija un número del 1 al 3: ")
                while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                    print("Error: Debe elegir un número del 1 al 3.")
                    num_riesgo = input("Elija un número del 1 al 3: ")
                    
                if int(num_riesgo) == 3:
                    alarma = True
                    print("¡Cometiste un error al forzar! Alarma activada.")
            
            if not alarma:
                cerraduras_abiertas += 1
                print(f"¡Éxito! Abriste 1 cerradura. Total: {cerraduras_abiertas}/3.")

    # OPCIÓN 2: HACKEAR PANEL
    elif opcion == 2:
        forzar_seguidos = 0  # Corta racha
        energia -= 10
        tiempo -= 3
        
        print("Hackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"> Progreso paso {paso}/4 - Código: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f"¡Código suficiente completado! Se abrió 1 cerradura automáticamente. Total: {cerraduras_abiertas}/3.")

    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:
        forzar_seguidos = 0  # Corta racha
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma activa te causa estrés (-10 energía extra).")
        else:
            print("Descansaste y recuperaste energía.")

# CONDICIONES DE FIN DE JUEGO
print("\n" + "="*35)
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {agente} ha abierto la bóveda con éxito.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA: El sistema se bloqueó debido a la alarma activa. Misión fallida.")
else:
    print("DERROTA: Te has quedado sin energía o sin tiempo. Misión fallida.")

#-------------------------------------------------------
# Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 
#-------------------------------------------------------

# Paso 1: Configuración del Personaje
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Paso 2: Inicialización de Estadísticas
vida_gladiador = 100        
vida_enemigo = 100          
pociones = 3                
ataque_pesado_base = 15     
dano_enemigo = 12           
juego_activo = True         

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: El Ciclo de Combate
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opc = input("Opción: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 3:
        print("Error: Ingrese un número válido.")
        opc = input("Opción: ")
        
    opcion = int(opc)
    
    # TURNO DEL JUGADOR
    if opcion == 1:
        dano_final = float(ataque_pesado_base)
        if vida_enemigo < 20:
            dano_final = ataque_pesado_base * 1.5  # Golpe Crítico (float)
            print("¡GOLPE CRÍTICO!")
            
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
        
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print(f"¡Te has curado! Recuperaste 30 HP. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones! Pierdes la oportunidad de curarte.")

    # TURNO DEL ENEMIGO (Solo si sigue vivo tras el ataque del jugador)
    if vida_enemigo > 0:
        vida_gladiador -= dano_enemigo
        print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

# Paso 4: Fin del Juego
print("\n" + "="*30)
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
    
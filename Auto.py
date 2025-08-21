class ReglaDiagnostico:
    def __init__(self, condiciones, resultado):
        self.condiciones = condiciones
        self.resultado = resultado


class MotorInferenciaAuto:
    def __init__(self):
        # Base de conocimiento: reglas iniciales
        self.base_conocimiento = [
            ReglaDiagnostico(["falla encendido", "tablero sin luz"], "Posible causa: batería descargada"),
            ReglaDiagnostico(["falla encendido", "tablero con luz"], "Posible causa: fallo en el motor de arranque"),
            ReglaDiagnostico(["enciende", "se apaga al acelerar"], "Posible causa: problema en el suministro de combustible"),
            ReglaDiagnostico(["humo escape negro"], "Posible causa: mezcla rica de combustible"),
            ReglaDiagnostico(["humo escape blanco"], "Posible causa: falla en la junta de culata")
        ]

    def evaluar(self, hechos):
        """
        Recibe una lista de hechos (síntomas) y determina qué regla coincide.
        """
        for regla in self.base_conocimiento:
            if all(cond in hechos for cond in regla.condiciones):
                return regla.resultado
        return "No se encontró un diagnóstico con los síntomas dados."


# ===============================
# Programa principal
# ===============================
if __name__ == "__main__":
    motor = MotorInferenciaAuto()
    hechos_usuario = []

    print("=== SISTEMA EXPERTO: DIAGNÓSTICO DE VEHÍCULOS 🚗🔧 ===\n")
    print("Responde con 's' para Sí o 'n' para No.\n")

    # Preguntas al usuario
    if input("¿El vehículo enciende? (s/n): ").lower() == "n":
        hechos_usuario.append("falla encendido")
        if input("¿El tablero enciende? (s/n): ").lower() == "s":
            hechos_usuario.append("tablero con luz")
        else:
            hechos_usuario.append("tablero sin luz")
    else:
        hechos_usuario.append("enciende")
        if input("¿Se apaga al acelerar? (s/n): ").lower() == "s":
            hechos_usuario.append("se apaga al acelerar")

    if input("¿Sale humo negro del escape? (s/n): ").lower() == "s":
        hechos_usuario.append("humo escape negro")

    if input("¿Sale humo blanco constante del escape? (s/n): ").lower() == "s":
        hechos_usuario.append("humo escape blanco")

    # Diagnóstico final
    print("\n=== RESULTADO DEL DIAGNÓSTICO ===")
    print(motor.evaluar(hechos_usuario))

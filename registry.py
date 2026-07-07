from models import Persona

class RegistroPersonas:
    def __init__(self):
        self._personas: dict[str, Persona] = {}

    def cargar_datos(self, datos: list[tuple[str, str, str, int]]):
        for dni, nombre, apellido, edad in datos:
            if dni in self._personas:
                raise ValueError(f"El DNI ya se encuentra registrado.")
            persona = Persona(dni, nombre, apellido, edad)
            self._personas[dni] = persona

    def formatear_registros(self) -> dict[str, tuple[str, str, int]]:
        return {
            dni: (persona.nombre, persona.apellido, persona.edad)
            for dni, persona in self._personas.items()
        }

    def obtener_mayor_edad(self) -> Persona:
        if not self._personas:
            raise ValueError("No hay personas registradas.")
        return max(self._personas.values(), key=lambda p: p.edad)

    def obtener_menor_edad(self) -> Persona:
        if not self._personas:
            raise ValueError("No hay personas registradas.")
        return min(self._personas.values(), key=lambda p: p.edad)

    def segmentar_por_edad(self, umbral: int = 25) -> dict[str, list[Persona]]:
        segmentado = {
            "menor_igual": [],
            "mayor": []
        }
        for persona in self._personas.values():
            if persona.edad <= umbral:
                segmentado["menor_igual"].append(persona)
            else:
                segmentado["mayor"].append(persona)
        return segmentado

    def promedio_edad(self) -> float:
        if not self._personas:
            return 0.0
        total_edad = sum(persona.edad for persona in self._personas.values())
        return total_edad / len(self._personas)

    def consultar_edad(self, dni: str) -> int:
        if dni not in self._personas:
            raise KeyError(f"El DNI no está registrado.")
        return self._personas[dni].edad

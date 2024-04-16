from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas=None, listados_respuestas=None):
        self.nombre = nombre
        self.preguntas = preguntas if preguntas is not None else []
        self.listados_respuestas = listados_respuestas if listados_respuestas is not None else []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)


class Limitada_edad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, preguntas=None, listados_respuestas=None):
        super().__init__(nombre, preguntas, listados_respuestas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima


class Limitada_region(Encuesta):
    def __init__(self, nombre, regiones, preguntas=None, listados_respuestas=None):
        super().__init__(nombre, preguntas, listados_respuestas)
        self.regiones = regiones

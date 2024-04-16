class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def responder_encuesta(self, encuesta, respuestas):
        listado_respuestas = Listado_Respuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)


class Listado_Respuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas

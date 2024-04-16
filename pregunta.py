from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, requerida: bool, alternativas: str):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [
			Alternativa(dicc["contenido"],dicc["ayuda"]) for dicc in alternativas
		]

    def mostrar_pregunta(self, ):
            print(self.enunciado)
            
            if self.ayuda:
                print("ayuda!!",self.ayuda)
                
            for obj_alter in self.__alternativas:
                print(obj_alter.mostrar_alternativa())
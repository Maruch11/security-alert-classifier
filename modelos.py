class Instancia:
    """
    Representa un registro del dataset.
    """
    def __init__(self, intentos_login, ips_distintas, alerta):
        self.intentos_login = intentos_login
        self.ips_distintas = ips_distintas
        self.alerta = alerta

    def mostrar(self):
        """
        Instancia.mostrar() imprime como tupla la instancia
        """
        print((self.intentos_login), ( self.ips_distintas), (self.alerta))

    def es_sospechosa(self):
        """
        Instancia.es_sospechosa() responde True si la instancia pertenece a la clase sospechosa según la etiqueta real almacenada en alerta
        """    
        return self.alerta == 1
class ModeloBase:
    pass

class ModeloUmbral:
    """
    Representa al clasificador baseline.
    """
    def __init__(self, umbral_intentos, umbral_ips):
        self.umbral_intentos = umbral_intentos
        self.umbral_ips = umbral_ips

    def predecir(self, instancia):
        """
        ModeloUmbral.predecir(instancia) recibe una Instancia y devuelve una predicción.
        """
        return(
            instancia.intentos_login > self.umbral_intentos
            and
            instancia.ips_distintas > self.umbral_ips
            )

class ModeloKNN:
    pass
    
if __name__ == "__main__":
            
    print(Instancia(10, 6, 1).es_sospechosa())
    print(Instancia(10, 6, 0).es_sospechosa())
        
    modelo = ModeloUmbral(8, 5)

    instancia = Instancia(10, 6, 1)

    print(modelo.predecir(instancia))
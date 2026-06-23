class Instancia:
    """
    Representa un registro del dataset.
    """
    def __init__(self, intentos_login, ips_distintas, alerta=None):
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
    def __init__(self, k, metrica):
        if k <= 0 or k % 2 == 0:
           raise ValueError("Error de valor k")
        if metrica not in {"euclideana", "manhattan"}:
            raise ValueError("Error de valor métrica")
        self.k = k
        self.metrica = metrica
        self.instancias_entrenamiento = None  
        
    def entrenar(self, instancias_entrenamiento):
        """
        Entrena el modelo KNN. 
        En este caso, no hace nada porque KNN es un algoritmo "perezoso".
        Sólo almacena las instancias de entrenamiento.
        """
        self.instancias_entrenamiento = instancias_entrenamiento

    def predecir(self, instancia):
        """
        Predice la clase de la instancia usando el algoritmo KNN.
        """
        vecinos = self._obtener_vecinos(instancia)
        votos = sum([vecino.alerta for vecino in vecinos])
        return int(votos > self.k / 2)

    def _calcular_distancia(self, instancia1, instancia2):
        """
        Calcula distancia entre dos instancias. 
        Consulta metrica configurada en modelo.
        Instancia1 la instancia que se quiere clasificar.
        Instancia2 es una instancia del conjunto de entrenamiento.
        Retorna un float que representa la distancia entre ambas instancias.
        """
        if self.metrica ==  "euclideana": 
            return ((instancia1.intentos_login - instancia2.intentos_login) ** 2 + (instancia1.ips_distintas - instancia2.ips_distintas) ** 2) ** 0.5
        if self.metrica == "manhattan":
            return abs(instancia1.intentos_login - instancia2.intentos_login) + abs(instancia1.ips_distintas - instancia2.ips_distintas)

    def _obtener_vecinos(self, instancia):
        """
        Devuelve los k vecinos más cercanos a la instancia.
        """
        if self.instancias_entrenamiento is None:
            raise ValueError("No hay instancias de entrenamiento cargadas.")
        return sorted(
            self.instancias_entrenamiento, 
            key=lambda x: self._calcular_distancia(instancia, x)
        )[:self.k]

if __name__ == "__main__":
            
    print(Instancia(10, 6, 1).es_sospechosa())
    print(Instancia(10, 6, 0).es_sospechosa())
        
    modelo = ModeloUmbral(8, 5)

    instancia = Instancia(10, 6, 1)

    print(modelo.predecir(instancia))
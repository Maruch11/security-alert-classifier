from dataset import cargar_dataset

instancias = cargar_dataset("data/alertas.csv")
print(len(instancias))
instancias[0].mostrar()

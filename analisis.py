from modelos import ModeloUmbral

def cantidad_instancias(instancias):
    return len(instancias)

def distribucion_clases(instancias):
    normal = 0
    sospechosa = 0
    for instancia in instancias:
        if instancia.alerta == 0:
            normal += 1
        else:
            sospechosa +=1
    return normal, sospechosa

def promedio_intentos_login(instancias):
    total = 0

    for instancia in instancias:
        total += instancia.intentos_login

    return total / len(instancias)


def promedio_ips_distintas(instancias):
    total = 0

    for instancia in instancias:
        total += instancia.ips_distintas

    return total / len(instancias)

def evaluar_modelo(modelo, instancias):
    """
    Recorre las instancias y compara.
    """
    tp = 0
    tn = 0 
    fp = 0
    fn = 0

    for instancia in instancias:
        etiqueta_real = instancia.es_sospechosa()
        prediccion = modelo.predecir(instancia)
        if etiqueta_real == True and prediccion == True:
            tp += 1
        elif etiqueta_real == False and prediccion == False:
            tn += 1
        elif etiqueta_real == False and prediccion == True:
            fp += 1
        else:
            fn += 1
    
    accuracy = ((tp + tn) / (tp+tn+fp+fn))* 100

    recall = (tp/(tp+fn))* 100

    precision = (tp/(tp+fp))* 100

    return tp, tn, fp, fn, accuracy, recall, precision


if __name__ == "__main__":

    # Pruebas 
    from dataset import cargar_dataset

    instancias = cargar_dataset("data/alertas.csv")
    
    modelo = ModeloUmbral(8, 5)

    # Prueba de cantidad_instancias
    print(cantidad_instancias(instancias))

    # Prueba de distribucion_clases
    print(distribucion_clases(instancias))

    # Prueba de promedio_intentos_login
    print(promedio_intentos_login(instancias))

    # Prueba de promedio_ips_distintas
    print(promedio_ips_distintas(instancias))

    # Prueba de evaluar modelo
    print(evaluar_modelo(modelo, instancias))
    # Desempaquetar tupla
    tp, tn, fp, fn, accuracy, recall, precision = evaluar_modelo(modelo, instancias) 
    print("-"*30)
    print("EVALUACION MODELO BASELINE")
    print("-"*30)
    print(f"TP: {tp}")
    print(f"TN: {tn}")
    print(f"FP: {fp}")
    print(f"FN: {fn}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Recall: {recall:.2f}%")
    print(f"Precision: {precision:.2f}%")
    

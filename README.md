# Sistema de Clasificación de Alertas de Seguridad

## Descripción

Este proyecto implementa un sistema de clasificación de alertas de seguridad utilizando Python y el algoritmo K-Nearest Neighbors (KNN) desarrollado desde cero.

El objetivo es aplicar conceptos fundamentales de Machine Learning mediante el análisis de alertas generadas por un sistema de monitoreo. A partir de datos históricos etiquetados, el sistema aprende patrones de comportamiento y clasifica nuevas alertas como normales o sospechosas.

Además de los conceptos de aprendizaje automático, el proyecto incorpora mediciones de rendimiento y análisis de complejidad temporal para evaluar el costo computacional de los algoritmos implementados.

---

## Objetivos

* Comprender la estructura de un dataset supervisado.
* Diferenciar features y target.
* Representar observaciones mediante clases y estructuras de datos.
* Implementar algoritmos de clasificación sin utilizar bibliotecas de Machine Learning.
* Aplicar la distancia Manhattan para medir similitud entre observaciones.
* Implementar un clasificador K-Nearest Neighbors (KNN).
* Comparar un modelo basado en reglas (ModeloUmbral) con un modelo de Machine Learning (KNN).
* Evaluar el desempeño del modelo mediante métricas básicas.
* Analizar tiempos de ejecución y complejidad algorítmica.

---

## Problema

El sistema debe determinar si una alerta de seguridad es normal o sospechosa a partir de información histórica.

Cada registro del dataset contiene:

* Cantidad de intentos de login detectados.
* Cantidad de direcciones IP distintas involucradas.
* Etiqueta de clasificación.

---

## Arquitectura conceptual

- Dataset
- Features y Target
- ModeloUmbral (Baseline)
- Distancia Manhattan
- Vecinos mas cercanos
- KNN
- Entrenamiento
- Predicción
- Evaluación
- Tiempos y Big O

---

## Flujo de Machine Learning

```text
Dataset
    │
    ▼
Carga de datos
    │
    ▼
Análisis exploratorio
    │
    ▼
Separación Train/Test
    │
    ▼
Entrenamiento
    │
    ├── Modelo por umbral
    │
    └── KNN
    │
    ▼
Predicción
    │
    ▼
Evaluación
```
---

## Data storytelling

1. ¿Qué datos tengo?
2. ¿Cómo comparo alertas?
3. ¿Cómo aprende el modelo?
4. ¿Qué predice?
5. ¿Qué tan bien funciona?
6. ¿Cuánto cuesta computacionalmente?

```
Tengo datos
↓
Los represento como features
↓
Mido similitud con Manhattan
↓
Uso esa similitud en KNN
↓
Entreno
↓
Predigo
↓
Evalúo accuracy
↓
Mido tiempos y complejidad
```

## Dataset

### Variables

| Variable       | Descripción                           |
| -------------- | ------------------------------------- |
| intentos_login | Cantidad de intentos de autenticación |
| ips_distintas  | Cantidad de direcciones IP observadas |
| alerta         | Clasificación de la alerta            |

La **variable objetivo (target)** es:

- `alerta`

porque es lo que el modelo debe aprender a predecir.

Las **Features** son:

- `intentos_login`
- `ips_distintas`

### Clases

| Valor | Significado       |
| ----- | ----------------- |
| 0     | Alerta normal     |
| 1     | Alerta sospechosa |


observación: [15, 5, 1]

se interpreta como:

Features:
- intentos_login = 15
- ips_distintas = 5

Target:
- alerta = 1

nueva alerta: [18, 6, ?]

el KNN utilizará las features 18, 6 para predecir el valor faltante del target: alerta = ?

### Generación de Datos

El dataset contiene 1000 registros:

- 750 alertas normales (75%)
- 250 alertas sospechosas (25%)

Para evitar que el problema sea trivial, las clases presentan solapamiento parcial en sus valores.

| Feature | Normal | Sospechosa |
|----------|----------|----------|
| intentos_login | 1-8 | 5-20 |
| ips_distintas | 1-3 | 3-10 |

Debido a este solapamiento, algunas observaciones pueden pertenecer a regiones similares del espacio de características, haciendo necesario el uso de algoritmos de clasificación como KNN.

### Ejemplo

```csv
intentos_login,ips_distintas,alerta
2,1,0
4,1,0
15,5,1
30,10,1
1,1,0
3,1,0
5,2,0
7,3,0
8,3,1
10,4,1
```

*Nota*:

El dataset utilizado en este proyecto es sintético y fue generado con fines educativos para facilitar la comprensión de los algoritmos de clasificación supervisada.

En escenarios reales, los datos suelen provenir de registros históricos generados por herramientas de monitoreo y seguridad, como firewalls, IDS/IPS o plataformas SIEM.

---

## Estructura del Proyecto

```text
clasificador-alertas-seguridad/
├── data/
│   └── alertas.csv
├── reports/
├── scripts/
│   └── generar_alertas.csv
│
├── dataset.py
├── analisis.py
├── modelos.py
├── main.py
└──README.md
```

---
## Responsabilidades

Archivo|	Responsabilidad
---|---
dataset.py|	Carga del CSV y preparación de datos
analisis.py|	EDA básico y métricas descriptivas
modelos.py|	Instancia, ModeloBase, ModeloUmbral, ClasificadorKNN
main.py|	Orquestación, entrenamiento, evaluación y medición de tiempos
data/|	Dataset de entrada
reports/|	Reportes CSV/JSON o resultados de evaluación

## Componentes

### dataset.py

Responsable de cargar y preparar los datos para su utilización por los modelos. 

Transforma el almacenamiento persistido (CSV) en objetos del dominio que el resto de la aplicación utilizará.

#### Funciones principales

* Abrir el archivo CSV.
* Leer los registros.
* Validar la estructura y los datos básicos.
* Generar instancias de `Instancia`, que representan alertas individuales y encapsulan atributos y operaciones relacionadas con una alerta.
* Retornar la colección de instancias cargadas.

### analisis.py

Contiene funciones de análisis exploratorio de datos (EDA).

Ejemplos:

* Cantidad de instancias.
* Distribución de clases.
* Promedio de intentos de login.
* Promedio de IPs distintas.
* Evaluacion de modelo

```
analisis.py
├─cantidad_instancias()
├─ distribucion_clases()
├─promedio_intentos_login()
├─ promedio_intentos_login()
└─ evaluar_modelo()
```

### modelos.py

Contiene las clases principales del proyecto.

#### Instancia

Representa una alerta individual.

#### ModeloBase

Clase base para los modelos de clasificación.

#### ModeloUmbral

Clasificador simple basado en reglas.

Se utiliza como modelo baseline para comparar el desempeño del algoritmo KNN.

#### ClasificadorKNN

Implementación manual del algoritmo K-Nearest Neighbors utilizando distancia Manhattan. Calcula la distancia Manhattan entre alertas y selecciona los K vecinos más cercanos para realizar la clasificación.

```modelos.py
├─ Instancia
├─ ModeloBase
├─ ModeloUmbral
└─ ClasificadorKNN
```

#### CHECKS (BORRAR?)
✅ Instancia encapsula las features (intentos_login, ips_distintas) y la etiqueta real (alerta).
✅ es_sospechosa() devuelve un booleano basado en la etiqueta real.
✅ ModeloUmbral almacena los parámetros del modelo (umbral_intentos, umbral_ips).
✅ predecir(instancia) utiliza las features de la instancia y los umbrales del modelo.
✅ Separación clara entre:
- realidad: instancia.es_sospechosa()
- predicción: modelo.predecir(instancia)

### main.py

Punto de entrada del sistema.

Responsabilidades:

1. Cargar el dataset.
2. Realizar análisis descriptivo.
3. Entrenar los modelos.
4. Realizar predicciones.
5. Evaluar resultados.
6. Medir tiempos de ejecución.

---

## Distancia Manhattan

El algoritmo KNN utiliza la distancia Manhattan para medir la similitud entre alertas. 

La distancia entre dos observaciones se calcula como:

```
D(A,B) = |x1 - x2| + |y1 - y2|
```
Cuanto menor es la distancia, más parecidas son las alertas.

---

## Entrenamiento y Predicción

El clasificador KNN utiliza las instancias del conjunto de entrenamiento para clasificar nuevas alertas. Durante el entrenamiento, el modelo almacena las alertas históricas.

Durante la predicción, para predecir una nueva alerta:

1. Calcula distancias.
2. Selecciona vecinos.
3. Realiza votación.
4. Predice la clase.

---

## Evaluación

La evaluación compara:

- ModeloUmbral (baseline)
- ClasificadorKNN

El sistema calcula métricas básicas para medir el desempeño de los clasificadores.

### Accuracy

Porcentaje de predicciones correctas sobre el conjunto de prueba.

### Matriz de Confusión

Permite visualizar aciertos y errores de clasificación.

---

## Rendimiento

Además de la calidad de las predicciones, se registran métricas de rendimiento:

* Tiempo de entrenamiento.
* Tiempo de predicción.
* Tiempo total de ejecución.

También se analiza la complejidad temporal de los algoritmos implementados.

El proyecto analiza tanto la calidad de las predicciones como el costo computacional de cada modelo.

### Complejidad

| Algoritmo         | Entrenamiento | Predicción |
| ----------------- | ------------- | ---------- |
| Modelo por umbral | O(1)          | O(1)       |
| KNN               | O(1)          | O(n)       |

---

## Ejemplo de Salida

```text
=== Análisis de Alertas de Seguridad ===

Para clasificar nuevas alertas, se utiliza el algoritmo KNN.

Se cargaron 1000 alertas históricas.

Normales: 750
Sospechosas: 250

=== Distancia Manhattan ===

Alerta A: (2, 1)
Alerta B: (15, 5)

Distancia: 17

=== Similitud entre Alertas ===

Una distancia menor indica alertas más similares.

=== Entrenamiento ===

Modelo KNN entrenado con 800 alertas.

Tiempo de entrenamiento: 0.0003 s

=== Predicción ===

Nueva alerta:
Intentos login: 28
IPs distintas: 7

Vecinos más cercanos:

(15,5) -> clase 1
(20,7) -> clase 1
(12,4) -> clase 0

Predicción: SOSPECHOSA

=== Evaluación ===

= Modelo Umbral =

Accuracy: 74%

= Clasificador KNN =

Accuracy: 88%

=== Rendimiento ===

Tiempo de predicción: 0.0008 s
Tiempo total: 0.0011 s
Complejidad de predicción: O(n)
```

---

## Tecnologías Utilizadas

* Python 3
* csv
* collections
* math
* time
* random

---

## Orden de implementación

1. data/alertas.csv
   - Definir 1000 registros.
   - Distribución 75% normales y 25% sospechosas.
   - Definir rangos de las features.
   - Generar solapamiento entre clases.

2. modelos.py
   - Crear Instancia.
   - Crear ModeloBase.
   - Crear ModeloUmbral.
   - Crear ClasificadorKNN.

3. dataset.py
   - Implementar carga del CSV.
   - Convertir registros en instancias.

4. analisis.py
   - Implementar cantidad de instancias.
   - Implementar distribución de clases.
   - Implementar promedios.

5. main.py
   - Cargar dataset.
   - Ejecutar análisis.
   - Entrenar ModeloUmbral.
   - Entrenar KNN.
   - Realizar predicciones.
   - Evaluar accuracy.
   - Medir tiempos.

6. reports/
   - Generar reportes y resultados.

7. README.md
   - Actualizar documentación final.

## Autor 

Mariana Emilia Mazzoccoli

Trabajo Práctico de Fundamentos de Machine Learning.

Implementación educativa de un sistema de clasificación supervisada utilizando K-Nearest Neighbors (KNN) desarrollado desde cero en Python.

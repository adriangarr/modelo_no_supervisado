# Descripción de los datos

## Fuente
El CSV contiene 600 registros generados artificialmente y de forma reproducible para fines académicos. No se encontró una fuente pública real para esta muestra, por lo que se construyó un dataset simulado, opción contemplada en la consigna.

## Variables
| Variable | Tipo | Descripción |
|---|---|---|
| `distancia_km` | Numérica | Distancia simulada del recorrido en kilómetros. |
| `pasajeros` | Entero | Cantidad simulada de pasajeros. |
| `espera_min` | Numérica | Tiempo de espera simulado en minutos. |
| `indice_congestion` | Numérica | Indicador simulado de 0 a 1; mayor valor representa más congestión en la simulación. |
| `tiempo_recorrido_min` | Numérica | Duración simulada del recorrido en minutos. |

## Preparación y método
El programa valida columnas y valores vacíos. Después estandariza variables con `StandardScaler`, ya que usan escalas diferentes, y aplica K-Means con tres grupos por defecto. La columna `grupo` se crea después del entrenamiento; no es una etiqueta original.

## Evaluación
Se calcula el coeficiente de silueta como medida exploratoria de la separación entre grupos. Debe interpretarse junto con el gráfico y las características promedio de cada grupo.

## Limitaciones
Los registros no representan rutas, horarios, personas ni mediciones reales. El resultado demuestra el método académico y no debe utilizarse para decisiones operativas reales sin datos reales validados.

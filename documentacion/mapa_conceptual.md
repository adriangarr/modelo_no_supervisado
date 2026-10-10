# Mapa conceptual: aprendizaje no supervisado

```text
Dataset de viajes simulados (CSV)
              |
              v
Validar columnas y valores
              |
              v
Estandarizar variables (StandardScaler)
              |
              v
K-Means encuentra 3 grupos
              |
        +-----+------+
        |            |
        v            v
Etiquetas grupo   Centroides
        |            |
        +-----+------+
              v
Resumen, gráfico y coeficiente de silueta
              |
              v
Interpretar con limitaciones del dataset
```

K-Means no utiliza etiquetas correctas conocidas durante el entrenamiento; agrupa registros según la similitud de sus variables.

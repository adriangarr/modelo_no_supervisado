from pathlib import Path
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

COLUMNAS = ["distancia_km", "pasajeros", "espera_min", "indice_congestion", "tiempo_recorrido_min"]

def cargar_datos(ruta_csv):
    datos = pd.read_csv(ruta_csv)
    faltantes = [c for c in COLUMNAS if c not in datos.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {faltantes}")
    if datos[COLUMNAS].isnull().any().any():
        raise ValueError("El dataset contiene valores vacíos.")
    return datos

def agrupar_viajes(datos, n_clusters=3, random_state=42):
    if n_clusters < 2 or n_clusters >= len(datos):
        raise ValueError("n_clusters debe ser al menos 2 y menor al número de filas.")
    scaler = StandardScaler()
    X = scaler.fit_transform(datos[COLUMNAS])
    modelo = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    etiquetas = modelo.fit_predict(X)
    resultado = datos.copy()
    resultado["grupo"] = etiquetas
    silueta = silhouette_score(X, etiquetas)
    centros = pd.DataFrame(scaler.inverse_transform(modelo.cluster_centers_), columns=COLUMNAS)
    return resultado, modelo, scaler, centros, silueta

def describir_grupos(resultado):
    return resultado.groupby("grupo")[COLUMNAS].mean().round(2)

def crear_grafico(resultado, ruta_salida):
    ruta_salida = Path(ruta_salida)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 6))
    for grupo, parte in resultado.groupby("grupo"):
        ax.scatter(parte["espera_min"], parte["tiempo_recorrido_min"], alpha=.7, s=25, label=f"Grupo {grupo}")
    ax.set_title("Agrupamiento de viajes: espera y tiempo de recorrido")
    ax.set_xlabel("Tiempo de espera (minutos)")
    ax.set_ylabel("Tiempo de recorrido (minutos)")
    ax.grid(True, alpha=.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(ruta_salida, dpi=160)
    plt.close(fig)
    return ruta_salida

def ejecutar(ruta_csv, carpeta_resultados="resultados", n_clusters=3):
    carpeta = Path(carpeta_resultados)
    carpeta.mkdir(parents=True, exist_ok=True)
    datos = cargar_datos(ruta_csv)
    resultado, modelo, scaler, centros, silueta = agrupar_viajes(datos, n_clusters)
    resultado.to_csv(carpeta/"viajes_agrupados.csv", index=False)
    describir_grupos(resultado).to_csv(carpeta/"resumen_grupos.csv")
    centros.to_csv(carpeta/"centros_grupos.csv", index=False)
    crear_grafico(resultado, carpeta/"grafico_agrupamiento.png")
    (carpeta/"evaluacion_modelo.txt").write_text(
        f"Registros analizados: {len(datos)}\\nNúmero de grupos: {n_clusters}\\nCoeficiente de silueta: {silueta:.4f}\\n\\n"
        + describir_grupos(resultado).to_string()
        + "\\n\\nNota: dataset sintético; no representa tráfico real.\\n", encoding="utf-8")
    return resultado, silueta

def main():
    p = argparse.ArgumentParser(description="Agrupa viajes de transporte con K-Means.")
    p.add_argument("--datos", default="datos/datos_transporte_no_supervisados.csv")
    p.add_argument("--salida", default="resultados")
    p.add_argument("--grupos", type=int, default=3)
    a = p.parse_args()
    r, s = ejecutar(a.datos, a.salida, a.grupos)
    print(f"Registros agrupados: {len(r)}")
    print(f"Grupos encontrados: {sorted(r['grupo'].unique().tolist())}")
    print(f"Coeficiente de silueta: {s:.4f}")
    print(f"Resultados guardados en: {a.salida}")

if __name__ == "__main__":
    main()

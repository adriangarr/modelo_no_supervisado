# Sistema Inteligente de Rutas — Aprendizaje no supervisado

## Objetivo
Explorar patrones en viajes simulados de transporte usando K-Means.

## Archivos
- `modelo_no_supervisado.py`: código de agrupamiento.
- `datos/datos_transporte_no_supervisados.csv`: 600 registros sintéticos.
- `documentacion/descripcion_datos.md`: diccionario y limitaciones.
- `documentacion/guion_video.md`: guion sugerido.
- `pruebas/test_modelo_no_supervisado.py`: pruebas automáticas.
- `resultados/`: salidas y gráfico de ejemplo.

## Ejecución
```bash
pip install -r requirements.txt
python modelo_no_supervisado.py
python -m unittest discover -s pruebas -v
```
Se puede cambiar el número de grupos con `python modelo_no_supervisado.py --grupos 4`.

## Limitación
El dataset es sintético, no son mediciones oficiales ni datos reales del tráfico. Los grupos solo describen los datos simulados.

## Enlaces
Repositorio: https://github.com/adriangarr/sistema-inteligente-de-rutas
Video: añadir el enlace real después de grabarlo.

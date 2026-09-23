# Modelo de riesgo de default crediticio — Lending Club

**Ciencia de Datos Aplicada · ITBA**
Gianluca Giannine Lizarraga · Timoteo Harrington · Lucas Kim

Sistema de decisión para el otorgamiento de préstamos, basado en datos históricos de Lending Club (plataforma estadounidense de préstamos peer-to-peer). El objetivo es estimar la probabilidad de default (PD) de un solicitante a partir de información disponible al momento de la solicitud, traducirla en bandas de riesgo, y estimar una prima de riesgo de default (PD × LGD) para apoyar la decisión de otorgamiento.

## Estado del proyecto

| Entrega | Contenido | Estado |
|---|---|---|
| E01 — Propuesta de proyecto | Problema de negocio, objetivos, alcance | ✅ Entregado |
| E02 — Recopilación y preparación de datos | Este repo: dataset, EDA, leakage, split, LGD, transformaciones | ✅ Entregado |
| E03 — Modelado de la solución | Baseline, Random Forest, LightGBM/XGBoost, evaluación, bandas | Pendiente |
| E04 — Despliegue y presentación | Pricing, informe final | Pendiente |

## Estructura del repositorio

```
├── data/                    # CSV descargado (no versionado, ver scripts/download_data.py)
├── notebooks/
│   └── 02_recopilacion_preparacion_datos.ipynb   # Notebook del Entregable 02
├── scripts/
│   └── download_data.py     # Descarga el dataset
├── requirements.txt
└── README.md
```

## Cómo reproducir

```bash
git clone <url-del-repo>
cd lending-club-riesgo-default
pip install -r requirements.txt
python scripts/download_data.py
jupyter notebook notebooks/02_recopilacion_preparacion_datos.ipynb
```

## Dataset

Se utiliza la versión 2007-2011 del dataset de Lending Club (~39.700 préstamos, 111 variables, sin codificar). Se eligió esta ventana temporal, en vez del dataset completo 2007-2018 (~2.26M de filas), por ser manejable en un entorno de cómputo estándar y por permitir observar directamente el efecto del ciclo económico (crisis financiera de 2008) dentro de los propios datos — justificación completa en el notebook, Sección 1.

## Metodología (resumen)

1. **Target**: `loan_status` → binario (`Fully Paid` vs. `Charged Off`), excluyendo préstamos `Current`.
2. **Clasificación de variables**: ex-ante (disponibles al solicitar el préstamo) vs. ex-post (solo existen después de otorgado, se excluyen por *data leakage*). `grade`, `sub_grade` e `int_rate` se tratan aparte por ser output del propio scoring de Lending Club.
3. **Split temporal**: train/test por fecha de originación, *antes* del EDA enfocado en el target — el test representa el futuro, no una muestra al azar.
4. **LGD**: calculado empíricamente sobre los préstamos de train que entraron en default, no asumido.
5. **Output final del sistema**: una prima de riesgo de default (PD × LGD) por solicitante — no una tasa de interés final. La tasa base y el resto de la estructura de tasa (plazo, iliquidez) quedan fuera del alcance de este TP.

## Autores

Gianluca Giannine Lizarraga · Timoteo Harrington · Lucas Kim — ITBA, 2026

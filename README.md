# 🛒 Análisis de Comportamiento y Retención en Retail

**Análisis exploratorio de transacciones para identificar patrones de compra y segmentar clientes.**

## 🎯 Contexto del Proyecto
Este proyecto analiza un dataset transaccional de un comercio minorista con el objetivo de entender mejor los hábitos de consumo. A través del análisis de datos históricos, se busca identificar en qué momentos se concentra la mayor actividad, cómo se componen los ingresos por categoría y evaluar el estado de la retención de usuarios mediante un modelo RFM.

Evolución del Proyecto: La versión inicial se desarrolló como un análisis exploratorio ad-hoc utilizando Python (Pandas). Para escalar la solución y permitir el consumo interactivo por parte de stakeholders, la arquitectura evolucionó hacia un modelo de Inteligencia de Negocios. Se implementó un modelo de datos dimensional (Star Schema) consumido a través de Excel (Power Query/Pivot) y dashboards interactivos en Power BI.

## 🛠️ Stack Tecnológico
* **Procesamiento y Análisis:** Python (Pandas), SQL, Excel
* **Visualización de Datos:** Matplotlib, Seaborn (`seaborn.objects`), Power BI
* **Entorno:** Jupyter Notebook, Git

---

## 💡 Resumen Ejecutivo (Hallazgos Principales)

* **Horarios de mayor actividad vs. Recaudación:** Se observó que el pico de transacciones ocurre a las 19:00 hs (impulsado por la categoría *Home Decor*), sin embargo, la hora que genera mayores ingresos brutos es a la 01:00 hs.
  * *Oportunidad detectada:* Ofrecer descuentos en horarios de baja actividad podría simplemente trasladar las ventas que igual iban a ocurrir en el horario pico, sin generar ingresos nuevos. Una alternativa más rentable sería aprovechar el tráfico natural de las 19:00 hs ofreciendo beneficios (como envío bonificado) a partir de un ticket de compra más alto.
* **Segmentación de Clientes (Modelo RFM):** Agrupando a los clientes por su Recencia, Frecuencia y Valor Monetario, se determinó que aproximadamente un 95% de los clientes compraron una sola vez y al cruzar esta informacion con el analisis de concentracion de revenue resulta en que aproximadamente el 50% de los clientes concentran el 80% del revenue.
* **Comportamiento por Medio de Pago:** Los datos muestran que los usuarios no presentan grandes diferencias entre metodos de pago, resultan en montos similares (teniendo en cuenta que es un dataset ficticio descargado de Kaggle).

---

## 📂 Estructura del Repositorio

```text
retail-transactions-analysis/
│
├── data/
│   ├── raw/                   # Dataset original
│   └── processed/             # Dataset limpio listo para BI
├── dashboards/
│   ├── reporte_comercial.pbix # Archivo de Power BI
│   └── analisis_ad_hoc.xlsx   # Archivo Excel con Pareto y Pivot Tables
├── notebooks/
│   └── analisis_visual.ipynb  # Código fuente: Limpieza, EDA y Modelo RFM
├── images/
│   └── powerbi_dashboard.png  # Captura para mostrar en el README
├── README.md
└── requirements.txt
└── .gitignore

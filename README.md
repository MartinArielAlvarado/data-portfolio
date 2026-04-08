# 🛒 Análisis de Comportamiento y Retención en Retail

**Un enfoque Data-Driven para la optimización del revenue y la fidelización de clientes.**

## 🎯 Contexto del Proyecto
En el competitivo sector del retail, atraer nuevos clientes es significativamente más costoso que retener a los actuales. Este proyecto analiza un dataset transaccional de e-commerce para extraer patrones de consumo ocultos, evaluar la salud de la cartera de clientes mediante segmentación RFM y proponer estrategias de precios (pricing) accionables que maximicen la rentabilidad sin canibalizar las ventas orgánicas.

## 🛠️ Stack Tecnológico
* **Procesamiento y Análisis:** Python (Pandas)
* **Visualización de Datos:** Matplotlib, Seaborn (`seaborn.objects`)
* **Entorno:** Jupyter Notebook, Git

---

## 💡 Resumen Ejecutivo (Hallazgos Principales)

* **Paradoja de Tráfico vs. Rentabilidad:** Se detectó que el pico de mayor volumen de ventas ocurre a las 19:00 hs (liderado fuertemente por la categoría *Home Decor*), mientras que la hora de mayor recaudación es a la(s) [Completar con la hora de mayor ingreso].
  * *Acción Estratégica:* Se desaconseja aplicar descuentos directos en horas valle para evitar la **canibalización de ventas** de las horas pico. En su lugar, se sugiere implementar promociones de venta cruzada o bonificaciones de envío superando un ticket mínimo durante las 19:00 hs para capitalizar el tráfico natural e incrementar el ticket promedio.
* **Segmentación de Clientes (Modelo RFM):** A través del análisis de Recencia, Frecuencia y Valor Monetario, se determinó que [Completar con un hallazgo clave de tu RFM, ej: "el X% de los clientes genera el Y% del revenue", o "existe un segmento de 'Riesgo de Abandono' que requiere campañas de retargeting urgente"].
* **Comportamiento por Medio de Pago:** El análisis demostró que los usuarios que abonan con Tarjeta de Crédito [Completar con la respuesta a tu pregunta 1: gastan más, menos, o igual que los de efectivo].

---

## 📂 Estructura del Repositorio

El proyecto sigue estándares de la industria para facilitar su reproducibilidad:

```text
retail-transactions-analysis/
│
├── data/
│   └── raw/                   # Dataset original (Kaggle)
├── notebooks/
│   └── analisis_visual.ipynb  # Código fuente: Limpieza, EDA y Modelo RFM
├── img/                       # Visualizaciones clave exportadas
├── README.md
├── requirements.txt           # Dependencias del entorno
└── .gitignore

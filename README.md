# 🎬 Netflix Movie Explorer (Portfolio Project)

Proyecto de portafolio de **análisis de datos** + **aplicación interactiva** para explorar un catálogo de películas y visualizar resultados desde una interfaz web.

Este repositorio combina:
- **Notebooks (Jupyter)** para exploración, limpieza y preparación de datos.
- **App en Streamlit** para consultar y filtrar películas desde una base de datos **PostgreSQL**.

---

## 📷Capturas
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/07f5b03b-f658-4261-a0af-e20ba92d4ace" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/896bc050-17ba-461a-b8ce-fa13de9bdd66" />



## ✨ Qué incluye

### 📊 Data Analysis (Notebooks)
En la carpeta `notebook/` encontrarás notebooks enfocados en:
- carga del dataset y revisión de calidad
- transformación de columnas (fechas, categorías, duración, etc.)
- análisis exploratorio (EDA) y consultas
- carga de tablas a la base de datos (por ejemplo `Movies` y `categoria`)

Notebooks incluidos:
- `notebook/AnalisisCatalogoNetflix.ipynb`
- `notebook/AnalisisCatalogoNivel4.ipynb`
- `notebook/recomender_movie.ipynb`

---

### 🖥️ App (Streamlit)
La aplicación principal está en:
- [`app.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/app.py)

Funcionalidades implementadas en la UI:
- filtro por **categoría** (selectbox)
- filtro por **duración máxima** (slider)
- tarjetas con resultados y un modal **View** con detalles (cast y categorías)

Componentes principales:
- Filtros: [`ui/filters.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/ui/filters.py)
- Modal/info de película: [`ui/modals.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/ui/modals.py)
- Lógica/servicios: [`services/movie_service.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/services/movie_service.py)
- Acceso a datos: [`database/movies_querys.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/database/movies_querys.py)

---

## 🗃️ Base de datos (PostgreSQL)

La app consume datos desde PostgreSQL consultando directamente:
- `SELECT * FROM "Movies"`
- `SELECT * FROM "categoria"`

> Nota: el código usa identificadores entre comillas dobles, por lo que el nombre exacto de las tablas importa.

---

## 🧼 Transformaciones clave

En el preprocesamiento se aplican transformaciones como:
- conversión de `duration` a un campo numérico `duration_int` para poder filtrar por duración
- limpieza del texto de categorías para mostrar opciones consistentes en la UI

Archivo:
- [`utils/preprocess.py`](https://github.com/Daniel20051601/recomender_movie/blob/42565405ee204dbb3b44f1a169d0615e3e4fb960/utils/preprocess.py)

---

## ▶️ Demo local (rápido)

Ejecutar la app:
```bash
streamlit run app.py
```

---

## 📁 Estructura del proyecto

```text
.
├── app.py
├── database/
│   ├── conection.py
│   └── movies_querys.py
├── services/
│   └── movie_service.py
├── ui/
│   ├── filters.py
│   └── modals.py
├── utils/
│   └── preprocess.py
└── notebook/
    ├── AnalisisCatalogoNetflix.ipynb
    ├── AnalisisCatalogoNivel4.ipynb
    └── recomender_movie.ipynb
```

---

## 🧑‍💻 Autor

**Daniel20051601**

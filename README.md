# Quiz Semana 3 — Pilares de POO (leyendo desde Excel) 🧩

En este quiz demuestras que dominas los **tres pilares de la POO** que vimos esta semana:
**Encapsulamiento** (getters/setters con validación), **Herencia** (clase base y clases hijas)
y **Polimorfismo** (un mismo método con comportamiento distinto).

**Novedad de este quiz:** los datos vienen de un **archivo de Excel** (`empleados.xlsx`) con
varias columnas. La **lectura del Excel ya está lista** (y es robusta): tú te concentras en la
POO y en un pequeño reto de creatividad. 🚀

> Este quiz es **solo de POO**. No incluye bases de datos: eso lo exploramos aparte.

---

## 🎯 El reto

Una empresa tiene su nómina en `empleados.xlsx`: **24 empleados** y **12 columnas**.

| columna | ¿la usa el quiz? | para qué sirve |
|---------|------------------|----------------|
| `id` | ❌ | Identificador del empleado. |
| `nombre` | ✅ | Nombre. Si la celda está vacía, la fila se descarta. |
| `tipo` | ✅ | `PLANTA` o `CONTRATISTA`. Decide **qué clase hija** se crea. |
| `salario_base` | ✅ | Salario mensual. Lo valida tu **setter**. |
| `ciudad` | ✅ | Ciudad de trabajo (opcional: si falta, queda texto vacío). |
| `departamento` | ❌ | Área: Ventas, TI, Finanzas, RRHH, Logística, Marketing, Operaciones. |
| `cargo` | ❌ | Cargo concreto (Desarrollador, Contadora, Practicante…). |
| `nivel` | ❌ | Junior / Semi Senior / Senior. |
| `horas_semana` | ❌ | Horas contratadas por semana. |
| `fecha_ingreso` | ❌ | Fecha de entrada a la empresa. |
| `correo` | ❌ | Correo corporativo. |
| `activo` | ❌ | `SI` / `NO`: si sigue vinculado. |

Solo usaremos **nombre**, **tipo**, **salario_base** y **ciudad**; las demás columnas están
"por si acaso", para que veas que un buen lector **ignora lo que no necesita** en lugar de
romperse. 😉

El archivo trae además **dos hojas de ayuda** que puedes consultar cuando quieras:
- **`Diccionario`** — qué significa cada columna y cuáles usa el quiz.
- **`Casos_especiales`** — las filas raras del archivo, explicadas una por una.

> 💡 Tu programa **solo lee la primera hoja** (`Empleados`). Las otras dos son documentación
> para ti; no afectan al código.

Hay dos tipos de empleado y cada uno **cobra distinto** (polimorfismo):
- **PLANTA:** salario base **+ 30 %** de prestaciones.
- **CONTRATISTA:** **solo** su salario base.

### ⚠️ Las filas "trampa" (en amarillo dentro del Excel)

La lectura ya las descarta sola (robustez con `try/except` y validación). Son **5**:

| id | nombre | qué tiene de raro | qué pasa |
|----|--------|-------------------|----------|
| 5 | Sofía | salario **negativo** (`-100`) | tu **setter** lanza `ValueError` |
| 6 | *(vacío)* | **sin nombre** | fila incompleta → se ignora |
| 21 | Gabriela | tipo `TEMPORAL` (esa clase no existe) | `crear_empleado()` lanza `ValueError` |
| 22 | Felipe | salario en **texto** (`"no aplica"`) | `int("no aplica")` falla dentro del setter |
| 23 | Sara | **sin tipo** | fila incompleta → se ignora |

### ✅ Y dos casos borde que **sí** entran (en verde)

| id | nombre | qué tiene de raro | por qué sí entra |
|----|--------|-------------------|------------------|
| 20 | Santiago | salario `0` | **cero no es negativo**: la validación lo acepta |
| 24 | Emilio | tipo `planta` en minúscula y ciudad con espacios | `.strip().upper()` normaliza el dato |

De 24 filas quedan **19 empleados** en la nómina.

---

## 🛠️ Qué debes hacer

Instala primero las librerías para leer Excel (una sola vez):

```bash
pip install -r requirements.txt
```

Abre **`quiz_nomina.py`** y completa **todos los bloques `# TODO`**:

1. **Encapsulamiento** — en `EmpleadoBase`: guarda `_salario_base` (privado), crea el *getter*
   `@property` y el *setter* con validación (no permite negativos).
2. **Herencia** — `EmpleadoPlanta` y `EmpleadoContratista` heredan de `EmpleadoBase`.
3. **Polimorfismo** — sobreescribe `calcular_pago()` en cada clase hija.
4. Completa `crear_empleado()` y `obtener_informacion()`.

> 📌 **La función `leer_empleados_excel()` YA ESTÁ HECHA.** No la modifiques: es tu ejemplo de
> lectura robusta de un Excel.

### ✨ Reto extra (obligatorio): crea TU PROPIA función
Al final del archivo verás un hueco con la función `salario_promedio(empleados)`. **Cámbiala
por la función útil que tú quieras** (o complétala). Con 19 empleados en la nómina, ahora los
resultados sí son interesantes. Algunas ideas (elige **una** o propón la tuya):

- `salario_promedio(empleados)` → promedio de `salario_base`.
- `empleados_por_ciudad(empleados, ciudad)` → cuántos hay en esa ciudad.
- `empleado_mejor_pagado(empleados)` → el de mayor `calcular_pago()`.
- `nomina_total(empleados)` → cuánto paga la empresa en total al mes.
- `contar_por_tipo(empleados)` → cuántos de planta y cuántos contratistas.
- `ordenar_por_pago(empleados)` → la lista ordenada de mayor a menor pago.
- `ciudades_unicas(empleados)` → la lista de ciudades sin repetir.

Documéntala con un *docstring* y **llámala dentro de `ejecutar_quiz()`** para mostrar su resultado.

> 🏅 **Nivel PRO (opcional).** ¿Quieres usar las columnas extra (`departamento`,
> `horas_semana`, `activo`…)? Tus objetos hoy **solo guardan** nombre, tipo, salario y ciudad,
> así que primero tendrías que guardarlas también: añadir el parámetro en `__init__`, pasarlo
> en `crear_empleado()` y leer la columna en `leer_empleados_excel()`. Es un reto extra, no
> es obligatorio.

---

## ✅ Salida esperada (ejemplo)

Al ejecutar `python quiz_nomina.py` (con las clases completas) verás esto — primero los avisos
de las 5 filas inválidas y después los **19 empleados** que sí quedaron:

```
  [Aviso] Se ignoro Sofia: El salario no puede ser negativo.
  [Aviso] Fila incompleta ignorada.
  [Aviso] Se ignoro Gabriela: tipo desconocido 'TEMPORAL'
  [Aviso] Se ignoro Felipe: invalid literal for int() with base 10: 'no aplica'
  [Aviso] Fila incompleta ignorada.
--- Nomina ---
Ana | EmpleadoPlanta | Medellin | base $3000000 -> pago: 3900000.0
Luis | EmpleadoContratista | Bogota | base $2500000 -> pago: 2500000
Marta | EmpleadoPlanta | Medellin | base $4200000 -> pago: 5460000.0
Carlos | EmpleadoContratista | Cali | base $1800000 -> pago: 1800000
Diego | EmpleadoPlanta | Medellin | base $3500000 -> pago: 4550000.0
Valentina | EmpleadoContratista | Bogota | base $2800000 -> pago: 2800000
Camila | EmpleadoPlanta | Barranquilla | base $5200000 -> pago: 6760000.0
Andres | EmpleadoContratista | Medellin | base $3200000 -> pago: 3200000
Laura | EmpleadoPlanta | Cali | base $2400000 -> pago: 3120000.0
Julian | EmpleadoContratista | Bogota | base $4500000 -> pago: 4500000
Paula | EmpleadoPlanta | Medellin | base $3800000 -> pago: 4940000.0
Ricardo | EmpleadoPlanta | Bogota | base $6100000 -> pago: 7930000.0
Natalia | EmpleadoContratista | Pereira | base $2100000 -> pago: 2100000
Mateo | EmpleadoPlanta | Bucaramanga | base $2900000 -> pago: 3770000.0
Isabella | EmpleadoContratista | Medellin | base $3600000 -> pago: 3600000
Tomas | EmpleadoPlanta | Cartagena | base $2600000 -> pago: 3380000.0
Daniela | EmpleadoPlanta | Bogota | base $4700000 -> pago: 6110000.0
Santiago | EmpleadoContratista | Cali | base $0 -> pago: 0
Emilio | EmpleadoPlanta | Medellin | base $3300000 -> pago: 4290000.0
```

Fíjate en los dos últimos: **Santiago cobra 0** (cero pasa la validación porque no es negativo)
y **Emilio sí es `EmpleadoPlanta`** aunque en el Excel su tipo está en minúscula.

(El resultado de tu función-reto dependerá de lo que decidas crear.)

---

## 📤 ¿Cómo entregar?

### Paso 1 — Actualiza el repositorio del curso
Ya tienes clonado el repo del curso. Tráete lo nuevo (esta carpeta del quiz):

```bash
git pull
cd "MisProyectosPython/Quiz_semana 3"
```

> 💡 En VS Code también puedes usar la pestaña *Source Control* → sincronizar (pull).

### Paso 2 — Resuelve
Instala las librerías, completa los `# TODO`, crea tu función y ejecuta hasta que la salida
coincida con la esperada. Documenta tu código con comentarios y docstrings.

### Paso 3 — Presenta tu solución en un repositorio APARTE
Crea un repositorio **nuevo** en GitHub llamado **`quiz_semana3`** y, al crearlo, márcalo como
**Public** 🔓 (no privado). Luego sube tu solución:

```bash
git init
git add quiz_nomina.py empleados.xlsx requirements.txt
git commit -m "Quiz Semana 3 resuelto"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/quiz_semana3.git
git push -u origin main
```

> ⚠️ **El repositorio debe quedar público.** No hay que invitar a nadie como colaborador: si es
> público, con el enlace basta. Si por error lo creaste privado, cámbialo en
> **Settings → General → Danger Zone → Change repository visibility → Make public**.

### Paso 4 — Entrega en Canvas
Sube en Canvas **únicamente el enlace de tu repositorio `quiz_semana3`**. Nada más.

```
https://github.com/TU_USUARIO/quiz_semana3
```

> ✅ Antes de entregar, abre ese enlace en una **ventana de incógnito**. Si el repositorio se ve
> sin iniciar sesión, quedó bien público.

---

## 📊 ¿Qué se evalúa?

- [ ] **Encapsulamiento:** atributo privado + getter `@property` + setter que valida.
- [ ] **Herencia:** las dos clases hijas heredan de `EmpleadoBase`.
- [ ] **Polimorfismo:** `calcular_pago()` da un resultado distinto por tipo.
- [ ] **Tu propia función:** creada, documentada y usada en `ejecutar_quiz()`.
- [ ] Código con **comentarios y docstrings** claros.
- [ ] **Entrega:** repositorio `quiz_semana3` **público** y su enlace subido a Canvas.

¡Éxitos! Recuerda: un `# TODO` a la vez. 💪

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    # Importamos la librería marimo como 'mo'.
    # Esto es obligatorio para que funcionen los elementos interactivos
    # (sliders, botones), el texto con formato (markdown) y las
    # referencias entre celdas.
    # NO CAMBIAR NI ELIMINAR
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Ejercicios 4.11 - 4.20 del Tema 4: Diccionarios, conjuntos y comprensiones

    ## Ejercicio 4.11: Frecuencia de letras

    Dada la cadena `texto = "matematicas y programacion"`, construye un diccionario `frecuencia` donde cada clave es una letra (no el espacio) y su valor es el número de veces que aparece en `texto`, sin distinguir mayúsculas de minúsculas.

    Usa el patrón `d[c] = d.get(c, 0) + 1` para actualizar el conteo.

    Una vez construido el diccionario:

    1. Imprime la letra más frecuente y su conteo.
    2. Imprime el diccionario
    """)
    return


@app.cell
def _():
    # Ejercicio 4.11: Frecuencia de letras

    texto = "matematicas y programacion"

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.12: Inversión del diccionario de frecuencias

    A partir del diccionario `frecuencia` del ejercicio anterior (redefinido abajo), construye un nuevo diccionario `por_frecuencia` donde:

    - las **claves** son los valores de frecuencia (enteros),
    - los **valores** son **listas de letras** con esa frecuencia, en orden alfabético.

    Por ejemplo, si `frecuencia = {'a': 3, 'e': 3, 't': 2, 'm': 1}`, el resultado debe ser:
    ```python
    {3: ['a', 'e'], 2: ['t'], 1: ['m']}
    ```

    ¿Cuántas letras distintas aparecen exactamente una vez?
    """)
    return


@app.cell
def _():
    # Ejercicio 4.12: Inversión del diccionario de frecuencias

    # El diccionario frecuencia ya debe estar definido en la celda arriba

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.13: Contador de palabras

    Escribe una función `contar_palabras(texto)` que reciba una cadena de texto y devuelva un diccionario con el número de veces que aparece cada palabra, sin distinguir mayúsculas de minúsculas e ignorando los signos de puntuación básicos (`.`, `,`, `!`, `?`, `;`, `:`).

    Pruébala con:
    ```python
    "el gato y el perro. El gato duerme."
    ```
    El resultado esperado es `{'el': 3, 'gato': 2, 'y': 1, 'perro': 1, 'duerme': 1}`.

    Pruébala también con un texto más largo de tu elección.
    """)
    return


@app.function
# Ejercicio 4.13: Contador de palabras

def contar_palabras(texto: str) -> dict[str, int]:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.14: ¿Es inyectiva la función?

    Un diccionario puede representar una **función finita** $f: A \to B$: las claves son los elementos del dominio $A$ y los valores son las imágenes en $B$.

    Una función es **inyectiva** si elementos distintos del dominio tienen imágenes distintas:

    $$
    f(x) = f(y) \implies x = y.
    $$

    Escribe una función `es_inyectiva(f)` que reciba un diccionario y devuelva `True` si y solo si la función que representa es inyectiva.

    Pruébala con:

    - `{'a': 1, 'b': 2, 'c': 3}` → `True` (de hecho es biyectiva sobre su imagen)
    - `{'a': 1, 'b': 2, 'c': 1}` → `False` (`'a'` y `'c'` comparten imagen)
    - `{1: 'x'}` → `True` (función de un elemento)
    - `{}` → `True` (la función vacía es inyectiva por vacuidad)

    Pista: una función es inyectiva si y solo si no hay valores repetidos, es decir, `len(f.values()) == len(set(f.values()))`.
    """)
    return


@app.function
# Ejercicio 4.14: ¿Es inyectiva la función?

def es_inyectiva(f: dict) -> bool:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.15: Operaciones de conjuntos

    Genera dos listas, `a` y `b`, cada una con 12 enteros aleatorios en el intervalo $[0, 20]$ (con `random.seed(7)`).

    1. Convierte cada lista en un conjunto y calcula:
       - Unión $A \cup B$, intersección $A \cap B$, diferencia $A \setminus B$, diferencia simétrica $A \triangle B$.
    2. Comprueba: ¿son $A$ y $B$ disjuntos? ¿Es alguno subconjunto del otro?
    3. ¿Cuántos elementos del intervalo $[0, 20]$ (21 valores posibles) no aparecen en ninguna de las dos listas?
    """)
    return


@app.cell
def _():
    # Ejercicio 4.15: Operaciones de conjuntos
    import random

    random.seed(7)
    a = [random.randint(0, 20) for _ in range(12)]
    b = [random.randint(0, 20) for _ in range(12)]
    print("a =", a)
    print("b =", b)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.16: Comprensiones de listas

    Resuelve cada apartado con **una sola comprensión de lista** (sin escribir un bucle `for` explícito fuera de la comprensión):

    1. Lista de los cuadrados $1^2, 2^2, \ldots, 10^2$.
    2. Lista de los cuadrados de los impares del 1 al 20.
    3. Dada `palabras = ["hola", "mundo", "python", "matematicas", "algebra"]`, lista con las palabras que tienen más de 5 letras, transformadas a mayúsculas.
    4. Lista de los enteros de 1 a 50 que son múltiplos de 3 o de 5, pero **no de ambos** a la vez (diferencia simétrica). (Pista: `(cond_A) != (cond_B)` evalúa XOR sobre booleanos.)
    """)
    return


@app.cell
def _():
    # Ejercicio 4.16: Comprensiones de listas

    palabras = ["hola", "mundo", "python", "matematicas", "algebra"]

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.17: Conversión de unidades con comprensión

    Dada la lista de distancias en metros:
    ```python
    distancias_m = [0.5, 1.0, 5.0, 10.0, 42.195, 100.0, 1609.344]
    ```
    (el último valor es exactamente 1 milla).

    Usando **comprensiones de lista**, genera tres listas paralelas con las mismas distancias en:

    - **Yardas** (yd): $1\ \text{m} = 1 / 0.9144\ \text{yd}$
    - **Pies** (ft): $1\ \text{m} = 1 / 0.3048\ \text{ft}$
    - **Millas** (mi): $1\ \text{m} = 1 / 1609.344\ \text{mi}$

    Imprime una tabla formateada con cuatro columnas (metros, yardas, pies, millas) alineadas y con 3 decimales. El último valor debe mostrar exactamente 1.000 millas.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.17: Conversión de unidades con comprensión

    distancias_m = [0.5, 1.0, 5.0, 10.0, 42.195, 100.0, 1609.344]

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.18: Comprensión de diccionarios: tabla de divisores

    Escribe una función `tabla_divisores(numeros)` que reciba una lista de enteros positivos y devuelva un diccionario `{n: [divisores de n en orden creciente]}` construido con una **comprensión de diccionario**.

    Pruébala con `numeros = [12, 15, 28, 36, 100]`.

    A partir del diccionario resultante, responde:

    1. ¿Cuáles de esos números tienen exactamente 6 divisores? (Para un número de la forma $p^2 q$ con $p, q$ primos distintos se cumple $\tau(n) = 6$.)
    2. ¿Cuál es la suma de todos los divisores de 28? (Un número perfecto cumple que esta suma es $2n$.)
    """)
    return


@app.function
# Ejercicio 4.18: Comprensión de diccionarios: tabla de divisores

def tabla_divisores(numeros: list[int]) -> dict[int, list[int]]:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.19: Cadena sin vocales y frecuencia de consonantes

    Dada la cadena `frase = "La matematica es la reina de las ciencias"`:

    1. Construye una nueva cadena `sin_vocales` eliminando **todas las vocales** (mayúsculas y minúsculas, incluyendo las acentuadas). Usa una comprensión de lista para filtrar los caracteres y `.join()` para reconstruir la cadena.

    2. Construye un diccionario `freq_consonantes` que asocie a cada consonante que aparece en `frase` (en minúsculas, ignorando espacios y vocales) su número de apariciones. Usa una **comprensión de diccionario** apoyándote en `contar_palabras` o directamente en `frase`.

    3. Ordena el diccionario por frecuencia descendente e imprime las tres consonantes más frecuentes con sus conteos.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.19: Cadena sin vocales y frecuencia de consonantes

    frase = "La matematica es la reina de las ciencias"
    vocales = set("aeiouáéíóúAEIOUÁÉÍÓÚ")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.20: Creación y procesamiento de diccionario con entradas de usuario

    Un usuario va a teclear una secuencia de oraciones (en inglés) una tras otra pero letra a letra. La primera información que pasará el usuario es el número de oraciones (un entero positivo) que va a introducir. El fin de una oración se señala con almohadilla (`'#'`) y las palabras están separadas por espacios en blanco (`' '`). Genera un diccionario `vocabulario` con las palabras únicas que va a suministrar el usuario como llaves cumpliendo con:

    - todas las letras son minusculas,
    - todos los signos de puntuación se eliminan (estos son los de la cadena `'.,;:?!-/"()'`)

    El valor asociado a cada llave (palabra única) es una lista de tuplas de la forma `(no, np)` donde `no` denota el número de oración donde la palabra aparece y `np` el numero de orden de la palabra en la oración. Para `no` y `np` se tiene indexación basada en cero, es decir, la primera oración es la de índice cero y la primera palabra de una oración también tiene índice cero. Por ejemplo, de la oración:

    `I think, therefore I am`

    se debe formar el diccionario

    `{'i': [(0, 0), (0, 3)], 'think': [(0, 1)], 'therefore': [(0, 2)], 'am': [(0, 4)]}`.

    Además de generar el diccionario imprima:

    1. El número de palabras únicas.
    2. La palabra que más se repite.
    3. La palabra con más consonantes (en caso de empate la primera que aparece).


    **Nota:** En este ejercicio para evitar la entrada de caracteres por parte de cada uno de ustedes vamos a simular una función `input()` que va a funcionar exactamente como la nativa de Python. Por ello no modifique el código en la celda abajo y utilice después del mismo la función `input()` de Python como es usual. No tendrá que teclear nada después del prompt ya que la entrada se simula como si fuera de un usuario. Esto permite además que los valores arriba en cada inciso sean los que debe obtener.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.20: Creación y procesamiento de diccionario con entradas de usuario
    # No tocar las dos líneas de código abajo
    from siminput import sim_input

    input = sim_input("oraciones.dat")

    # A partir de aquí su código para el ejercicio
    # Utilice input() como es usual

    return


if __name__ == "__main__":
    app.run()

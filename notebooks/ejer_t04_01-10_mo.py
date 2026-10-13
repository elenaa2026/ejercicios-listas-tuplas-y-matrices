# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.24.0"
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
    # Ejercicios 4.1 - 4.10 del Tema 4: Listas, tuplas y matrices

    ## Ejercicio 4.1: Operaciones básicas con listas

    Dada la lista `mi_lista = [1, 2, 3, 4, 5, 6, 7]`, realiza las siguientes operaciones **en orden** y verifica el estado de la lista con `print` después de cada una:

    1. Cambia el primer elemento por `33`.
    2. Muestra los tres últimos elementos usando *slicing* con índice negativo.
    3. Reemplaza el elemento central (índice 3) por `-5`.
    4. Extiende la lista añadiendo `[8, 9, 10]` al final.
    5. Elimina la primera aparición del valor `3`.
    6. Inserta el valor `99` en la posición inmediatamente posterior al valor `2`.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.1: Operaciones básicas con listas

    mi_lista = [1, 2, 3, 4, 5, 6, 7]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.2: Slicing

    Dada la lista `num_1_100 = list(range(1, 101))` extrae de ella mediante slicing (la expresión más simple posible) e imprime:

    1. Una lista `l1` que contenga los números del 1 al 20 ambos inclusive.
    2. Una lista `l2` que contenga los números del 81 al 100 ambos inclusive.
    3. Una lista `l3` que contenga todos los números entre 24 y 54 ambos inclusive.
    4. Una lista `l4` de todos los números pares en `num_1_100`.
    5. Una lista `l5` de todos los números impares en `num_1_100`.
    6. Una lista `l6` de todos los múltiplos de 5 en `num_1_100`.
    7. Una lista `l7` de todos los múltiplos de 3 entre 81 y 99 (ambos inclusive) en orden inverso.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.2: Slicing

    num_1_100 = list(range(1, 101))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.3: Eliminar todas las ocurrencias de un valor

    Dada la lista `segunda_lista = [1, 2, 2, 4, 5, 2, 4, 2, 2]`, elimina **todas** las ocurrencias del valor `2` **modificando la propia lista** (sin crear una lista nueva ni asignar a una variable nueva).

    Pista: el método `.remove()` solo elimina la primera aparición. Plantea una estrategia que lo llame repetidamente, o itera la lista en orden inverso usando `range(len(...)-1, -1, -1)` y borra con `del`.

    Al final verifica que `2 not in segunda_lista` es `True` y que los demás elementos no han cambiado.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.3: Eliminar todas las ocurrencias de un valor

    segunda_lista = [1, 2, 2, 4, 5, 2, 4, 2, 2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.4: Generación aleatoria y eliminación de duplicados

    El código abajo genera una lista `aleatorios` con 60 enteros aleatorios en el intervalo $[0, 100]$ usando `random.randint(0, 100)` con semilla `random.seed(42)`.

    - La función `random.randint(a, b)` devuelve un número entero aleatorio dentro del rango `[a, b]` (ambos inclusive).
    - La función `random.seed(x)` inicializa el motor del generador de números pseudoaleatorios utilizando un valor inicial x, conocido como "semilla". Si estableces la misma semilla antes de ejecutar tu código, siempre obtendrás exactamente la misma secuencia de números **"aleatorios"**.

    1. Crea una lista `unicos` con los valores de `aleatorios` **sin repeticiones**, preservando el **orden de primera aparición**. Para ello itera la lista y añade cada elemento a `unicos` solo si aún no se encuentra en esa lista.

    2. Imprime cuántos valores únicos hay y calcula qué porcentaje del total representan.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.4: Generación aleatoria y eliminación de duplicados
    import random

    random.seed(42)
    aleatorios = []
    for _ in range(60):
        aleatorios.append(random.randint(0, 100))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.5: Rotación de listas

    Dada la lista `numeros = [1, 2, 3, 4, 5, 6, 7]`:

    1. Rota la lista 3 posiciones a la **derecha** (los últimos 3 elementos pasan al inicio) creando una nueva lista `rotacion_derecha`.

        Resultado esperado: `[5, 6, 7, 1, 2, 3, 4]`.
    2. Rota la lista 2 posiciones a la **izquierda** (los primeros 2 elementos pasan al final) creando una nueva lista `rotacion_izquierda`.

        Resultado esperado: `[3, 4, 5, 6, 7, 1, 2]`.

    **Sugerencia:** Usa slicing y concatenación de listas con `+`.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.5: Rotación de listas

    numeros = [1, 2, 3, 4, 5, 6, 7]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.6: Filtrado de lista mixta

    Dada la lista mixta `datos = [42, "hola", 3.14, "mundo", True, "Python", 100, False]`:

    1. Extrae a una nueva lista `cadenas` solo los elementos que son cadenas de caracteres.

    2. Extrae a una nueva lista `numeros` solo los elementos numéricos (enteros y flotantes).

    3. Extrae a una nueva lista `otros` los que elementos que no sean de los tipos anteriores.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.6: Filtrado de lista mixta

    datos = [42, "hola", 3.14, "mundo", True, "Python", 100, False]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.7: Suma acumulada

    Dada una lista de números reales $v = (v_0, v_1, \ldots, v_{n-1})$, la **suma acumulada** es la lista de sumas parciales

    $$
    S_k = \sum_{i=0}^{k} v_i, \quad k = 0, 1, \ldots, n-1.
    $$

    Escribe una función `suma_acumulada(v)` que reciba una lista de flotantes y devuelva su lista de sumas parciales. La función **no debe modificar** la lista original.

    Comprueba tu implementación con:

    - `suma_acumulada([1.0, 2.0, 3.0, 4.0])` → `[1.0, 3.0, 6.0, 10.0]`
    - `suma_acumulada([1.0, -1.0, 1.0, -1.0])` → `[1.0, 0.0, 1.0, 0.0]`
    - `suma_acumulada([0.5, 0.25, 0.125])` → `[0.5, 0.75, 0.875]`
    """)
    return


@app.function
# Ejercicio 4.7: Suma acumulada

def suma_acumulada(v: list[float]) -> list[float]:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.8: Intercalar dos secuencias

    Escribe una función `intercalar(a, b)` que reciba dos listas de longitudes potencialmente distintas y devuelva una **nueva lista** con los elementos alternados: primero `a[0]`, luego `b[0]`, luego `a[1]`, `b[1]`, y así sucesivamente. Los elementos restantes de la lista más larga se añaden al final.

    Ejemplos:

    - `intercalar([1, 3, 5], [2, 4, 6])` → `[1, 2, 3, 4, 5, 6]`
    - `intercalar([1, 3, 5], [2, 4, 6, 8, 10])` → `[1, 2, 3, 4, 5, 6, 8, 10]`
    - `intercalar([], [1, 2, 3])` → `[1, 2, 3]`
    - `intercalar([7], [])` → `[7]`

    **Sugerencia:** Una forma elegante: usa `zip(a, b)` para los pares solapados y añade la cola con *slicing*.
    """)
    return


@app.function
# Ejercicio 4.8: Intercalar dos secuencias

def intercalar(a: list, b: list) -> list:
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.9: Estandarización de textos para tokenización

    El **Procesamiento del Lenguaje Natural** (**NLP** por sus siglas en inglés) es un campo que combina la lingüística, la informática y la inteligencia artificial para permitir que los ordenadores comprendan, interpreten y generen lenguaje humano.

    El primer paso crítico en el NLP es transformar el texto en bruto en un formato con el que los ordenadores puedan trabajar eficazmente. Este proceso se conoce como **tokenización**. La tokenización consiste en descomponer el texto en unidades más pequeñas y manejables llamadas **tokens**, que pueden ser palabras, subpalabras o incluso caracteres individuales. Antes de tokenizar, el texto se **estandariza** para garantizar la coherencia. Esto incluye convertir todas las letras a minúsculas, eliminar la puntuación y aplicar otras técnicas de normalización.

    Dada la lista de oraciones
    ```python
    corpus_original = [
        "El código tiene un error.",
        "Tu código funciona bien.",
        "Corregí el error del código.",
        "El sistema no tiene errores.",
        "Escribe un código limpio.",
        "Este código no funciona.",
    ]
    ```

    1. Convierte todas letras a minúsculas.
    2. Elimina los signos de puntuación.
    3. Genera una lista `palabras` con todas las palabras únicas de `corpus_original` después de haber completado 1 y 2.

    **Sugerencia:** Emplea los métodos `str.lower()` para convertir a minúsculas y `str.replace()` para remplazar cualquier signo de puntuación contenido en la cadena `".,;:¿?¡!-\"()"` por la cadena vacía <code>&quot;&quot;</code>. Para separar una oración en palabras emplea `str.split()`
    """)
    return


@app.cell
def _():
    # Ejercicio 4.9: Estandarización de textos para tokenización

    corpus_original = [
        "El código tiene un error.",
        "Tu código funciona bien.",
        "Corregí el error del código.",
        "El sistema no tiene errores.",
        "Escribe un código limpio.",
        "Este código no funciona.",
    ]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 4.10: Creación y procesamiento de lista con entradas de usuario

    Un usuario va a teclear una secuencia de números enteros uno tras otro. El fin de la secuencia se tiene cuando el usuario escribe un punto (`.`). Genera una lista `lnumeros` con los números que va a suministrar el usuario e imprime:

    1. La suma de todos los números (-27113).
    2. El máximo de todos los números (9960).
    3. El mínimo de todos los números (-9788).
    4. La cantidad de números mayores que cero (57).
    5. La cantidad de números iguales a cero (0).
    6. La cantidad de números menores que cero (68).

    **Nota:** En este ejercicio para evitar la entrada de números por parte de cada uno de ustedes vamos a simular una función `input()` que va a funcionar exactamente como la nativa de Python. Por ello no modifique el código en la celda abajo y utilice después del mismo la función `input()` de Python como es usual. No tendrá que teclear nada después del prompt ya que la entrada se simula como si fuera de un usuario. Esto permite además que los valores arriba en cada inciso sean los que debe obtener.
    """)
    return


@app.cell
def _():
    # Ejercicio 4.10: Creación y procesamiento de lista con entradas de usuario
    # No tocar las dos líneas de código abajo
    from siminput import sim_input

    input = sim_input("numeros.dat")

    # A partir de aquí su código para el ejercicio
    # Utilice input() como es usual

    return


if __name__ == "__main__":
    app.run()

---
colors: five
fonts: four

[comment]: <> (Slides made with https://play.presenta.cc/edit/)
---

# Pong game
### With pure Python 3

---

# Our tools:

* GitHub
* VSCode
* Python 3
* `pong.py`
* Documentación (`pdoc`)

---

# The exercise:

### Crearemos un juego Pong paso a paso

&nbsp;

---

# The exercise:

### Crearemos un juego Pong paso a paso

Empezamos descargando el proyecto de [GitHub](https://github.com/LECbg/pong-challenge).
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;

---

# The exercise:

### Crearemos un juego Pong paso a paso

Empezamos descargando el proyecto de [GitHub](https://github.com/LECbg/pong-challenge).

### ¡Ya es nuestro!

Lo primero siempre es abrir el archivo `README.md`.
&nbsp;
&nbsp;
&nbsp;
&nbsp;

---

# The exercise:

### Crearemos un juego Pong paso a paso

Empezamos descargando el proyecto de [GitHub](https://github.com/LECbg/pong-challenge).

### ¡Ya es nuestro!

Lo primero siempre es abrir el archivo `README.md`.

### ¡Entorno listo!

Ya podemos abrir el archivo <high>step 1.py</high>.

**NO abrir** cada <high>step N.py</high> hasta haber completado el anterior!

---

# no me hagáis trampas

---

# Step 1 - Python basics

* `import`, módulo
* `field`, variable
* `GameField`, clase
* instancia de clase
* `while`
* `True`/`False`, booleanos
* `field.update()`

---


# Step 1 - Summary

En resumen: en este paso **se crea** un campo de juego (**la ventana** donde se verá el juego).

El contenido de **la pantalla se refresca** cada vez que el bucle se repite (y se repite **infinitamente**).

Tenemos **dos objetos** **que podemos usar** en sucesivos pasos: **`pong` y `field`**.

---

# Step 2 - Add stuff

### Seguid las instrucciones en los comentarios que empiezan por `##`

---

# Step 2 - Add stuff

### Seguid las instrucciones en los comentarios que empiezan por `##`

<ins>Cada vez que "llamamos" a una clase, creamos un objeto:</ins>

```python
field = pong.GameField(title="Celti-Pong")
paddle_a = pong.Paddle()
paddle_b = pong.Paddle()
ball = pong.Ball()
```
<ins>Que se guarda en las diferentes variables:</ins>
`field`, `paddle_a`, `paddle_b`, `ball`.

---

# Step 2 - Add stuff

### Seguid las instrucciones en los comentarios que empiezan por `##`

<ins>Luego podemos usar esas variables:</ins>

```python
paddle_a.draw(left=True)
paddle_b.draw(left=False)
ball.draw()
field.update()
```
Nos permitirán usar los métodos y atributos contenidos en esos objetos, como son `draw` y `update`.

---

# Step 2 - Add stuff

### ¿Os habéis fijado en que la llamada a `GameField` ha camibiado?

## `GameField(title="Celti-Pong")`
* `title` es el nombre del parámetro.
* `"Celti-Pong"` es un **string**, una cadena de texto.

Los strings **siempre** deben ir entre comillas dobles.

---

# Step 3 - Moving paddles

> `class Paddle`
* `draw(left=True)`
* `up()`
* `down()`
* `link_keys(game_field, up="Up", down="Down")`

---

# Step 4 - Ball bouncing

### `if` - `else`

```python
if condition:
    # Runs when condition is True
else:
    # Runs otherwise
```

### `if` - `elif`

```python
if condition1:
    # Runs when condition1 is True
elif condition2:
    # Runs when condition1 is False and condition2 is True
```

## ¡La indentación es importante!

---

# Step 4 - Ball bouncing

> `class Ball`
* `reaches_top_end()` &rarr; `bool` (`True`/`False`)
* `bounce_down()`
* `reaches_bottom_end()` &rarr; `bool`
* `bounce_up()`

---

# Step 5 - Restart ball

> `class Ball`
* `reaches_right_end()` &rarr; `bool`
* `reaches_left_end()` &rarr; `bool`
* `start_again()`

---

# Step 6 - Boolean operators

* **`not`**
    **`not`**` True` &rarr; `False`
    **`not`**` False` &rarr; `True`
* **`and`**
    `True `**`and`**` True` &rarr; `True`
    `True `**`and`**` False` &rarr; `False`
    `False `**`and`**` False` &rarr; `False`
* **`or`**
    `True `**`or`**` True` &rarr; `True`
    `True `**`or`**` False` &rarr; `True`
    `False `**`or`**` False` &rarr; `False`

---

# Step 6 - Paddle and ball collide

> `class Ball`
* `touches_paddle(paddle)` &rarr; `bool`
* `flip_horizontally()`

---

# After step 6...
# It works!

---

# But lets make it cooler...

---

# Step 7 - Scores

> <high>DIY</high>

---

# Step 8 - Increase scores

* `score.a_gets_point()`
  Incrementa en 1 la puntuación de A
* `score.update_board()`
  Refresca el contenido pintado en el marcador.
&nbsp;
&nbsp;
&nbsp;

---

# Step 8 - Increase scores

* `score.a_gets_point()`
  Incrementa en 1 la puntuación de A
* `score.b_gets_point()`
  Incrementa en 1 la puntuación de B
* `score.update_board()`
  Refresca el contenido pintado en el marcador.

---

# Step 8
# Hard mode on

---

# Step 8
# Hard mode on
### What's this mystical magic?!

---

# It's not magic,
# it's parameters

---

# Step 9 - Let there be sound
&nbsp;

---

# Step 9 - Let there be sound

* Crear un objeto sonido
* La bola suena al rebotar
&nbsp;
&nbsp;

---

# Step 9 - Let there be sound

* Crear un objeto sonido
* La bola suena al rebotar
* La bola rebota contra los márgenes superior e inferior y contra las palas.

---

# Step 10 - And there was sound

* Identificad esas posiciones y reproducid el sonido.

---

# Step 11 - Parameters

* Buscad en la <mark>documentación</mark> cómo poner vuestros nombres en el marcador.

---

# It's alive!

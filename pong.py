import turtle

global FIELD_WIDTH
global FIELD_HEIGHT


class GameField:
    """Crea un campo de juego (una ventana)."""

    def __init__(self, title="Pong by Laura", color="black", width=800, height=600):
        """Se pueden modificar el título, el color de fondo, el ancho y la altura."""
        global FIELD_WIDTH, FIELD_HEIGHT
        FIELD_WIDTH, FIELD_HEIGHT = width, height

        self.screen = turtle.Screen()
        self.screen.title(title)
        self.screen.bgcolor(color)
        self.screen.setup(width=width, height=height)
        self.screen.tracer(0)

    def update(self):
        """Refresca el contenido pintado en la ventana."""
        self.screen.update()


class Paddle:
    """Crea una pala del juego (la barra vertical)."""

    def __init__(self, delta=20):
        """Con `delta` controlamos las unidades que avanza la pala con cada
        pulsación de tecla."""
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.step = delta

    def draw(self, shape="square", color="white", left=True):
        """Dibuja el objeto en la ventana.
        Podemos cambiar la forma, el color e indicar si está a la izquierda o a
        la derecha."""
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.penup()
        x = FIELD_WIDTH//2-50
        if left:
            x = -x
        self.turtle.goto(x, 0)

    def up(self):
        """Mueve la pala hacia arriba `delta` unidades."""
        y = self.turtle.ycor() + self.step
        self.turtle.sety(y)

    def down(self):
        """Mueve la pala hacia abajo `delta` unidades."""
        y = self.turtle.ycor() - self.step
        self.turtle.sety(y)

    def link_keys(self, game_field, up="Up", down="Down"):
        """Vincular las teclas especificadas en `up` y `down` con sus
        respectivos movimientos."""
        screen = game_field.screen
        screen.listen()
        # Keyboard bindings
        screen.onkeypress(self.up, up)
        screen.onkeypress(self.down, down)


class Ball:
    """Crea la bola del juego"""
    def __init__(self, delta_x=2, delta_y=2):
        """Con `delta_x` y `delta_y` controlamos las unidades que avanza la
        bola cada vez que se llama a `move` en los ejes x e y."""
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        # The distance the ball will move each step
        self.dx = delta_x
        self.dy = delta_y

    def draw(self, shape="square", color="white"):
        """Dibuja el objeto en la ventana.
        Podemos cambiar la forma y el color."""
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(0, 0)

    # Movement
    def move(self, distance_x=None, distance_y=None):
        """Mueve la bola. Por defecto usa los valores `delta`, pero se pueden
        especificar otros."""
        dx = self.dx if distance_x is None else distance_x
        dy = self.dy if distance_y is None else distance_y
        self.turtle.setx(self.turtle.xcor() + dx)
        self.turtle.sety(self.turtle.ycor() + dy)

    def flip_vertically(self):
        """Se invierte la dirección vertical del movimiento (eje y)."""
        self.dy *= -1

    def flip_horizontally(self):
        """Se invierte la dirección horizontal del movimiento (eje x)."""
        self.dx *= -1

    # Border checking
    def reaches_top_end(self) -> bool:
        """Devuelve un booleano que indica si la bola ha llegado al borde superior."""
        return self.turtle.ycor() > FIELD_HEIGHT//2-10

    def reaches_bottom_end(self) -> bool:
        """Devuelve un booleano que indica si la bola ha llegado al borde inferior."""
        return self.turtle.ycor() < -(FIELD_HEIGHT//2-10)

    def reaches_right_end(self) -> bool:
        """Devuelve un booleano que indica si la bola ha llegado al borde derecho."""
        return self.turtle.xcor() > FIELD_WIDTH//2-50

    def reaches_left_end(self) -> bool:
        """Devuelve un booleano que indica si la bola ha llegado al borde izquierdo."""
        return self.turtle.xcor() < -(FIELD_WIDTH//2-50)

    # Border bouncing
    def bounce_down(self):
        """Hace rebotar la bola con el borde inferior."""
        self.turtle.sety(FIELD_HEIGHT//2-10)
        self.dy *= -1

    def bounce_up(self):
        """Hace rebotar la bola con el borde superior."""
        self.turtle.sety(-(FIELD_HEIGHT//2-10))
        self.flip_vertically()

    # To start over when the ball reaches left & right borders
    def start_again(self):
        """Reinicia el movimiento de la bola desde el centro de la pantalla y
        en sentido horizontal inverso."""
        self.turtle.goto(0, 0)
        self.dx *= -1

    # Paddle checking
    def touches_paddle(self, paddle) -> bool:
        """Devuelve un booleano que indica si la bola ha tocado la pala `paddle`."""
        b = self.turtle
        p = paddle.turtle
        if p.xcor() < 0:
            # Left paddle
            return b.xcor() < -(FIELD_WIDTH//2-60) and b.ycor() < p.ycor() + 50 and b.ycor() > p.ycor() - 50

        # Right paddle
        return b.xcor() > FIELD_WIDTH//2-60 and b.ycor() < p.ycor() + 50 and b.ycor() > p.ycor() - 50


class ScoreBoard:
    """Crea un marcador."""
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.score_a = 0
        self.score_b = 0

    def draw(self, name_a="Player A", name_b="Player B"):
        """Dibuja el objeto en la ventana.
        Podemos cambiar los nombres de los jugadores."""
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(0, 260)
        self.name_a = name_a
        self.name_b = name_b
        self.update_board()

    def update_board(self):
        """Refresca el contenido pintado en el marcador."""
        self.turtle.clear()
        player_a = f"{self.name_a}: {self.score_a:02}".ljust(20, ' ')
        player_b = f"{self.name_b}: {self.score_b:02}".rjust(20, ' ')
        self.turtle.write(f"{player_a} vs {player_b}",
                          align="center", font=("Courier", 24, "normal"))

    def set_score(self, a=0, b=0):
        """Reiniciar los marcadores. Pueden otorgarse puntuaciones específicas."""
        self.score_a = a
        self.score_b = b
        self.update_score()

    def a_gets_point(self):
        """Sumar un punto al jugador A."""
        self.score_a += 1

    def b_gets_point(self):
        """Sumar un punto al jugador B."""
        self.score_b += 1


class Sound:
    """Crea un sonido que poder reproducir."""
    def __init__(self, file="bounce.wav"):
        """Se puede indicar un nombre de archivo relativo a la carpeta
        `sound_files`."""
        self.file_path = f"sound_files/{file}"

        from sys import platform

        if platform.startswith("linux"):
            # Linux
            import os
            self.system_call = lambda file: os.system(f"aplay {file}&")
        elif platform == "darwin":
            # OS X
            import os
            self.system_call = lambda file: os.system(f"afplay {file}&")
        elif platform == "win32":
            # Windows
            import winsound
            self.system_call = lambda file: winsound.PlaySound(file, winsound.SND_ASYNC)

    def play(self):
        """Reproduce el sonido."""
        self.system_call(self.file_path)

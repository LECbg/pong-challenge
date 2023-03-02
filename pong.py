import turtle

global FIELD_WIDTH
global FIELD_HEIGHT


class GameField:
    def __init__(self, title="Pong by Laura", color="black", width=800, height=600):
        global FIELD_WIDTH, FIELD_HEIGHT
        FIELD_WIDTH, FIELD_HEIGHT = width, height

        self.screen = turtle.Screen()
        self.screen.title(title)
        self.screen.bgcolor(color)
        self.screen.setup(width=width, height=height)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()


class Paddle:
    def __init__(self, delta=20):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.step = delta

    def draw(self, shape="square", color="white", left=True):
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.turtle.penup()
        x = FIELD_WIDTH//2-50
        if left:
            x = -x
        self.turtle.goto(x, 0)

    def up(self):
        y = self.turtle.ycor() + self.step
        self.turtle.sety(y)

    def down(self):
        y = self.turtle.ycor() - self.step
        self.turtle.sety(y)

    def link_keys(self, game_field, up="Up", down="Down"):
        screen = game_field.screen
        screen.listen()
        # Keyboard bindings
        screen.onkeypress(self.up, up)
        screen.onkeypress(self.down, down)


class Ball:
    def __init__(self, delta_x=2, delta_y=2):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        # The distance the ball will move each step
        self.dx = delta_x
        self.dy = delta_y

    def draw(self, shape="square", color="white"):
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(0, 0)

    # Movement
    def move(self, distance_x=None, distance_y=None):
        dx = self.dx if distance_x is None else distance_x
        dy = self.dy if distance_y is None else distance_y
        self.turtle.setx(self.turtle.xcor() + dx)
        self.turtle.sety(self.turtle.ycor() + dy)

    def flip_vertically(self):
        self.dy *= -1

    def flip_horizontally(self):
        self.dx *= -1

    # Border checking
    def reaches_top_end(self):
        return self.turtle.ycor() > FIELD_HEIGHT//2-10

    def reaches_bottom_end(self):
        return self.turtle.ycor() < -(FIELD_HEIGHT//2-10)

    def reaches_right_end(self):
        return self.turtle.xcor() > FIELD_WIDTH//2-50

    def reaches_left_end(self):
        return self.turtle.xcor() < -(FIELD_WIDTH//2-50)

    # Border bouncing
    def bounce_down(self):
        self.turtle.sety(FIELD_HEIGHT//2-10)
        self.dy *= -1

    def bounce_up(self):
        self.turtle.sety(-(FIELD_HEIGHT//2-10))
        self.flip_vertically()

    # To start over when the ball reaches left & right borders
    def start_again(self):
        self.turtle.goto(0, 0)
        self.dx *= -1

    # Paddle checking
    def touches_paddle(self, paddle):
        b = self.turtle
        p = paddle.turtle
        if p.xcor() < 0:
            # Left paddle
            return b.xcor() < -(FIELD_WIDTH//2-60) and b.ycor() < p.ycor() + 50 and b.ycor() > p.ycor() - 50

        # Right paddle
        return b.xcor() > FIELD_WIDTH//2-60 and b.ycor() < p.ycor() + 50 and b.ycor() > p.ycor() - 50


class ScoreBoard:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.score_a = 0
        self.score_b = 0

    def draw(self, name_a="Player A", name_b="Player B"):
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(0, 260)
        self.name_a = name_a
        self.name_b = name_b
        self.update_board()

    def update_board(self):
        self.turtle.clear()
        player_a = f"{self.name_a}: {self.score_a:02}".ljust(20, ' ')
        player_b = f"{self.name_b}: {self.score_b:02}".rjust(20, ' ')
        self.turtle.write(f"{player_a} vs {player_b}",
                          align="center", font=("Courier", 24, "normal"))

    def set_score(self, a=0, b=0):
        self.score_a = a
        self.score_b = b
        self.update_score()

    def a_gets_point(self):
        self.score_a += 1

    def b_gets_point(self):
        self.score_b += 1


class Sound:
    def __init__(self, file="bounce.wav"):
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
        self.system_call(self.file_path)

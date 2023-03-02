import pong

field = pong.GameField(title="Celti-Pong")

# Create paddles and ball
paddle_a = pong.Paddle()
paddle_a.draw(left=True)
paddle_b = pong.Paddle()
paddle_b.draw(left=False)
ball = pong.Ball()
ball.draw()

# Enable moving paddles
paddle_a.link_keys(field, "w", "s")
## Enable moving paddle_b
## Use "Up" and "Down" keys

while True:
    field.update()

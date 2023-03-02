import pong

field = pong.GameField(title="Celti-Pong")

# Create paddles and ball
paddle_a = pong.Paddle()
paddle_a.draw(left=True)
## Add paddle_b
ball = pong.Ball()
## Anything else?

while True:
    field.update()

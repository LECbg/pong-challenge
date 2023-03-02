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
paddle_b.link_keys(field, "Up", "Down")

while True:
    field.update()

    # Move the ball
    ball.move()

    # --- Border checking ---

    # Top and bottom
    if ball.reaches_top_end():
        ball.bounce_down()

    elif ball.reaches_bottom_end():
        ball.bounce_up()

    # Left and right
    if ball.reaches_right_end():
        ball.start_again()

    ## Add left end check

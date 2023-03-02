## Play the sound with sound.play()

import pong

field = pong.GameField(title="Celti-Pong")
score = pong.ScoreBoard()
score.draw()

# Create paddles and ball
paddle_a = pong.Paddle(30)
paddle_a.draw(left=True)
paddle_b = pong.Paddle(30)
paddle_b.draw(left=False)
ball = pong.Ball(4, 4)
ball.draw()

# Enable moving paddles
paddle_a.link_keys(field, "w", "s")
paddle_b.link_keys(field, "Up", "Down")

# Add sound to the ball
sound = pong.Sound()

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
        score.a_gets_point()
        score.update_board()
        ball.start_again()

    elif ball.reaches_left_end():
        score.b_gets_point()
        score.update_board()
        ball.start_again()

    # -- Paddle and ball collisions --

    if ball.touches_paddle(paddle_a) or ball.touches_paddle(paddle_b):
        ball.flip_horizontally()

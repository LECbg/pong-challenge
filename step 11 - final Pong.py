#############################
#   🏓 Super Pong Game! 🏓  #
#       © by Laura          #
#############################

import pong

field = pong.GameField(title="Celti-Pong")
score = pong.ScoreBoard()
score.draw(name_a="Laura", name_b="Puche")

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

# Add sounds
ball_sound = pong.Sound()
point_sound = pong.Sound("win.wav")

while True:
    field.update()

    # Move the ball
    ball.move()

    # --- Border checking ---

    # Top and bottom
    if ball.reaches_top_end():
        ball.bounce_down()
        ball_sound.play()

    elif ball.reaches_bottom_end():
        ball.bounce_up()
        ball_sound.play()

    # Left and right
    if ball.reaches_right_end():
        score.a_gets_point()
        score.update_board()
        ball.start_again()
        point_sound.play()

    elif ball.reaches_left_end():
        score.b_gets_point()
        score.update_board()
        ball.start_again()
        point_sound.play()

    # -- Paddle and ball collisions --

    if ball.touches_paddle(paddle_a) or ball.touches_paddle(paddle_b):
        ball.flip_horizontally()
        ball_sound.play()

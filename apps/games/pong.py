import time
import curses

def pong():
    # Completely Vibe Coded. Couldnt be asked to code this
    WIDTH = 60
    HEIGHT = 20
    PADDLE_SIZE = 4

    def game(stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.timeout(20)

        left_y = HEIGHT // 2 - PADDLE_SIZE // 2
        right_y = HEIGHT // 2 - PADDLE_SIZE // 2

        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        dx = 1
        dy = 1

        left_score = 0
        right_score = 0

        while True:
            key = stdscr.getch()

            # Controls
            if key == ord("w") and left_y > 2:
                left_y -= 1
            elif key == ord("s") and left_y < HEIGHT - PADDLE_SIZE:
                left_y += 1
            elif key == ord("q"):
                break
            # Simple AI
            ai_center = right_y + PADDLE_SIZE // 2

            if ball_y < ai_center and right_y > 2:
                right_y -= 1
            elif ball_y > ai_center and right_y < HEIGHT - PADDLE_SIZE:
                right_y += 1

            # Move ball
            ball_x += dx
            ball_y += dy

            # Bounce off top/bottom
            if ball_y <= 2 or ball_y >= HEIGHT - 1:
                dy *= -1

            # Left paddle collision / score
            if ball_x == 2:
                if left_y <= ball_y < left_y + PADDLE_SIZE:
                    dx *= -1
                else:
                    right_score += 1
                    ball_x = WIDTH // 2
                    ball_y = HEIGHT // 2
                    dx = 1

            # Right paddle collision / score
            if ball_x == WIDTH - 3:
                if right_y <= ball_y < right_y + PADDLE_SIZE:
                    dx *= -1
                else:
                    left_score += 1
                    ball_x = WIDTH // 2
                    ball_y = HEIGHT // 2
                    dx = -1

            # Draw
            stdscr.clear()
            stdscr.addstr(
                0, 0,
                f"Left: {left_score}  Right: {right_score}   W/S to go up and down  Q=Quit"
            )

            # Top & bottom borders
            for x in range(WIDTH):
                stdscr.addch(1, x, "-")
                stdscr.addch(HEIGHT, x, "-")

            # Paddles
            for i in range(PADDLE_SIZE):
                stdscr.addch(left_y + i, 1, "|")
                stdscr.addch(right_y + i, WIDTH - 2, "|")

            # Ball
            stdscr.addch(ball_y, ball_x, "O")

            stdscr.refresh()
            time.sleep(0.02)

    curses.wrapper(game)
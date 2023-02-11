import time

import pygame

pygame.init()
WIDTH = 700
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("StopWatch")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont("comicsans", 60)
window.fill(WHITE)

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE

    def draw_button(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, 100, 50))

    def write_text(self, text, x, y):
        text = pygame.font.SysFont("comicsans", 40).render(text, True, BLACK)
        window.blit(text, (x, y))


def timer(hour: int, min: int, sec: int):
    if sec < 10:
        sec = f"0{sec}"

    if min < 10:
        min = f"0{min}"

    if hour < 10:
        hour = f"0{hour}"

    time = FONT.render(f"{hour}:{min}:{sec}", True, BLACK)

    window.blit(time, (100, 100))


def main():
    run = True
    hour = min = sec = 0
    timer(hour, min, sec)
    startBtn = Button(200, 250)
    startPos = [[i for i in range(200, 301)], [i for i in range(250, 301)]]
    startBtn.draw_button()
    startBtn.write_text("Start", 200, 240)
    isRunning = False

    while run:
        pygame.display.update()
        if isRunning:
            sec += 1

            if sec == 60:
                sec = 0
                min += 1

            if min == 60:
                min = 0
                hour += 1

            if hour == 24:
                hour = 0

            time.sleep(1)
            window.fill(WHITE)
            startBtn.draw_button()
            startBtn.write_text("Stop", 200, 240)
            timer(hour, min, sec)

        else:
            window.fill(WHITE)
            startBtn.draw_button()
            startBtn.write_text("Start", 200, 240)
            timer(0, 0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] in startPos[0] and pos[1] in startPos[1]:
                    isRunning = True


    pygame.quit()

if __name__ == '__main__':
    main()
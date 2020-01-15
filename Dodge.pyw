import pygame
from random import *
import os
import sys

os.environ['SDL_VIDEO_WINDOW_POS'] = "325, 120"

pygame.init()
crash_sound = pygame.mixer.Sound("Crash.wav")
music = pygame.mixer.music.load("Theme.wav")
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 200, 0)
light_green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dodge")
clock = pygame.time.Clock()
carimage = pygame.image.load('car1.png')
carimage2 = pygame.image.load("carimage.png")
pygame.display.set_icon(carimage2)


def blocks_dodged(count):
    font = pygame.font.SysFont("Comic Sans MS", 30)
    text = font.render("Dodged: " + str(count), True, black)
    gamedisplay.blit(text, (0, 0))


def blocks(x, y):
    block = pygame.image.load("block1.png")
    gamedisplay.blit(block, (x, y))


def car(x, y):
    gamedisplay.blit(carimage, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont("Comic Sans MS", 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), 280)
    gamedisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    while crash:
        message_display("Crashed")
        pygame.draw.rect(gamedisplay, green, (250, 400, 100, 50))
        pygame.draw.rect(gamedisplay, red, (450, 400, 100, 50))
        text = pygame.font.SysFont("Comic Sans MS", 15)
        text_show = text.render("Play Again", True, black)
        text2 = pygame.font.SysFont("Comic Sans MS", 15)
        text_show2 = text2.render("Quit", True, black)
        gamedisplay.blit(text_show2, (482, 420))
        gamedisplay.blit(text_show, (260, 420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 350 > mouse[0] > 250 and 450 > mouse[1] > 400:
            pygame.draw.rect(gamedisplay, light_green, (250, 400, 100, 50))
            text = pygame.font.SysFont("Comic Sans MS", 15)
            text_show = text.render("Play Again", True, black)
            gamedisplay.blit(text_show, (260, 420))
            if click[0] == 1:
                game_loop()
        if 550 > mouse[0] > 450 and 450 > mouse[1] > 400:
            pygame.draw.rect(gamedisplay, light_red, (450, 400, 100, 50))
            text2 = pygame.font.SysFont("Comic Sans MS", 15)
            text_show2 = text2.render("Quit", True, black)
            gamedisplay.blit(text_show2, (482, 420))
            if click[0] == 1:
                pygame.quit()
                sys.exit()


def introduction():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gamedisplay.fill(white)
        text = pygame.font.SysFont("Comic Sans MS", 70)
        text2 = text.render("Dodge", True, black)
        gamedisplay.blit(text2, (300, 200))
        text = pygame.font.SysFont("Comic Sans MS", 20)
        text2 = text.render("A game by Mohamed Emad", True, black)
        gamedisplay.blit(text2, (280, 295))

        pygame.draw.rect(gamedisplay, green, (250, 400, 100, 50))
        pygame.draw.rect(gamedisplay, red, (450, 400, 100, 50))

        text = pygame.font.SysFont("Comic Sans MS", 15)
        text2 = text.render("Play Now", True, black)
        gamedisplay.blit(text2, (268, 420))
        text3 = pygame.font.SysFont("Comic Sans MS", 15)
        text4 = text3.render("Quit", True, black)
        gamedisplay.blit(text4, (485, 420))

        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 350 > mouse[0] > 250 and 450 > mouse[1] > 400:
            pygame.draw.rect(gamedisplay, light_green, (250, 400, 100, 50))
            gamedisplay.blit(text2, (268, 420))
            pygame.display.update()
            clock.tick(60)
            if click[0] == 1:
                intro = False
        else:
            pass

        if 550 > mouse[0] > 450 and 450 > mouse[1] > 400:
            pygame.draw.rect(gamedisplay, light_red, (450, 400, 100, 50))
            gamedisplay.blit(text4, (485, 420))
            pygame.display.update()
            clock.tick(60)
            if click[0] == 1:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def game_loop():
    pygame.mixer.music.play(-1)
    x = 350
    y = 380
    x_change = 0
    y_change = 0
    game_exit = False
    block_startx = randrange(0, display_width)
    block_starty = -600
    block_speed = 7
    block_width = 111
    block_height = 95
    dodged = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_UP:
                    y_change = -5

                if event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        pygame.display.update()
        clock.tick(60)
        gamedisplay.fill(white)
        blocks(block_startx, block_starty)
        block_starty += block_speed
        blocks_dodged(dodged)

        if block_starty >= display_height:
            block_starty = -100
            block_startx = randrange(0, display_width)
            dodged += 1
            block_speed += 0.1

        x += x_change
        y += y_change

        if 700 < x or x < 0:
            x -= x_change
        if y > 415 or y < 0:
            y -= y_change
        if block_height + block_starty > y > block_starty:
            if block_startx < x < block_startx + block_width or x + 120 > block_startx and 120 + x < block_startx + block_width and x + 120 > block_startx:
                crash()

        car(x, y)
        font = pygame.font.SysFont("Comic Sans MS", 25)
        text = font.render("Designed by Mohamed Emad", True, black)
        gamedisplay.blit(text, (450, 10))


introduction()
game_loop()
pygame.quit()
sys.exit()

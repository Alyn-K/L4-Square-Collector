import sys

import pygame
from pygame.locals import *

from coin import Coin

pygame.display.init()
screen = pygame.display.set_mode((800, 600))

pygame.font.init()
font = pygame.font.SysFont("freeserif", 32)

# colors
black = pygame.Color(0, 0, 0, 255)
white = pygame.Color(255, 255, 255)
yellow = pygame.Color(230, 182, 76)

# player
player = pygame.Rect(400, 300, 12, 12)

game_over = False

score = 0

x_speed = 0
y_speed = 0

# player movement
def move_up():
  global y_speed
  y_speed = 1

def move_down():
  global y_speed
  y_speed = -1

def move_left():
  global x_speed
  x_speed = -1

def move_right():
  global x_speed
  x_speed = 1


def movement_loop():
  global x_speed, y_speed, player
  player.centerx += x_speed
  player.centery -= y_speed

  x_speed = 0
  y_speed = 0


# spawn coins
coins = []

for i in range(100):
  coins.append(Coin())

def render_coins(screen):
  for coin in coins:
    if not coin.isHidden:
      screen.fill(yellow, coin.rect)

def collision():
  global score, game_over, player

  for coin in coins:
    
    if player.colliderect(coin.rect) and not coin.isHidden:
      coin.isHidden = True
      score += 1

      if score == 100:
        game_over = True


def main():
  global game_over, score

  while not game_over:

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    pygame.event.pump()
    key = pygame.key.get_pressed()

    if key[K_UP]:
      move_up()
    if key[K_DOWN]:
      move_down()
    if key[K_LEFT]:
      move_left()
    if key[K_RIGHT]:
      move_right()

    movement_loop()

    collision()
    
    screen.fill(black)
    screen.fill(white, player)

    render_coins(screen)

    screen.blit(font.render("Score: ", True, white), (20, 80))

    pygame.display.flip()


main()
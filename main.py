# importing pygame
import pygame

pygame.init()

def main():

  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption('Space Invaders')
  player = pygame.image.load('spaceInvadersSprite.png')
  alien = pygame.image.load('spaceInvadersAlien.png')
  bullet = pygame.image.load('spaceInvadersBullet.png')
  transparent = (0, 0, 0, 0)

  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))

  x, y = 320, 430
  alienX, alienY = 320, 0
  bulletX, bulletY = x + 25, y + 1

  screen.blit(player, (x, y))
  screen.blit(alien, (alienX, alienY))

  while 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and x >= 0:
          x -= 50
          bulletX -= 50
        elif event.key == pygame.K_RIGHT and x <= 590:
          x += 50
          bulletX += 50
        elif event.key == pygame.K_SPACE:
          
          screen.blit(bullet, (bulletX, bulletY))
          for i in range(10):
            bulletY -= 70
            screen.blit(bullet, (bulletX, bulletY))
            pygame.display.update()
            for j in range(alienX, alienX + 50):
              for k in range(alienY, alienY + 50):
                if bulletX == j and bulletY == k:
                  alien = pygame.image.load("blank.png")
            pygame.time.delay(10)
          bulletY = y + 1
          
    screen.blit(background, (0, 0))
    screen.blit(player, (x, y))
    screen.blit(alien, (alienX, alienY))
    pygame.display.update()

if __name__ == '__main__' : main()

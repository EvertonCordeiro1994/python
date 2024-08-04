import pygame


pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("exercicio021.mp3")

pygame.mixer.music.play(loops=0) 


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

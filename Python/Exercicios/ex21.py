import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('E:\Prog\Python\Exercicios\simples.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
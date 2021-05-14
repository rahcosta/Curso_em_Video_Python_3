# FAÇA UM PROGRAMA QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3.

import pygame
pygame.init() #inicia o pygame

pygame.mixer.music.load('Cavaleiros(1).mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
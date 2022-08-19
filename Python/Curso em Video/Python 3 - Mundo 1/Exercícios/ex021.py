# Título:       Exercício 21 – Tocando um MP3
# Desafio:      021
# Requisito:    Aula 08
# Enunciado:    Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

print('====== EXERCÍCIO 021 ======')
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

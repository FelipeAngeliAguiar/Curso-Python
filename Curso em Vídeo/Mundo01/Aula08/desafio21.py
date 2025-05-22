#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import os
os.chdir(os.path.dirname(__file__))

import pygame
pygame.init()
pygame.mixer.music.load('Notion.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
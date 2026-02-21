"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

titulo = 'MP3'
print(f'{titulo:=^70}')

import pygame

pygame.mixer.init()  # Inicializa o sistema de áudio
pygame.mixer.music.load('./audio_exemplo.mp3')  # Carrega o arquivo MP3
pygame.mixer.music.play()  # Inicia a reprodução

input('Pressione Enter para encerrar...')  # Mantém o programa ativo até o usuário encerrar

# O pygame.mixer.init() também permite configurar o sistema de áudio antes de carregar o MP3.
# Exemplo:
# pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m².
"""

h = float(input('Qual é a altura de sua parede? '))
l = float(input('Qual é a largura de sua parede? '))
print(f'Sua parede possui {h*l} m² de área. Logo, considerando que cada litro litro de tinta pinta 2 m², você irá gastar {h*l/2} litros')

import csv
import sys

import pygame

file = open("data/mnist_test.csv", "r")
data = list(csv.reader(file))

k = 1
tile_size = int(sys.argv[1])

screen = pygame.display.set_mode((28 * tile_size, 28 * tile_size), pygame.RESIZABLE)
run = True
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            k += 1
        if pygame.mouse.get_pressed()[2]:
            k -= 1
        if pygame.key.get_pressed() and event.type == pygame.K_SPACE:
            pass

    u = 0
    for i in range(28):
        for j in range(28):
            if k != 0:
                pygame.draw.rect(
                    screen,
                    (int(data[k][u]), int(data[k][u]), int(data[k][u])),
                    ((j * tile_size), (i * tile_size), tile_size, tile_size),
                )
                u += 1
            else:
                pygame.draw.rect(
                    screen, (0, 0, 0), (0, 0, 28 * tile_size, 28 * tile_size)
                )

    pygame.display.update()

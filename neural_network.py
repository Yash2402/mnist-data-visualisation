import csv

import numpy as np
import pygame


class NeuralNetwork:
    def __init__(
        self,
        setup,
        TrainingData: list,
        TestingData: list,
        weight1,
        weight2,
        bias1,
        bias2,
    ):
        self.setup = setup
        self.TrainingData = TrainingData
        self.TestingData = TestingData
        self.node1 = np.zeros((785, 1))
        self.node2 = np.zeros((20, 1))
        self.node3 = np.zeros((10, 1))
        self.weight1 = weight1
        self.weight2 = weight2
        self.bias1 = bias1
        self.bias2 = bias2

    # @staticmethod
    # def sigmoid():

    def train(self):
        for i in range(1, len(self.TrainingData)):
            for j in range(785):
                self.node1[j] = self.TrainingData[i][j]


setup = [785, 20, 10]
file = open("data/mnist_test.csv", "r")
data = list(csv.reader(file))

weight1 = np.random.uniform(-0.5, 0.5, (20, 785))
weight2 = np.random.uniform(-0.5, 0.5, (10, 20))
bias1 = np.zeros((20, 1))
bias2 = np.zeros((10, 1))
nn = NeuralNetwork(setup, data[:100], data[100:200], weight1, weight2, bias1, bias2)

k = 1
tile_size = 20
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
    nn.train()
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

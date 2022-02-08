# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:13:47 2020

@author: genaf
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def game(m,n,start,iterations):
    board = np.ones([m,n])

    for i in start:
        board[i[0]][i[1]] = float(0)

    plt.imshow(board,interpolation = "nearest", cmap=cm.Greys_r)                        # Displays matrix with floating points as a white square for 1. and a black square for 0.
    plt.ion()
    plt.show()
    blackSq = start
    n = 0

    while True:
        n = n + 1
        plt.pause(.01)

        potential = []
        nextIterB = []
        nextIterW = []

        for bs in blackSq:
            for i in  range(3):
                for j in range(3):
                    potential.append([bs[0] + i - 1, bs[1] + j - 1])

        potential = np.unique(potential, axis = 0)

        for square in potential:
            check = 0

            if board[square[0]][square[1]] == 1.:
                for i in range(3):
                    for j in range(3):
                        check += board[square[0] + i - 1][square[1] + j -1]
                if check == 6.:
                    nextIterB.append([square[0],square[1]])

            else:
                for i in range(3):
                    for j in range(3):
                        check += board[square[0] + i - 1][square[1] + j -1]
                if check != 6. and check != 5.:
                    nextIterW.append([square[0],square[1]])

        for changeSq in nextIterW:
            board[changeSq[0]][changeSq[1]] = 1.
        for changeSq in nextIterB:
            board[changeSq[0]][changeSq[1]] = 0.

        plt.cla()
        plt.imshow(board,interpolation = "nearest", cmap=cm.Greys_r)
        plt.draw()

        for oldSq in blackSq:
            if board[oldSq[0]][oldSq[1]] == 0.:
                nextIterB.append(oldSq)

        nextIterB = np.array(nextIterB)
        nextIterB = np.unique(nextIterB, axis = 0)
        blackSq = nextIterB
        
        if n > iterations:
            break
    

#

glider = [[1,2],[2,3],[3,1],[3,2],[3,3]]

gliderGun = [[6,2],[6,3],[7,2],[7,3],[6,12],[7,12],[8,12],[5,13],[4,14],[4,15],[9,13],[10,14],[10,15],[7,16],[7,18],[6,18],[8,18],[5,17],[9,17],[7,19],[6,22],[5,22],[4,22],[6,23],[5,23],[4,23], \
             [3,24],[7,24],[7,26],[8,26],[3,26],[2,26],[4,36],[5,36],[4,37],[5,37]]
    
#

game(100,100,gliderGun, 2000)
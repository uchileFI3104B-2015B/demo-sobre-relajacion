#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Descripcion
'''

from __future__ import division
import numpy as np

def muestra_phi(phi):
    print(phi[::-1,:])

def q(i, j, h):
    x = i * h -1
    y = j * h -1
    return 2 * (2 - x**2 - y**2)

def una_iteracion(phi, N_pasos, h, w=1.):
    for i in range(1, N_pasos-1):
        for j in range(1, N_pasos-1):
            phi[i, j] = (1 - w) * phi[i, j] + w / 4 * (phi[i+1,j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1] + h**2 * q(i, j, h))

# Main

# Setup

Lx = Ly = 2
N_pasos = 5
h = Lx / (N_pasos -1)

phi = np.zeros((N_pasos, N_pasos))

# iteracion
una_iteracion(phi, N_pasos, h, w=1.)

muestra_phi(phi)




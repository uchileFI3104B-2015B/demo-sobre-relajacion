#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Descripcion
'''

import numpy as np

def muestra_phi(phi):
    print(phi[::-1,:])


# Main

# Setup

Lx = Ly = 2
N_pasos = 5
h = Lx / (N_pasos -1)

phi = np.zeros((N_pasos, N_pasos))

phi[0,0] =1
muestra_phi(phi)


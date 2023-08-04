#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:17:53 2023

@author: nebiyousamuel
"""

import numpy as np
import monte_carlo_integration

def circle_g(x, y):
    return x**2 + y**2 - 1.5**2

def circle_f(x, y):
    return 1

if __name__ == "__main__":
    # Parameters for the integration
    x0, x1, y0, y1 = -1.5, 1.5, -1.5, 1.5
    n = 10000  # Number of random points

    # Calculate the area of the circle using Monte Carlo integration
    circle_area = monte_carlo_integration.MonteCarlo_double(circle_f, circle_g, x0, x1, y0, y1, n)
    print("Area of the circle with radius 1.5:", circle_area)

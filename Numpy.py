# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HRCnLAoVyS_E_Kl-NjnTFAUZrirUq4Fd
"""

import numpy as np
import time

a = np.zeros(4);             print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,));          print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4);    print(f"np.random.random_sample(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},      a shape = {a.shape}, a data type = {a.dtype}")
a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a},      a shape = {a.shape}, a data type = {a.dtype}")


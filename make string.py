# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:58:45 2019

@author: kids
"""
import numpy as np
ekg = np.load("F:\\30731_ekg_data\\ekg_lead_1.npy")
ekg = ekg[400000:402000]
print(min(ekg))
print(max(ekg))
print([e for e in ekg])
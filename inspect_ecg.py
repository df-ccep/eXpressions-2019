# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:52:19 2019

@author: kids
"""
import numpy as np


path = 'C:\\Users\\kids\\Expressions\\'

ecg = np.load(path + '30731_ekg_data\\ekg_lead_1.npy')

print(max(ecg))
print(min(ecg))
ecg[ecg > 200] = 200
ecg[ecg < -200] = -200

ecg = ecg[4000:5000]
notes = {1:'a3', 2:'b3', 3:'c4', 4:'d4', 5:'e4', 6:'f4', 7:'g4', 8:'a4', 9:'b4',
         10:'c5', 11:'d5', 12:'e5', 13:'f5', 14:'g5'}

bins = np.linspace(-200, 200, 14)
print(bins)
binned = np.digitize(ecg, bins)
print(binned)
note = []

for x in binned:
#    print(notes[x], end = ' ')
    note.append(notes[x])
    
print(note, end = ' ')  
print(np.bincount(binned))

np.reshape(note, (50, 20))
np.savetxt(path + '1000_notes.csv', note, fmt = '%s', delimiter = ', ')
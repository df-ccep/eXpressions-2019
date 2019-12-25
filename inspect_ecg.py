# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:52:19 2019

@author: dfertel

This is the code I used to turn the raw EKG values into notes
"""
import numpy as np

path = 'C:\\Users\\kids\\Expressions\\'

ecg = np.load(path + '30731_ekg_data\\ekg_lead_1.npy')

print(max(ecg))
print(min(ecg))

#All numbers greater than 200 to 200
ecg[ecg > 200] = 200
#All numbers less than -200 to 200
ecg[ecg < -200] = -200
#take a sample from the EKG
ecg = ecg[400000:401250]
#map notes to numbers
notes = {1:'a3', 2:'b3', 3:'c4', 4:'d4', 5:'e4', 6:'f4', 7:'g4', 8:'a4', 9:'b4',
         10:'c5', 11:'d5', 12:'e5', 13:'f5', 14:'g5'}
#divide the range up into equal bins
bins = np.linspace(-200, 200, 14)
print(bins)
#bin the EKG
binned = np.digitize(ecg, bins)
print(binned)
note = []

for x in binned:
#    print(notes[x], end = ' ')
    #convert numbers to notes
    note.append(notes[x])
    
print(note, end = ' ')  
print(np.bincount(binned))

#Don't know why this line is here
np.reshape(note, (50, 20))
#save as a comma-separated values file
np.savetxt(path + '1000_notes.csv', note, fmt = '%s', delimiter = ', ')

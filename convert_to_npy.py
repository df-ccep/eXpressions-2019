# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:50:41 2019

@author: kids
"""
#from scipy import io
import numpy as np
import matplotlib.pyplot as plt

path = "E:\\30731_ekg_data\\ekg_lead_1"
ekg = np.load(path)
def loadmat(path):
    
    mat = io.loadmat(path)
    print(type(mat))
    print(mat.keys())
    for key in mat.keys():
        if not key == 'val':
            print(mat[key])
    EKG = np.array(mat['val'], dtype = float)
    return EKG, mat.keys()

def plot(lead, xmin = 0, xmax = 1):
    fs = 250
    time = np.arange(lead.size) / fs

    fig = plt.plot(time, lead)
    plt.xlim(xmin, xmax)
    plt.show()
    
#EKG, headers = loadmat(path + 's30731m.mat')

#print(EKG.shape)
#print(EKG)

#lead_0 = EKG[0]
#lead_1 = EKG[1]
#lead_2 = EKG[2]

#np.save(path + 'ekg_lead_0', lead_0)
#np.save(path + 'ekg_lead_1', lead_1)
#np.save(path + 'ekg_lead_2', lead_2)

#print(lead_1)
plot(ekg[7000:7200])

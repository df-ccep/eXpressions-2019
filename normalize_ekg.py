'''
Normalize (fake normalize as I have not checked the mean and SD) the
EKG values to between -1 and 1 so I can scale up as necessary 
in the animation (I used responsive units so it works on all different
size screens.
'''
import numpy as np

ekg = np.load("F:\\30731_ekg_data\\ekg_lead_1.npy")

ekg = ekg[400000:401250]
#EKG values all between -1 and 1
ekg = ekg / np.max(np.abs(ekg))
#So I can copy-paste into JavaScript (It's not letting me upload files directly from JS)
print([e for e in ekg], end = ', ')

#np.save(ekg, "ekg_for_js")



import numpy as np

ekg = np.load("F:\\30731_ekg_data\\ekg_lead_1.npy")

ekg = ekg[400000:401250]
#EKG values all between -1 and 1
ekg = ekg / np.max(np.abs(ekg))
#So I can copy-paste into JavaScript (It's not letting me upload files directly from JS)
print([e for e in ekg], end = ', ')

#np.save(ekg, "ekg_for_js")



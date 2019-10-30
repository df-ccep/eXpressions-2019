import numpy as np

ekg = np.load("F:\\30731_ekg_data\\ekg_lead_1.npy")

ekg = ekg[400000:401250]
ekg = ekg / np.max(np.abs(ekg))
print([e for e in ekg], end = ', ')

#np.save(ekg, "ekg_for_js")



import numpy as np 
import mne

for i in range(1,110):
    print('Converting edf to numpy subject %d' % i)
    fp_ec = 'raw_data/data_ec_%.3d.npy' % i
    fp_eo = 'raw_data/data_eo_%.3d.npy' % i

    file_eo = 'files/S%.3d/S%.3dR01.edf' % (i,i)
    data_eo = mne.io.read_raw_edf(file_eo)
    data_eo = data_eo.get_data()
    data_eo = data_eo.transpose()
    data_eo = data_eo[:9600]    

    file_ec = 'files/S%.3d/S%.3dR02.edf' % (i,i)
    data_ec = mne.io.read_raw_edf(file_ec)
    data_ec = data_ec.get_data()
    data_ec = data_ec.transpose()
    data_ec = data_ec[:9600]    

    np.save(fp_ec,data_ec)
    np.save(fp_eo,data_eo)
    
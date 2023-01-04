import numpy as np 
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

lowcut = 8.0
highcut = 12.0
fs = 160

for i in range(1,110):
    print ('EC',i)
    Data = np.load('raw_data/data_ec_%.3d.npy' % i)

    for j in range(len(Data[0])):
        Serie = Data[:,j]
        y = butter_bandpass_filter(Serie, lowcut, highcut, fs, order=6)   
        Data[:,j] = y

    np.save('filtered_data/alpha_data_ec_%.3d.npy' % i,Data)

for i in range(1,110):
    print ('EO',i)
    Data = np.load('raw_data/data_eo_%.3d.npy' % i)

    for j in range(len(Data[0])):
        Serie = Data[:,j]
        y = butter_bandpass_filter(Serie, lowcut, highcut, fs, order=6)   
        Data[:,j] = y

    np.save('filtered_data/alpha_data_eo_%.3d.npy' % i,Data)

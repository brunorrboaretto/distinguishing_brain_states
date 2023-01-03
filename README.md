# distinguishing_brain_states

We use ordinal analysis to distinguish between eyes-open (EO) and eyes-closed (EC) resting brain states. 

We analyze EEG data recorded with 64 electrodes from 109 healthy subjects, under two one-minute baseline runs: One with eyes open, and one with eyes closed. The data is freely available at https://physionet.org/content/eegmmidb/1.0.0/. We use spatial ordinal analysis to distinguish between these states, where the permutation entropy is evaluated considering the spatial distribution of electrodes for each time instant. 

We analyze both raw and post-processed data considering only the alpha-band frequency which is known to be important for resting states in the brain. 

The raw files are stored in <code>/raw_data</code> directory in <code>.npy</code> files. See https://fileinfo.com/extension/npy for more information. 

Instructions for running the code:

<code>filtering_data.sh</code> creates a new directory <code>/filtered_data</code> and automatically runs <code>filterd_data.py</code> which is a bandpass Butterworth filter which uses the <code> Scipy </code> open library to select the alpha-band frequency (8 - 12 Hz). This process may take a few seconds.

<code> spatial_PE.py </code> evaluates the spatial permutation entropy, creating 4 files containing the spatial PE of EO and EC states of each subject (2 files for raw data and two files for filtered data). This process may take a few minutes. <code> shuffled_spatial_PE.py </code> do the same but shuffle the data. We have discarded subjects 97 and 109 due to several null values at the end of the time series. 

<code> plot_figures.py </code> creates three figures, which correspond to figures 5,6, and 8 of the manuscript XXXXX.  

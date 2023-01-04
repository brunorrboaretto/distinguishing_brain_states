# distinguishing_brain_states

We use ordinal analysis to distinguish between eyes-open (EO) and eyes-closed (EC) resting brain states. 

We analyze EEG data recorded with 64 electrodes from 109 healthy subjects, under two one-minute baseline runs: One with eyes open, and one with eyes closed. The data is freely available. We use spatial ordinal analysis to distinguish between these states, where the permutation entropy is evaluated considering the spatial distribution of electrodes for each time instant. 

We analyze both raw and post-processed data considering only the alpha-band frequency which is known to be important for resting states in the brain. 

Preparing the data:

- The raw data can be downloaded from https://physionet.org/content/eegmmidb/1.0.0/ as a <code>.zip</code> file. which contains the data from 109 subjects. 
- By extracting the data, a directory <code>files</code> will be created including the data from 109 subjects, containing in majority <code>.edf</code> files.
- <code>preparing_data.sh</code> will automatically create a <code>raw_data</code> directory and using <code>convert_edf2npy.py</code>, converts the data into <code>.npy</code> files. After that a <code>filtered_data</code> directory is created and <code>filter_data.py</code> is activated which is a bandpass Butterworth filter which uses the <code> Scipy </code> open library to select the alpha-band frequency (8 - 12 Hz). This process may take a few seconds.

Instructions for running the code:

<code> spatial_PE.py </code> evaluates the spatial permutation entropy, creating 4 files containing the spatial PE of EO and EC states of each subject (2 files for raw data and two files for filtered data). This process may take a few minutes. <code> shuffled_spatial_PE.py </code> do the same but shuffle the data. We have discarded subjects 97 and 109 due to several null values at the end of the time series. 

<code> plot_figures.py </code> creates three figures, which correspond to figures 5,6, and 8 of the manuscript XXXXX.  


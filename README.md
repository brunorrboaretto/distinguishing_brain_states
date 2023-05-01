# distinguishing_brain_states

We use ordinal analysis to distinguish between eyes-open (EO) and eyes-closed (EC) resting brain states. 

We analyze EEG data recorded with 64 electrodes from 109 healthy subjects, under two one-minute baseline runs: One with eyes open, and one with eyes closed. The data is freely available. We use spatial ordinal analysis to distinguish between these states, where the permutation entropy is evaluated considering the spatial distribution of electrodes for each time instant. 

We analyze both raw and post-processed data considering only the alpha-band frequency which is known to be important for resting states in the brain. 

*To ensure proper attribution, It would be greatly appreciated if you could kindly cite our paper <code>DOI:10.1016/j.chaos.2023.113453</code>.
Thank you for considering our work!* 

## Preparing the data:

- The raw data can be downloaded from https://physionet.org/content/eegmmidb/1.0.0/ as a <code>.zip</code> file, which contains the data from 109 subjects (1.9 GB). 
- By extracting the data, a directory <code>/files</code> is created including several folders containing in majority <code>.edf</code> files.
- Run the command line <code>chmod +x preparing_data.sh</code> to transform the <code>shell</code> file into and executable.
- The command line <code>./preparing_data.sh</code> automatically creates a <code>/raw_data</code> directory and <code>/filtered_data</code> with the data as <code>.npy</code> files.

## Instructions for running the code:

- command <code> python3 spatial_PE.py </code> evaluates the spatial permutation entropy, creating 4 files containing the spatial permutation entropy of EO and EC states of each subject (2 files for raw data and 2 files for filtered data). This process may take a few minutes. 
- <code> python3 perm_spatial_PE.py </code> do the same but considering different spatial configuration of the electrodes. 
- <code> python3 shuffled_spatial_PE.py </code> do the same but shuffle the data. We have discarded subjects 97 and 109 due to several null values at the end of the time series.
- <code> python3 plot_figures.py </code> creates four figures, which correspond to figures 5,6,7, and 9 of the manuscript.  

## Python libraries:

- <code>numpy </code>
- <code>mne </code> to convert edf to npy.
- <code>scipy </code> to filter the data.
- <code>matplotlib.pyplot </code> to generate the figures.

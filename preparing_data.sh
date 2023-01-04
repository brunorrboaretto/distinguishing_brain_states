#!/bin/bash
mkdir raw_data;
mkdir filtered_data;
python3 convert_edf2npy.py;
python3 filter_data.py;


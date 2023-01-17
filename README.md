# eeg_clastering using k means.

after preprocessing your data and analyzing the eeg signal to get roi in each subject (one signal in each subject),
this program will claster the subjects to clusters according to common patterns in the time domain waveform of the signals using k means with the tslearn library.

for more information on the library you can check: Tslearn, A Machine Learning Toolkit for Time Series Data

## how to use?

works for me in windows10.

* clone the project
* change the home folder
* change the files datatarget1.mat, datatarget2.mat to the files you want to analyize
* run the main function
* you can change some parameters in the algorithm according to the tslrean documentation and see if it gives you better results. 


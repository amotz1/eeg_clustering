# eeg_clustering using k means.

after preprocessing your data and analyzing the eeg signal to get roi in each subject (one signal in each subject),
this program will cluster the subjects to clusters according to common patterns in the time domain waveform of the signals using k means with the tslearn library. it creates a directory tree and save the results automatically. it can also evaluate a range of cluster numbers and save figures of the metrics used to evaluate them in a dedicated directory tree.

for more information on the tslearn library you can check: Tavenard, R., Faouzi, J., Vandewiele, G., Divo, F., Androz, G., Holtz, C., ... & Woods, E. (2020). Tslearn, a machine learning toolkit for time series data. The Journal of Machine Learning Research, 21(1), 4686-4691.

and https://tslearn.readthedocs.io/en/stable/index.html

## how to use?

works for me in windows10.

* clone the project
* change the home folder
* change the files datatarget1.mat, datatarget2.mat to the the 2 conditions you have (2 matrices of n subjects * m datapoints saved as a mat file) you want to analyize
* run the main function, the program will ask you 2 questions. 
* first if you want a clustering experiment or an experiment that evaluate the performance of range of cluster numbers. 
* second if you are doing a specific experiment or if you want a to vary n_init/max_iter_barycenter arguments. 
* you can press c if you want clustering experiment and e if you want evaluation experiment s if you want a specific experiment and b/i if you want an experiment that change one of these variables 
* you can change some other parameters in the algorithm according to the tslrean documentation and see if it gives you better results. 


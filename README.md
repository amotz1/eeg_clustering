# eeg_clustering using k means.

after preprocessing your data and analyzing the eeg signal to get roi in each subject (one signal in each subject),
this program will cluster the subjects to clusters according to common patterns in the time domain waveform of the signals using k means with the tslearn library. it creates a directory tree and save the results automatically. it can also evaluate a range of cluster numbers and save figures of the metrics used to evaluate them in a dedicated directory tree.

for more information on the tslearn library, you can check: Tavenard, R., Faouzi, J., Vandewiele, G., Divo, F., Androz, G., Holtz, C., ... & Woods, E. (2020). Tslearn, a machine learning toolkit for time series data. The Journal of Machine Learning Research, 21(1), 4686-4691.

and https://tslearn.readthedocs.io/en/stable/index.html

this is how the graph of the clustering can look like at the end:

<img src="https://github.com/amotz1/eeg_clustering/blob/master/clusters_results.png">

## how to use?

works for me in windows10.

* clone the project and create a local python environment with the neccesary libraries (you can try the requirements.txt if it works for you)
* change the home folder
* add two .mat files with the eeg data conditions after pre-processing with a matrix format of n (subjects) * m (time samples) and change the load_data function in the utils file to load those files
* run the main function, the program will ask you 2 questions. 
* first if you want a clustering experiment or an experiment that evaluate the performance of range of cluster numbers. 
* second if you are doing a specific experiment or if you want a to vary n_init/max_iter_barycenter arguments. 
* you can press c if you want clustering experiment and e if you want evaluation experiment ec if you want both. you can then press s if you want a specific experiment and b/i if you want an experiment that change one of these variables 
* you can change some other parameters in the algorithm according to the tslrean documentation and see if it gives you better results. 

### issues

* right now if you are doing both experiments (ec) you can use just one type of experiment for both of them. eventually i use mainly the specific option and i see no reason to use the ec option at all.



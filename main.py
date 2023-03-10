from config import config
import numpy as np
import scipy
from utils import plot_save_data
from clustering_experiment import k_means_clustering_experiment
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from eval_clusters_number import elobow_method
from utils import load_data


# WE NEED TO CITE: Tslearn, A Machine Learning Toolkit for Time Series Data


def main(param):
    down_sample_data = scipy.signal.decimate(param["data"], param["down_sample_factor"])
    np.random.seed(param["random_state"])
    down_sample_standardized_data = TimeSeriesScalerMeanVariance().fit_transform(down_sample_data)

    plot_save_data(down_sample_standardized_data, param)

    elobow_method(down_sample_standardized_data, param)
    k_means_clustering_experiment(down_sample_standardized_data, param)


if __name__ == '__main__':
    data = load_data()
    (data_target1, data_target2) = data
    exp_data = data_target1

    args = {"data": exp_data, "exp_number": 82, "home_folder": "E:\\omer",
            "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": 10,
            "n_clusters": 2, "clusters_range": [2, 3], "random_state": 0, "verbose": 0,
            "tol": 10**-6, "n_jobs": None, "init": "k-means++", 'max_iter': 50,
            "dtw_inertia": False, "metric_params": None}

    if (exp_data == data_target1).all():
        args['num_cond'] = 'cond_1'
    else:
        args['num_cond'] = 'cond_2'

    args = config(args)

    main(args)

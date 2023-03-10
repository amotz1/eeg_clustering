from utils import create_exp_spec
from utils import load_data
from config import config


def test_create_exp_spec():

    data = load_data()
    (data_target1, data_target2) = data

    param = {"data": data_target1, "exp_number": 555, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": 10,
             "n_clusters": 4, "clusters_range": [2, 7], "random_state": 0, "max_iter": 50 ,"n_jobs": None, "tol": 10**-6,
             "verbose": 0, "init": "k-means++", "metric_params": None, "dtw_inertia": False}

    param = config(param)

    create_exp_spec(param)


test_create_exp_spec()
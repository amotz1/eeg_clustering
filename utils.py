import scipy.io
import pickle
from tslearn.clustering import TimeSeriesKMeans
from tslearn.clustering import silhouette_score
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_eval_c(dba_km, data, param, exp_folder_path_key):
    print("fitting...")
    dba_km = dba_km.fit(data)
    print("calc_sillhouette...")

    print("data.shape ", data.shape)
    print("data.ndim ", data.ndim)
    silhouette_avg = silhouette_score(data, dba_km.labels_, param['metric'])
    print("end_sillhouette...")
    print("silhouette avg ", silhouette_avg)

    with open(param[exp_folder_path_key] + "\\" + "results.pickle", "wb") as bf:
        pickle.dump(dba_km, bf)

    with open(param[exp_folder_path_key] + "\\" + "silhouette_avg.pickle", "wb") as bf:
        pickle.dump(silhouette_avg, bf)

    print(dba_km.labels_)
    sz = data.shape[1]

    for cluster_index in range(param['n_clusters']):
        plt.style.use('seaborn')
        plt.subplot(param['n_clusters'], 1,  cluster_index + 1)
        print("cluster index ", cluster_index)

        if cluster_index == 0:
            plt.title("subjects signals devided to clusters")

        for sub_sig in data[dba_km.labels_ == cluster_index]:
            plt.plot(sub_sig.ravel(), alpha=0.4)
            plt.xlabel('time samples')
            plt.ylabel('mV')
            plt.xlim(0, sz)

    print(param[exp_folder_path_key] + "clusters_results.png")
    plt.savefig(param[exp_folder_path_key] + "\\" + "clusters_results.png")


def load_data():

    data_target1 = scipy.io.loadmat(r"data_target1.mat")
    data_target2 = scipy.io.loadmat(r"data_target2.mat")

    data_target_1 = data_target1["data_target1"]
    data_target_2 = data_target2["data_target2"]

    # data_target1_train = data_target1["data_target1"][0:23, :]
    # data_target1_test = data_target1["data_target1"][24:29, :]
    #
    # data_target2_train = data_target2['data_target2'][0:23, :]
    # data_target2_test = data_target2['data_target2'][24:29, :]

    return data_target_1, data_target_2


def param_2_file(param, text_file):
    number_of_subjects = param["number_of_subjects"]
    text_file.write(f"number_of_subjects {number_of_subjects} \n")

    home_folder = param["home_folder"]
    text_file.write(f"home_folder {home_folder} \n")

    down_sample_factor = param["down_sample_factor"]
    text_file.write(f"down_sample_factor {down_sample_factor} \n")

    metric = param["metric"]
    text_file.write(f"metric {metric} \n")

    n_init = param["n_init"]
    text_file.write(f"n_init {n_init} \n")

    max_iter_barycenter = param["max_iter_barycenter"]
    text_file.write(f"max_iter_barycenter {max_iter_barycenter} \n")

    if param['exp_type'] == "c" or param["exp_type"] == "ec":
        n_clusters = param["n_clusters"]
        text_file.write(f"n_clusters {n_clusters} \n")

    if param["exp_type"] == "e" or param["exp_type"] == "ec":
        clusters_range = param["clusters_range"]
        text_file.write(f"clusters_range {clusters_range} \n")

    random_state = param["random_state"]
    text_file.write(f"random_state {random_state} \n")

    init = param["init"]
    text_file.write(f"init {init} \n")

    max_iter = param["max_iter"]
    text_file.write(f"max_iter {max_iter} \n")

    dtw_inertia = param["dtw_inertia"]
    text_file.write(f"dtw_inertia {dtw_inertia} \n")

    metric_params = param["metric_params"]
    text_file.write(f"metric_params {metric_params} \n")

    tol = param["tol"]
    text_file.write(f"tol {tol} \n")

    verbose = param["verbose"]
    text_file.write(f"verbose {verbose} \n")

    n_jobs = param["n_jobs"]
    text_file.write(f"n_jobs {n_jobs} \n")

    text_file.close()


def check_param(param):

    if param['var_change'] == "i":

        assert type(param['n_init']) == list, "n_init vary so need to be a list"
        assert type(param['down_sample_factor']) == int, "down_sample_factor need to be an int"
        assert type(param['exp_type']) == str, "exp_type need to be str"
        assert type(param['home_folder']) == str, "home folder need to be str"
        assert type(param['max_iter_barycenter']) == int, "not vary so need to be int"
        assert type(param['metric']) == str, "not vary so need to be str"
        assert type(param['n_clusters']) == int, "n_clusters need to be int"
        assert type(param['clusters_range']) == list, "clusters range need to be a list"
        assert type(param['tol']) == float, "tol must be float"
        assert type(param['verbose']) == int, "verbose must be int"
        assert type(param['n_jobs']) == int or None, "n_jobs can be int or None"
        assert type(param['metric_params']) == dict or None, "metric params need to be dict or None"
        assert type(param['dtw_inertia']) == bool, "dtw_inertia need to be a bool"
        assert type(param['init']) == str or np.ndarray, "init must be str or numpy array"
        assert type(param['random_state']) == int or np.random.RandomState, "random_state must be int or numpy " \
                                                                            "random state"

    elif param['var_change'] == "b":
        assert type(param['n_init']) == int, "n_init do not vary so need to be an int"
        assert type(param['down_sample_factor']) == int, "down_sample_factor need to be a list"
        assert type(param['exp_type']) == str, "exp_type need to be str"
        assert type(param['home_folder']) == str, "home folder need to be str"
        assert type(param['max_iter_barycenter']) == list, "max_iter_barycenter vary so need to be a list"
        assert type(param['metric']) == str, "metric do not vary so need to be str"
        assert type(param['n_clusters']) == int, "n_clusters need to be int"
        assert type(param['clusters_range']) == list, "clusters range need to be a list"
        assert type(param['tol']) == float, "tol must be float"
        assert type(param['verbose']) == int, "verbose must be int"
        assert type(param['n_jobs']) == int or None, "n_jobs can be int or None"
        assert type(param['metric_params']) == dict or None, "metric params need to be dict or None"
        assert type(param['dtw_inertia']) == bool, "dtw_inertia need to be a bool"
        assert type(param['init']) == str or np.ndarray, "init must be str or numpy array"
        assert type(param['random_state']) == int or np.random.RandomState, "random_state must be int or numpy " \
                                                                            "random state"

    elif param['var_change'] == "m":
        assert type(param['n_init']) == list, "n_init do not vary so need to be an int"
        assert type(param['down_sample_factor']) == int, "down_sample_factor need to be a list"
        assert type(param['exp_type']) == str, "exp_type need to be str"
        assert type(param['home_folder']) == str, "home folder need to be str"
        assert type(param['max_iter_barycenter']) == int, "max_iter_barycenter do not vary so need to be int"
        assert type(param['metric']) == list, "metric vary so need to be a list"
        assert type(param['n_clusters']) == int, "n_clusters need to be int"
        assert type(param['clusters_range']) == list, "clusters range need to be a list"
        assert type(param['tol']) == float, "tol must be float"
        assert type(param['verbose']) == int, "verbose must be int"
        assert type(param['n_jobs']) == int or None, "n_jobs can be int or None"
        assert type(param['metric_params']) == dict or None, "metric params need to be dict or None"
        assert type(param['dtw_inertia']) == bool, "dtw_inertia need to be a bool"
        assert type(param['init']) == str or np.ndarray, "init must be str or numpy array"
        assert type(param['random_state']) == int or np.random.RandomState, "random_state must be int or numpy " \
                                                                            "random state"

    elif param['var_change'] == "s":
        assert type(param['n_init']) == int, "n_init do not vary so need to be an int"
        assert type(param['down_sample_factor']) == int, "down_sample_factor need to be an int"
        assert type(param['exp_type']) == str, "exp_type need to be str"
        assert type(param['home_folder']) == str, "home folder need to be str"
        assert type(param['max_iter_barycenter']) == int, "max_iter_barycenter do not vary so need to be int"
        assert type(param['metric']) == str, "metric do not vary so need to be str"
        assert type(param['n_clusters']) == int, "n_clusters need to be int"
        assert type(param['clusters_range']) == list, "clusters range need to be a list"
        assert type(param['tol']) == float, "tol must be float"
        assert type(param['verbose']) == int, "verbose must be int"
        assert type(param['n_jobs']) == int or param['n_jobs'] is None, "n_jobs can be int or None"
        assert type(param['metric_params']) == dict or param['metric_params'] is None, "metric params need to " \
                                                                                       "be dict or None"
        assert type(param['dtw_inertia']) == bool, "dtw_inertia need to be a bool"
        assert type(param['init']) == str or np.ndarray, "init must be str or numpy array"
        assert type(param['random_state']) == int or np.random.RandomState, "random_state must be int or numpy " \
                                                                            "random state"
    else:
        print("unspecified experiment")


def plot_save_data(data, param):
    length = 10
    height = int(np.round(data.shape[0], decimals=-1) / 10)
    reminder = int(np.round(data.shape[0], decimals=-1) - data.shape[0])
    os.chdir(param['exp_var_change_folder'])
    plt.figure(figsize=(15, 5))
    for sig_ind in range(data.shape[0]):
        plt.style.use('seaborn')
        plt.subplot(height, length, sig_ind+1)
        if sig_ind == np.floor(length / 2):
            plt.title("subjects after preprocessing")
        if sig_ind >= ((height-1)*length)-reminder:
            plt.xlabel('time samples')

        if sig_ind % 10 == 0:
            plt.ylabel('mV')

        plt.plot(data[sig_ind, :])

    plt.savefig(os.getcwd() + "\\" + "subjects_graphs.png")
    plt.close()


def plot_save_eval(param, inertias, silhouette_avgs, exp_folder_path_key):

    with open(param[exp_folder_path_key] + "\\" + "inertias", "wb") as fp:
        pickle.dump(inertias, fp)

    with open(param[exp_folder_path_key] + "\\" + "silhouette_avgs", "wb") as fp:
        pickle.dump(silhouette_avgs, fp)

    plt.style.use('seaborn')
    plt.plot(param['clusters_range'], inertias)
    plt.title('clusters inertia')
    plt.xlabel('cluster number')
    plt.ylabel('inertia')
    plt.savefig(param[exp_folder_path_key] + "\\" + "sum_samples_centroid_distances.png")
    plt.close()

    plt.style.use('seaborn')
    plt.plot(param['clusters_range'], silhouette_avgs)
    plt.title('cluster silhouette_avg')
    plt.xlabel('cluster number')
    plt.ylabel('silhouette_avg')
    plt.savefig(param[exp_folder_path_key] + "\\" + "silhouette_avgs.png")


def create_exp_spec(param):
    if param['var_change'] == 's':
        with open(param["exp_folder_path"] + "\\" + "exp_spec.text", 'w') as text_file:
            param_2_file(param, text_file)

    else:
        with open(param["exp_var_change_folder"] + "\\" + "exp_spec.text", 'w') as text_file:
            param_2_file(param, text_file)

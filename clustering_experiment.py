from tslearn.clustering import TimeSeriesKMeans
import os
from utils import plot_eval_c
from utils import check_param


def k_means_clustering_experiment(data, param):
    check_param(param)

    if param["exp_type"] == "c" or param["exp_type"] == "ec":

        if param['var_change'] == "i" and param["exp_type"] == "c" or param["exp_type"] == "ec":
            for n_init_ind in range(len(param['n_init'])):
                dba_km = TimeSeriesKMeans(n_clusters=param['n_clusters'],
                                          n_init=param['n_init'][n_init_ind],
                                          metric=param['metric'],
                                          verbose=False,
                                          max_iter_barycenter=param['max_iter_barycenter'],
                                          random_state=param['seed'])

                exp_folder_path_key = 'exp_folder_path_{n_init_ind}'.format(n_init_ind=n_init_ind + 1)
                plot_eval_c(dba_km, data, param, exp_folder_path_key)

        elif param['var_change'] == "b" and param["exp_type"] == "c" or param["exp_type"] == "ec":
            for barycenter_ind in range(len(param['max_iter_barycenter'])):
                dba_km = TimeSeriesKMeans(n_clusters=param['n_clusters'],
                                          n_init=param['n_init'],
                                          metric=param['metric'],
                                          verbose=False,
                                          max_iter_barycenter=param['max_iter_barycenter'][barycenter_ind],
                                          random_state=param['seed'])

                exp_folder_path_key = 'exp_folder_path_{barycenter_ind}'.format(barycenter_ind=barycenter_ind + 1)
                plot_eval_c(dba_km, data, param, exp_folder_path_key)

        elif param['var_change'] == "s" and (param["exp_type"] == "c" or param["exp_type"] == "ec"):
            print("starting the timeseriesKmeans algorithm")
            dba_km = TimeSeriesKMeans(n_clusters=param['n_clusters'],
                                      n_init=param['n_init'],
                                      metric=param['metric'],
                                      verbose=False,
                                      max_iter_barycenter=param['max_iter_barycenter'],
                                      random_state=param['seed'])

            exp_folder_path_key = 'exp_folder_path'
            os.chdir(param[exp_folder_path_key])
            plot_eval_c(dba_km, data, param, exp_folder_path_key)
            os.chdir('..')

        else:
            print("unspecified experiment")







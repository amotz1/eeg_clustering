from tslearn.clustering import TimeSeriesKMeans
from tslearn.clustering import silhouette_score
import os
from utils import check_param
from utils import plot_save_eval

#  TODO: delegate the evaluation and plotting code to subfunctions


def elobow_method(data, param):
    check_param(param)

    if param["exp_type"] == "e" or param["exp_type"] == "ec":

        inertias = []
        silhouette_avgs = []
        centroids = param['clusters_range']

        if param['var_change'] == "i" and param["exp_type"] == "e" or param["exp_type"] == "ec":
            for n_init_ind in range(len(param['n_init'])):
                print('n_init_ind ', n_init_ind)
                exp_folder_path_key = 'exp_folder_path_{n_init_ind}'.format(n_init_ind=n_init_ind + 1)
                os.chdir(param[exp_folder_path_key])

                for centroid in centroids:
                    km = TimeSeriesKMeans(n_clusters=centroid,
                                          n_init=param['n_init'][n_init_ind],
                                          metric=param['metric'],
                                          verbose=False,
                                          max_iter_barycenter=param['max_iter_barycenter'],
                                          random_state=0)

                    km = km.fit(data)
                    inertias.append(km.inertia_)

                    y_pred_dba_km = km.fit_predict(data)
                    silhouette_avg = silhouette_score(data, y_pred_dba_km, metric=param['metric'])
                    silhouette_avgs.append(silhouette_avg)
                    print('silhoutte_avg ', silhouette_avg)

                plot_save_eval(param, inertias, silhouette_avgs, exp_folder_path_key)
                os.chdir('..')

        if param['var_change'] == "b" and param["exp_type"] == "e" or param["exp_type"] == "ec":
            for barycenter_ind in range(len(param['max_iter_barycenter'])):
                print('barycenter_ind ', barycenter_ind)
                exp_folder_path_key = 'exp_folder_path_{barycenter_ind}'.format(barycenter_ind=barycenter_ind + 1)
                os.chdir(param[exp_folder_path_key])

                for centroid in centroids:
                    km = TimeSeriesKMeans(n_clusters=centroid,
                                          n_init=param['n_init'],
                                          metric=param['metric'],
                                          verbose=False,
                                          max_iter_barycenter=param['max_iter_barycenter'][barycenter_ind],
                                          random_state=0)

                    km = km.fit(data)
                    inertias.append(km.inertia_)
                    silhouette_avg = silhouette_score(data, km.labels_, metric=param['metric'])
                    silhouette_avgs.append(silhouette_avg)
                    print('silhoutte_avg ', silhouette_avg)

                plot_save_eval(param, inertias, silhouette_avgs, exp_folder_path_key)
                os.chdir('..')

        if param['var_change'] == "s" and (param["exp_type"] == "e" or param["exp_type"] == "ec"):
            exp_folder_path_key = 'exp_folder_path'
            os.chdir(param[exp_folder_path_key])

            for centroid in centroids:
                print("fitting...")
                km = TimeSeriesKMeans(n_clusters=centroid,
                                      n_init=param['n_init'],
                                      metric=param['metric'],
                                      verbose=False,
                                      max_iter_barycenter=param['max_iter_barycenter'],
                                      random_state=0)

                km = km.fit(data)
                inertias.append(km.inertia_)
                silhouette_avg = silhouette_score(data, km.labels_, metric=param['metric'])
                silhouette_avgs.append(silhouette_avg)
                print('silhoutte_avg ', silhouette_avg)

            plot_save_eval(param, inertias, silhouette_avgs, exp_folder_path_key)
            os.chdir('..')





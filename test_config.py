from config import config
from utils import load_data


def test_config():

    data = load_data()
    (data_target1, data_target2) = data

    param = {"data": data_target1, "exp_number": 556, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": 10,
             "n_clusters": 3, "clusters_range": [2, 8], "random_state": 0,
             "init": 'k-means++', "verbose": 0, "n_jobs": None, "tol": 10**6, "metric_params":None,
             "max_iter": 50, "dtw_intertia": False}

    param = config(param)
    print(param.keys())

    assert param["exp_number"] == 556
    assert param["number_of_subjects"] == 29
    assert param["home_folder"] == "E:\\omer"
    assert param["n_init"] == 2
    assert param["max_iter_barycenter"] == 10
    assert param["down_sample_factor"] == 2
    assert param["metric"] == "dtw"
    assert param["n_clusters"] == 3
    assert param["clusters_range"] == [2,8]
    assert param["random_state"] == 0
    assert param["metric_params"] is None
    assert param["dtw_inertia"] is False
    assert param["tol"] == 10**-6
    assert param["max_iter"] == 50
    assert param["verbose"] == 0
    assert param["n_jobs"] is None

    if param["exp_type"] == "e":
        assert param["var_change"] == "s"
        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\cond_1\\specific_556"
        print(param["exp_folder_path"])
        assert param["exp_folder_path"] == "E:\\omer\\elbow_method\\cond_1\\" \
                                           "specific_556"

    if param["exp_type"] == "c":
        assert param["var_change"] == "s"
        assert param["exp_type_folder"] == "E:\\omer\\clustering"
        print(param["exp_var_change_folder"])
        assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\cond_1\\specific_556"

        assert param["exp_folder_path"] == "E:\\omer\\clustering\\cond_1\\specific_556"

    param = {"data": data_target1, "exp_number": 556, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": [2, 3, 4], "max_iter_barycenter": 10,
             "n_clusters": 3, "clusters_range": [2,8], "random_state": 0}

    param = config(param)
    print(param.keys())

    if param["exp_type"] == "e":

        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\cond_1\\n_init_change_556"
        assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\cond_1\\" \
                                             "n_init_change_556\\n_init_2"

        assert param["exp_folder_path_2"] == "E:\\omer\\elbow_method\\cond_1\\" \
                                             "n_init_change_556\\n_init_3"

        assert param["exp_folder_path_3"] == "E:\\omer\\elbow_method\\cond_1\\n_init_change_556\\n_init_4"
    elif param['exp_type'] == 'c':
        assert param["exp_type_folder"] == "E:\\omer\\clustering"

        assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\cond_1\\n_init_change_556"

        assert param["exp_folder_path_1"] == "E:\\omer\\clustering\\cond_1\\n_init_change_556\\n_init_2"
        
        assert param["exp_folder_path_2"] == "E:\\omer\\clustering\\cond_1\\n_init_change_556\\n_init_3"
                                             
        assert param["exp_folder_path_3"] == "E:\\omer\\clustering\\cond_1\\n_init_change_556\\n_init_4"

    param = {"data": data_target1, "exp_number": 556, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": [10, 40, 80, 160],
             "n_clusters": 3, "clusters_range": [2,8], "random_state": 0}

    param = config(param)

    if param['exp_type'] == 'e':
        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        print(param["exp_var_change_folder"])
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change_556"
        print(param["exp_folder_path_1"])
        assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change_556\\" \
                                             "max_iter_barycenter_10"

        print(param["exp_folder_path_2"])
        assert param["exp_folder_path_2"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change_556\\" \
                                             "max_iter_barycenter_40"

        assert param["exp_folder_path_3"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change_556\\" \
                                             "max_iter_barycenter_80"

        assert param["exp_folder_path_4"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change_556\\" \
                                             "max_iter_barycenter_160"

    elif param['exp_type'] == 'c':

            assert param["exp_type_folder"] == "E:\\omer\\clustering"
            assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\cond_1\\max_iter_barycenter_change_556"
            assert param["exp_folder_path_1"] == "E:\\omer\\clustering\\cond_1\\max_iter_barycenter_change_556\\max_iter_barycenter_10"

            assert param["exp_folder_path_2"] == "E:\\omer\\clustering\\cond_1\\max_iter_barycenter_change_556\\max_iter_barycenter_40"

            assert param["exp_folder_path_3"] == "E:\\omer\\clustering\\cond_1\\max_iter_barycenter_change_556\\max_iter_barycenter_80"

            assert param["exp_folder_path_4"] == "E:\\omer\\clustering\\cond_1\\max_iter_barycenter_change_556\\max_iter_barycenter_160"

# if param["var_change"] == "i":
    #         assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
    #         assert param["var_change_folder"] == "E:\\omer\\elbow_method\\cond_1\\init_change_2"
    #
    #         assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\cond_1\\" \
    #                                            "init_change_2\\n_init_2, max_iter_barycenter_10, metric dtw," \
    #                                            " down_sample_factor , 2, number of subjects 29"
    #
    #     elif param["var_change"] == "b":
    #         assert param["exp_type_folder"] == "E:\\omer\\elbow_method\\cond_1\\"
    #         assert param["var_change_folder"] == "E:\\omer\\elbow_method\\cond_1\\max_iter_barycenter_change2"
    #
    #         assert param["exp_folder_path"] == "E:\\omer\\elbow_method\\cond_1\\" \
    #                                            "barycenter_change2\\n_init_2, max_iter_barycenter_10, metric dtw," \
    #                                            " down_sample_factor , 2, number of subjects 29"
    #
    #
    #


test_config()
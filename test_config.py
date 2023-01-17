from config import config
from utils import load_data


def test_config():

    data = load_data()
    (data_target1, data_target2) = data

    param = {"data": data_target1, "exp_number": 555, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": 10,
             "n_clusters": 3, "clusters_range": [2,8], "seed": 0}

    param = config(param)
    print(param.keys())

    assert param["exp_number"] == 555
    assert param["number_of_subjects"] == 29
    assert param["home_folder"] == "E:\\omer"
    assert param["n_init"] == 2
    assert param["max_iter_barycenter"] == 10
    assert param["down_sample_factor"] == 2
    assert param["metric"] == "dtw"
    assert param["n_clusters"] == 3
    assert param["clusters_range"] == [2,8]
    assert param["seed"] == 0

    if param["exp_type"] == "e":
        assert param["var_change"] == "s"
        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\specific_555"
        print(param["exp_folder_path"])
        assert param["exp_folder_path"] == "E:\\omer\\elbow_method\\" \
                                           "specific_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                           " down_sample_factor , 2, number of subjects 29"

    if param["exp_type"] == "c":
        assert param["var_change"] == "s"
        assert param["exp_type_folder"] == "E:\\omer\\clustering"
        assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\specific_555"

        assert param["exp_folder_path"] == "E:\\omer\\clustering\\" \
                                           "specific_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                           " down_sample_factor , 2, number of subjects 29"

    param = {"data": data_target1, "exp_number": 555, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": [2, 3, 4], "max_iter_barycenter": 10,
             "n_clusters": 3, "clusters_range": [2,8], "seed": 0}

    param = config(param)
    print(param.keys())

    if param["exp_type"] == "e":

        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\n_init_change_555"
        assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\" \
                                             "n_init_change_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_2"] == "E:\\omer\\elbow_method\\" \
                                             "n_init_change_555\\n_init_3, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_3"] == "E:\\omer\\elbow_method\\" \
                                             "n_init_change_555\\n_init_4, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"
    elif param['exp_type'] == 'c':
        assert param["exp_type_folder"] == "E:\\omer\\clustering"

        assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\n_init_change_555"

        assert param["exp_folder_path_1"] == "E:\\omer\\clustering\\" \
                                             "n_init_change_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_2"] == "E:\\omer\\clustering\\" \
                                             "n_init_change_555\\n_init_3, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_3"] == "E:\\omer\\clustering\\" \
                                             "n_init_change_555\\n_init_4, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

    param = {"data": data_target1, "exp_number": 555, "home_folder": "E:\\omer",
             "down_sample_factor": 2, "metric": "dtw", "n_init": 2, "max_iter_barycenter": [10, 40, 80, 160],
             "n_clusters": 3, "clusters_range": [2,8], "seed": 0}

    param = config(param)

    if param['exp_type'] == 'e':
        assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
        print(param["exp_var_change_folder"])
        assert param["exp_var_change_folder"] == "E:\\omer\\elbow_method\\max_iter_barycenter_change_555"
        print(param["exp_folder_path_1"])
        assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\" \
                                             "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        print(param["exp_folder_path_2"])
        assert param["exp_folder_path_2"] == "E:\\omer\\elbow_method\\" \
                                             "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_40, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_3"] == "E:\\omer\\elbow_method\\" \
                                             "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_80, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

        assert param["exp_folder_path_4"] == "E:\\omer\\elbow_method\\" \
                                             "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_160, metric dtw," \
                                             " down_sample_factor , 2, number of subjects 29"

    elif param['exp_type'] == 'c':

            assert param["exp_type_folder"] == "E:\\omer\\clustering"
            assert param["exp_var_change_folder"] == "E:\\omer\\clustering\\max_iter_barycenter_change_555"
            assert param["exp_folder_path_1"] == "E:\\omer\\clustering\\" \
                                                 "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_10, metric dtw," \
                                                 " down_sample_factor , 2, number of subjects 29"

            assert param["exp_folder_path_2"] == "E:\\omer\\clustering\\" \
                                                 "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_40, metric dtw," \
                                                 " down_sample_factor , 2, number of subjects 29"

            assert param["exp_folder_path_3"] == "E:\\omer\\clustering\\" \
                                                 "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_80, metric dtw," \
                                                 " down_sample_factor , 2, number of subjects 29"

            assert param["exp_folder_path_4"] == "E:\\omer\\clustering\\" \
                                                 "max_iter_barycenter_change_555\\n_init_2, max_iter_barycenter_160, metric dtw," \
                                                 " down_sample_factor , 2, number of subjects 29"

# if param["var_change"] == "i":
    #         assert param["exp_type_folder"] == "E:\\omer\\elbow_method"
    #         assert param["var_change_folder"] == "E:\\omer\\elbow_method\\init_change_2"
    #
    #         assert param["exp_folder_path_1"] == "E:\\omer\\elbow_method\\" \
    #                                            "init_change_2\\n_init_2, max_iter_barycenter_10, metric dtw," \
    #                                            " down_sample_factor , 2, number of subjects 29"
    #
    #     elif param["var_change"] == "b":
    #         assert param["exp_type_folder"] == "E:\\omer\\elbow_method\\"
    #         assert param["var_change_folder"] == "E:\\omer\\elbow_method\\max_iter_barycenter_change2"
    #
    #         assert param["exp_folder_path"] == "E:\\omer\\elbow_method\\" \
    #                                            "barycenter_change2\\n_init_2, max_iter_barycenter_10, metric dtw," \
    #                                            " down_sample_factor , 2, number of subjects 29"
    #
    #
    #


test_config()
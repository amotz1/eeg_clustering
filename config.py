import os
from utils import check_param
from utils import create_exp_spec


def config(param):

    exp_type = input("what type of experiment you want to do? "
                     "(e for elbow method and c for clustering ec  for both if both specific)")

    var_change = input("what type of variable you want to change? "
                       "(i for changing n_init_and b for changing max_iter_barycenter or s for specific)")

    print(param["data"].shape)
    number_of_subjects = param["data"].shape[0]

    param["number_of_subjects"] = number_of_subjects
    param["exp_type"] = exp_type
    param["var_change"] = var_change

    check_param(param)

    if param['exp_type'] == "e":
        exp_type_folder_name = "elbow_method"
        exp_type_folder = param["home_folder"] + "\\" + exp_type_folder_name
        exp_cond_folder = exp_type_folder + "\\" + param["num_cond"]

        if not os.path.exists(exp_type_folder):
            os.mkdir(exp_type_folder)
            os.chdir(exp_type_folder)

        if not os.path.exists(exp_cond_folder):
            os.mkdir(exp_cond_folder)
            os.chdir(exp_cond_folder)

        param['exp_type_folder'] = exp_type_folder
        param['exp_cond_folder'] = exp_cond_folder

    elif param['exp_type'] == "c":
        exp_type_folder_name = "clustering"
        exp_type_folder = param["home_folder"] + "\\" + exp_type_folder_name
        exp_cond_folder = exp_type_folder + "\\" + param["num_cond"]

        if not os.path.exists(exp_type_folder):
            os.mkdir(exp_type_folder)
            os.chdir(exp_type_folder)

        if not os.path.exists(exp_cond_folder):
            os.mkdir(exp_cond_folder)
            os.chdir(exp_cond_folder)

        param['exp_type_folder'] = exp_type_folder
        param['exp_cond_folder'] = exp_cond_folder

    else:
        print("unspecified experiment type")

    if param["var_change"] == "i":
        exp_var_change_name = "n_init_change_" + str(param["exp_number"])
        exp_var_change_folder = param['exp_cond_folder'] + '\\' + exp_var_change_name
        param['exp_var_change_folder'] = exp_var_change_folder

        os.mkdir(exp_var_change_folder)
        os.chdir(exp_var_change_folder)

        for n_init_ind in range(len(param["n_init"])):
            exp_folder_name = "n_init_" + str(param["n_init"][n_init_ind])

            exp_folder_path = exp_var_change_folder + "\\" + exp_folder_name
            os.mkdir(exp_folder_path)
            exp_folder_path_key = 'exp_folder_path_{n_init_ind}'.format(n_init_ind=n_init_ind + 1)
            param[exp_folder_path_key] = exp_folder_path
            create_exp_spec(param)

    elif param["var_change"] == "b":
        exp_var_change_name = "max_iter_barycenter_change_" + str(param["exp_number"])
        exp_var_change_folder = param['exp_cond_folder'] + "\\" + exp_var_change_name
        param['exp_var_change_folder'] = exp_var_change_folder
        os.mkdir(exp_var_change_folder)

        for max_iter_id in range(len(param['max_iter_barycenter'])):
            exp_folder_name = "max_iter_barycenter_" + str(param["max_iter_barycenter"][max_iter_id])

            exp_folder_path = exp_var_change_folder + "\\" + exp_folder_name
            os.mkdir(exp_folder_path)
            exp_folder_path_key = 'exp_folder_path_{max_iter_id}'.format(max_iter_id=max_iter_id + 1)
            param[exp_folder_path_key] = exp_folder_path
            create_exp_spec(param)

    elif param["var_change"] == "s":
        exp_var_change_name = "specific_" + str(param["exp_number"])
        exp_var_change_folder = param["exp_cond_folder"] + "\\" + exp_var_change_name
        param["exp_var_change_folder"] = exp_var_change_folder

        os.mkdir(exp_var_change_folder)

        param['exp_folder_path'] = exp_var_change_folder
        os.chdir(param['exp_folder_path'])
        create_exp_spec(param)

    else:
        print("unspecified experiment")

    return param

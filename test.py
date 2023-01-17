import pickle
import os
import matplotlib.pyplot as plt

def loading_results():

    print(os.getcwd())
    silhouette_avgs = open("E:\\omer\\elbow_method\\cond_2\\specific_1\\silhouette_avgs", "rb")
    centroids = [2,3,4,5,6,7]

    silhouette_avgs = pickle.load(silhouette_avgs)
    print(silhouette_avgs)

    plt.plot(centroids, silhouette_avgs, 'bx-')
    plt.show()
    plt.savefig("E:\\omer\\elbow_method\\cond_2\\specific_1" + "\\" + "silhouette_avgs1.png")


loading_results()
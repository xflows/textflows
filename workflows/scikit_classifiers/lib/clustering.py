
def sc_kmeans(input_dict):
    """
    The KMeans algorithm clusters data by trying to separate samples in n groups of equal variance,
    minimizing a criterion known as the inertia <inertia> or within-cluster sum-of-squares.
    This algorithm requires the number of clusters to be specified. It scales well to large number
    of samples and has been used across a large range of application areas in many different fields.

    :param input_dict (default): {u'max_iter': u'300', u'tol': u'1e-4', u'n_clusters': u'8'}
    :param n_clusters : int, optional, default: 8. The number of clusters to form as well as the number of
    centroids to generate.
    :param max_iter : int, default: 300. Maximum number of iterations of the k-means algorithm for a single run.
    :param tol : float, default: 1e-4. Relative tolerance with regards to inertia to declare convergence

    :return: scikit clustering
    """
    from sklearn import cluster
    clustering = cluster.KMeans(n_clusters=int(input_dict['n_clusters']),
                                max_iter=int(input_dict['max_iter']),
                                tol=float(input_dict['tol']))
    return {"clustering": clustering}

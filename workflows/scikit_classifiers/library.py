
def sc_gaussian_nb(input_dict):
    """
    Gaussian Naive Bayes.  When dealing with continuous data, a typical assumption is that the continuous
    values associated with each class are distributed according to a Gaussian distribution.

    :param input_dict (default): {}

    :return: scikit classifier
    """

    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    return {'classifier': classifier}


def sc_multinomial_nb(input_dict):
    """
    The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts
    for text classification). The multinomial distribution normally requires integer feature counts. However, in
    practice, fractional counts such as tf-idf may also work.

    :param input_dict (default): {u'alpha': u'1.0', u'fit_prior': u''}
    :param alpha (float): Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).

    :return: scikit classifier
    """
    from sklearn.naive_bayes import MultinomialNB

    try:
        alpha = float(input_dict["alpha"])
    except Exception:
        raise Exception("Parameter alpha should be numeric.")
    fit_prior = input_dict["fit_prior"] == u"true"

    classifier = MultinomialNB(alpha=alpha, fit_prior=fit_prior)
    return {'classifier': classifier}


def sc_linear_svc(input_dict):
    """
    Linear Support Vector Classification. Similar to SVC with parameter kernel=linear,
    but implemented in terms of liblinear rather than libsvm, so it has more flexibility
    in the choice of penalties and loss functions and should scale better (to large numbers of samples).

    :param input_dict (default): {u'penalty': u'l2', u'loss': u'l2', u'C': u'1.0', u'multi_class': u'ovr'}
    :param C : float, optional (default=1.0) Penalty parameter C of the error term.
    :param loss : string, l1 or l2 (default=l2) Specifies the loss function. l1 is the hinge loss (standard SVM) while
    l2 is the squared hinge loss.
    :param penalty : string, l1 or l2 (default=l2) Specifies the norm used in the penalization. The l2 penalty is
    the standard used in SVC. The l1 leads to coef_ vectors that are sparse.
    :param multi_class: string, ovr or crammer_singer (default=ovr): Determines the multi-class strategy if y contains
    more than two classes. ovr trains n_classes one-vs-rest classifiers, while crammer_singer optimizes a joint
    objective over all classes. While crammer_singer is interesting from an theoretical perspective as it is consistent
    it is seldom used in practice and rarely leads to better accuracy and is more expensive to compute. If crammer_singer
    is chosen, the options loss, penalty and dual will be ignored.

    :return: scikit classifier
    """
    from sklearn.svm import LinearSVC
    print input_dict

    classifier = LinearSVC(C=float(input_dict["C"]),
                           loss=input_dict["loss"],
                           penalty=input_dict["penalty"],
                           multi_class=input_dict["multi_class"])

    return {'classifier': classifier}


def sc_svc(input_dict):
    """
    Implementation of Support Vector Machine classifier using libsvm: the kernel can be non-linear but its SMO algorithm
    does not scale to large number of samples as LinearSVC does. Furthermore SVC multi-class mode is implemented using
    one vs one scheme while LinearSVC uses one vs the rest.

    :param input_dict (default): {u'kernel': u'rbf', u'C': u'1.0', u'degree': u'3'}
    :param C : float, optional (default=1.0). Penalty parameter C of the error term.
    :param kernel : string, optional (default=rbf). Specifies the kernel type to be used in the algorithm.
    It must be one of linear, poly, rbf, sigmoid, precomputed or a callable. If none is given, rbf will be used.
    If a callable is given it is used to precompute the kernel matrix.
    :param degree : int, optional (default=3). Degree of the polynomial kernel function (poly).
    Ignored by all other kernels.

    :return: scikit classifier
    """
    from sklearn.svm import SVC
    classifier = SVC(C=float(input_dict["C"]),
                      kernel=str(input_dict["kernel"]),
                      degree=int(input_dict["degree"]))
    return {'classifier': classifier}


def sc_knn(input_dict):
    """

    :param input_dict (input): {u'n_neighbors': u'5', u'weights': u'uniform', u'algorithm': u'auto'}
    :param n_neighbors : int, optional (default = 5). Number of neighbors to use by default for k_neighbors queries.
    :param weights : str or callable. weight function used in prediction.
    Possible values:
    uniform : uniform weights. All points in each neighborhood are weighted equally.
    distance : weight points by the inverse of their distance. in this case, closer neighbors of a query point will have
    a greater influence than neighbors which are further away.
    :param algorithm : {auto, ball_tree, kd_tree, brute}, optional

    :return: scikit classifier
    """
    from sklearn.neighbors import KNeighborsClassifier

    classifier = KNeighborsClassifier(n_neighbors=int(input_dict['n_neighbors']),
                                      weights=input_dict['weights'],
                                      algorithm=input_dict['algorithm'])

    return {'classifier': classifier}

























def sc_naivebayes(input_dict):
    """
    Naive Bayes classifiers are a family of simple probabilistic classifiers based on applying Bayes' theorem with strong
    (naive) independence assumptions between the features.

    :param input_dict (default): {u'alpha': u'1.0', u'type': u'gaussian_nb'}
    :param type: gaussian_nb or multinomial_nb
    :param alpha (float): Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).
    Parameter is only used with Multinomial naive Bayes. Default 1.0
    :return: scikit classifier
    """

    from sklearn.naive_bayes import GaussianNB
    from sklearn.naive_bayes import MultinomialNB

    try:
        alpha = float(input_dict["alpha"])
    except Exception:
        raise Exception("Parameter alpha should be numeric.")

    if input_dict["type"] == "gaussian_nb":
        classifier = GaussianNB()
    elif input_dict["type"] == "multinomial_nb":
        classifier = MultinomialNB(alpha=alpha)
    return {'classifier': classifier}
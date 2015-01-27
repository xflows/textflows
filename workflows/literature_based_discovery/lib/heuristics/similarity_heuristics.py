__author__ = 'matic'

from memoizator import memoized
#from sklearn.neighbors.nearest_centroid import NearestCentroid
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityBasedHeuristicCalculations():
    # def calculate_centroids(self):
    #     from scipy.sparse import hstack, vstack
    #     from scipy.cluster.hierarchy import centroid
    #     #vstack((count_A,count_C))
    #
    #     clf = NearestCentroid()
    #     clf.fit(vstack((tfidf_A, tfidf_C)), np.concatenate((classes_C, classes_A)))
    #
    #     centroid_A_idx = list(clf.classes_).index(A_class)
    #     centroid_C_idx = list(clf.classes_).index(C_class)
    #     tfidf_centroid_A = clf.centroids_[centroid_A_idx]
    #     tfidf_centroid_C = clf.centroids_[centroid_C_idx]

    @memoized
    def _tfidf_matrix_mean(self):
        return self._tfidf_matrix().mean(axis=1).transpose()

    @memoized
    def _tfidf_mean_A(self):
        '''average term on A's csr matrix'''
        return self._tfidf_A().mean(axis=1).transpose()

    @memoized
    def _tfidf_mean_C(self):
        '''average term on C's csr matrix'''
        return self._tfidf_C().mean(axis=1).transpose()


    ###SIMILARITY BASED HEURISTICS
    @memoized
    def _sim_cos_U(self):
        #return cosine_similarity(self._tfidf_matrix_csc().transpose(), self._tfidf_matrix_mean())
        return np.array(cosine_similarity(self._tfidf_matrix_csc().transpose(), self._tfidf_matrix_mean()).transpose()[0])


    @memoized
    def _sim_cos_A(self):
        return np.array(cosine_similarity(self._tfidf_A_csc().transpose(), np.array(self._tfidf_mean_A())).transpose()[0])

    @memoized
    def _sim_cos_C(self):
        return np.array(cosine_similarity(self._tfidf_C_csc().transpose(), self._tfidf_mean_C()).transpose()[0])

    @memoized
    def sim_avg_term(self):
        '''Similarity to an average term - the distance from the center of the cluster of all terms'''
        return self._sim_cos_U()

    @memoized
    def sim_domn_prod(self):
        '''Product of a term's similarity to the centroids of both domains'''
        return self._sim_cos_A() * self._sim_cos_C()

    @memoized
    def sim_domn_ratio_min(self):
        '''Minimum of a term's frequencies ratio between both domains'''
        return np.minimum(np.true_divide(self._sim_cos_A(), self._sim_cos_C()),
                                np.true_divide(self._sim_cos_C(), self._sim_cos_A()))


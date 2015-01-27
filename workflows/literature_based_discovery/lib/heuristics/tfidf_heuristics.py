__author__ = 'matic'

from memoizator import memoized
import numpy as np

class TfIdfBasedHeuristicCalculations():
    # def __init__(self,raw_documents, classes):
    #     super(raw_documents, classes)
    #
    #     #TFIDF
    #
    #     self.tfidf_matrix = TfidfTransformer().fit_transform(self._count_matrix)  # tf-idf on entire matrix
    #     self.tfidf_A = TfidfTransformer().fit_transform(self._count_A)
    #     self.tfidf_C = TfidfTransformer().fit_transform(self._count_C)

    @memoized
    def _tfidf_matrix(self):
        '''tf-idf on entire matrix'''
        return self._bow_model._tfidf_transformer().fit_transform(self._count_matrix)

    @memoized
    def _tfidf_A(self):
        '''tf-idf on domain A'''
        return self._bow_model._tfidf_transformer().fit_transform(self._count_A)

    @memoized
    def _tfidf_C(self):
        '''tf-idf on domain C'''
        return self._bow_model._tfidf_transformer().fit_transform(self._count_C)
        #return TfidfTransformer().fit_transform(self._count_C)

    @memoized
    def _tfidf_matrix_csc(self):
        return self._tfidf_matrix().tocsc()

    @memoized
    def _tfidf_A_csc(self):
        return self._tfidf_A().tocsc()

    @memoized
    def _tfidf_C_csc(self):
        return self._tfidf_C().tocsc()

    #not memoized
    def _tfidf_D(self,csc_tfidf_matrix):
        '''represents the tf-idf weight of a term in the centroid (average document from D)'''
        return np.array(csc_tfidf_matrix.mean(axis=0))[0]

    ###TF-IDF BASED HEURISTICS
    @memoized
    def tfidf_sum(self):
        '''sum of all tf idf weights of a term across both domains'''
        return np.array(self._tfidf_matrix_csc().sum(axis=0))[0]

    @memoized
    def tfidf_avg(self):
        '''average tf idf of a term'''
        return np.true_divide(self.tfidf_sum(), self._count_doc_D(self._count_matrix_csc()))  #TODO: duplicate count

    @memoized
    def tfidf_domn_prod(self):
        '''product of a term's importance in both domains'''
        return self._tfidf_D(self._tfidf_A_csc()) * self._tfidf_D(self._tfidf_C_csc())

    @memoized
    def tfidf_domn_sum(self):
        '''sum of a term's importance in both domains'''
        return self._tfidf_D(self._tfidf_A_csc()) + self._tfidf_D(self._tfidf_C_csc()) #TODO duplicate with tfidf_domn_prod

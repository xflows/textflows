from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC
from workflows.textflows import BowDataset

__author__ = 'matic'

from memoizator import memoized
import numpy as np
from misclassification_indices import MisclassificationIndices

###OUTLIER BASED HEURISITCS
from sklearn.neighbors import  NearestCentroid


class OutlierBasedHeuristicCalculations():
    @memoized
    def _d_cs_indices(self):
        classifier=NearestCentroid(metric='cosine')
        #classifier=KNeighborsClassifier(n_neighbors=5)
        return MisclassificationIndices.calculate(classifier,
                                                  BowDataset(self._tfidf_matrix(),self._classes),
                                                  n_folds=10)['inds']
    @memoized
    def _d_rf_indices(self):
        classifier = RandomForestClassifier()
        return MisclassificationIndices.calculate(classifier,
                                                  BowDataset(self._tfidf_matrix(),self._classes),
                                                  n_folds=10)['inds']
    @memoized
    def _d_svm_indices(self):
        classifier = LinearSVC()
        return MisclassificationIndices.calculate(classifier,
                                                  BowDataset(self._tfidf_matrix(),self._classes),
                                                  n_folds=10)['inds']

    #not memoized
    def _count_matrix_D_cs_csc(self):
        return self._count_matrix_csc()[self._d_cs_indices()]

    #not memoized
    def _count_matrix_D_rf_csc(self):
        return self._count_matrix_csc()[self._d_rf_indices()]

    #not memoized
    def _count_matrix_D_svm_csc(self):
        return self._count_matrix_csc()[self._d_svm_indices()]


    #not memoized
    def _count_term_D_cs(self):
        return self._count_term_D(self._count_matrix_D_cs_csc())

    #not memoized
    def _count_term_D_rf(self):
        return self._count_term_D(self._count_matrix_D_rf_csc())

    #not memoized
    def _count_term_D_svm(self):
        return self._count_term_D(self._count_matrix_D_svm_csc())

    @memoized
    def out_freq_cs(self):
        '''Term frequency in the Centroid Similarity outlier set'''
        return self._count_term_D_cs()+10**-10

    @memoized
    def out_freq_rf(self):
        '''Term frequency in the Random Forest outlier set'''
        return self._count_term_D_rf()+10**-10

    @memoized
    def out_freq_svm(self):
        '''Term frequency in the Support Vector Machine outlier set'''
        return self._count_term_D_svm()+10**-10

    @memoized
    def out_freq_sum(self):
        '''Sum of term frequencies in all three outlier sets'''
        return self.out_freq_cs() + self.out_freq_rf() + self.out_freq_svm()

    @memoized
    def out_freq_rel_cs(self):
        '''Relative frequency in the Centroid Similarity outlier set'''
        return np.true_divide(self.out_freq_cs(), self.tf())

    @memoized
    def out_freq_rel_rf(self):
        '''Relative frequency in the Random Forest outlier set'''
        return np.true_divide(self.out_freq_rf(), self.tf())


    @memoized
    def out_freq_rel_svm(self):
        '''Relative frequency in the Support Vector Machine outlier set'''
        return np.true_divide(self.out_freq_svm(), self.tf())

    @memoized
    def out_freq_rel_sum(self):
        '''Sum of relative frequencies in all three outlier sets'''
        return np.true_divide(self.out_freq_sum(), self.tf())


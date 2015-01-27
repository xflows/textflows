__author__ = 'matic'

from memoizator import memoized
import numpy as np


class FrequencyBasedHeuristicCalculations():
    @memoized
    def _count_term_A(self):
        return self._count_term_D(self._count_A_csc())

    @memoized
    def _count_term_C(self):
        return self._count_term_D(self._count_C_csc())


    ###FREQUENCY BASED HEURISTICS
    @memoized
    def freq_ratio(self):
        '''Term to document frequency ratio'''
        return np.true_divide(self.tf(), self.freq_doc())

    @memoized
    def freq_domn_ratio_min(self):
        '''Minimum of term frequencies ratio between both domains'''
        np.seterr(divide='ignore')  #, invalid='ignore')
        return np.minimum(np.true_divide(self._count_term_A(), self._count_term_C()),
                                 np.true_divide(self._count_term_C(), self._count_term_A()))

    @memoized
    def freq_domn_prod(self):
        '''Product of term frequencies in both domains'''
        return self._count_term_A() * self._count_term_C()

    @memoized
    def freq_domn_prod_rel(self):
        '''Product of term frequencies in both domains relative to the term frequency in all domains'''
        return np.true_divide(self.freq_domn_prod(), self.tf())

    ###BASELINE HEURISITCS
    def random(self):
        '''Random baseline heuristic'''
        return np.random.rand(self._count_matrix.shape[0])

    def appear_in_all_domains(self):
        '''Better baseline heuristic which can separate two classes of terms - the ones that appear in both domains and the ones that appear only in one'''
        return np.array((self._count_term_A() > 0) & (self._count_term_C() > 0), dtype=int) + \
                        np.true_divide(np.random.rand(len(self._count_term_A())), 2)

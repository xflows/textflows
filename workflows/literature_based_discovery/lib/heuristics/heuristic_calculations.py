__author__ = 'matic'

from memoizator import memoized


import numpy as np
from frequency_heuristics import FrequencyBasedHeuristicCalculations
from tfidf_heuristics import TfIdfBasedHeuristicCalculations
from similarity_heuristics import SimilarityBasedHeuristicCalculations
from outlier_heuristics import OutlierBasedHeuristicCalculations


class HeuristicCalculations(FrequencyBasedHeuristicCalculations,
                            TfIdfBasedHeuristicCalculations,
                            SimilarityBasedHeuristicCalculations,
                            OutlierBasedHeuristicCalculations,
                            ):
    __A_class = 1
    __C_class = 0

    def __init__(self, raw_documents, classes,bow_model):
        # CALCULATE COUNT MATRIX FOR ENTIRE DATASET
        self._bow_model = bow_model
        self._count_matrix = bow_model._count_vectorizer().transform(raw_documents)
        self._classes=np.array(classes)

        #DEVIDE COUNT MATRIX BY CLASS
        idx_A = np.where(self._classes == self.__A_class)[0]
        idx_C = np.where(self._classes == self.__C_class)[0]
        try:
            self._count_A = self._count_matrix[idx_A]
            self._count_C = self._count_matrix[idx_C]
        except ValueError:
            raise Exception("One of domains appears not to contain any documents. "+\
                  "This usually happens because of wrong class settings in the Construct Bow Model widget.")


    @memoized
    def _count_A_csc(self):
        # if self._count_A_csc is None:
        #    self._count_A_csc=\
        return self._count_A.tocsc()
        #return self._count_A_csc

    @memoized
    def _count_C_csc(self):
        return self._count_C.tocsc()

    @memoized
    def _count_matrix_csc(self):
        return self._count_matrix.tocsc()

    #not memoized
    def _count_term_D(self,csc_count_matrix):
        '''returns number of occurances of every term from'''
        return np.array(csc_count_matrix.sum(axis=0))[0]

    #not memoized
    def _count_doc_D(self,csc_count_matrix):
        '''counts the number of documents in which a term appears'''
        return np.diff(csc_count_matrix.indptr)

    @memoized
    def tf(self):
        '''Term frequency across both domains'''
        return self._count_term_D(self._count_matrix_csc())

    @memoized
    def freq_doc(self):
        '''Document frequency across both domains'''
        return self._count_doc_D(self._count_matrix_csc())


    def calculate_heuristics(self, heuristic_names):
        if isinstance(heuristic_names, basestring):
            scores=getattr(self,heuristic_names)()
            return BTermHeuristic(heuristic_names,scores)
        elif isinstance(heuristic_names, tuple):
            if heuristic_names[0] == 'Sum':
                return self.calculate_heuristic_sum(heuristic_names[1])
            elif heuristic_names[0]=='Vote':
                return self.calculate_heuristic_votes(heuristic_names[1])

        elif isinstance(heuristic_names, list):
            return [self.calculate_heuristics(heuristic_name) for heuristic_name in heuristic_names]
        return None

    def calculate_heuristic_sum(self, heuristic_names):
        heuristics = [self.calculate_heuristics( heuristic_name) for heuristic_name in heuristic_names]
        name = "Sum(" + ",".join([heuristic.name for heuristic in heuristics]) + ")"
        scores = np.array([heuristic.scores for heuristic in heuristics]).sum(axis=0)
        return BTermHeuristic(name, scores)

    def calculate_heuristic_votes(self,heuristic_names):
        heuristics = [self.calculate_heuristics(heuristic_name) for heuristic_name in heuristic_names]
        name = "Vote(" + ",".join([heuristic.name for heuristic in heuristics]) + ")"
        voting_scores = []
        position_scores = []

        for h in heuristics:
            positions = h.scores.argsort().argsort() + 1  #double argsort: position on in the spot of the element
            h_voting_scores = np.array(positions > len(positions) * 2 / 3.0, dtype=int)
            h_position_scores = (len(positions) - positions) / (len(positions) * 1. * len(heuristics))

            voting_scores.append(h_voting_scores)
            position_scores.append(h_position_scores)
        scores = np.array(voting_scores + position_scores).sum(axis=0)

        return BTermHeuristic(name, scores)

    def _calculate_all(self):
        basic_h_names=[a for a in dir(self) if not a.startswith('_') and not a.startswith("calculate")]
        hevristic_names=basic_h_names+[('Sum',basic_h_names),('Vote',basic_h_names)]

        return self.calculate_heuristics(hevristic_names)



class BTermHeuristic:
    def __init__(self, name, scores,votes=None):
        self.name = name
        self.scores = scores
        self.votes=votes if votes else self._calculate_votes()

    def _calculate_votes(self):
        positions = self.scores.argsort().argsort() + 1  #double argsort: position on in the spot of the element
        return np.array(positions > len(positions) * 2 / 3.0, dtype=int)

    def __repr__(self):
        return '<BTermHeuristic name: %s>' % (self.name)
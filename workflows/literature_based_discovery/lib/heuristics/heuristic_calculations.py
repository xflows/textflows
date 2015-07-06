from scipy.stats import rankdata
from workflows.textflows import flatten

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

    def __init__(self, raw_documents, classes,bow_model,stress_idx=None):
        # CALCULATE COUNT MATRIX FOR ENTIRE DATASET
        self._bow_model = bow_model
        self._count_matrix = bow_model._count_vectorizer().transform(raw_documents)
        self._classes=np.array(classes)
        self.stress_idx=stress_idx
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



    def _penalize_not_appearing_in_all(self,scores):
        not_in_all=np.where(self._appear_in_all_domains()==0)
        scores[not_in_all]=0
        return scores


    def calculate_heuristics(self, heuristic_names):
        if isinstance(heuristic_names, basestring):
            scores=self._penalize_not_appearing_in_all(getattr(self,heuristic_names)())
            #scores=getattr(self,heuristic_names)()
            return BTermHeuristic(heuristic_names,scores)
        elif isinstance(heuristic_names, tuple):
            if heuristic_names[0] in ['Sum','Min','Max']:
                return self.calculate_heuristic_func(heuristic_names[1],heuristic_names[0])
            elif heuristic_names[0]=='Norm':
                return self.calculate_heuristic_norm(heuristic_names[1])
            elif heuristic_names[0]=='Vote':
                return self.calculate_ensemble_heuristic_votes(heuristic_names[1])
            elif heuristic_names[0]=='AvgPos':
                return self.calculate_ensemble_average_position(heuristic_names[1])

        elif isinstance(heuristic_names, list):
            return [self.calculate_heuristics(heuristic_name) for heuristic_name in heuristic_names]
        return None

    def calculate_heuristic_func(self, heuristic_names,function):
        heuristics = [self.calculate_heuristics( heuristic_name) for heuristic_name in heuristic_names]
        name = function+"(" + ",".join([heuristic.name for heuristic in heuristics]) + ")"
        scores = getattr(np.array([heuristic.scores for heuristic in heuristics]),function.lower())(axis=0)
        return BTermHeuristic(name, scores)


    def calculate_heuristic_norm(self, heuristic_name):
        heuristic = self.calculate_heuristics( heuristic_name)
        name = "Norm("+heuristic.name+ ")"
        xmin =  heuristic.scores.min(axis=0)
        scores= (heuristic.scores - xmin) / (heuristic.scores.max(axis=0) - xmin)
        return BTermHeuristic(name, scores)

    def calculate_ensemble_heuristic_votes(self,heuristic_names):
        heuristics = [self.calculate_heuristics(heuristic_name) for heuristic_name in heuristic_names]
        name = "Vote(" + ",".join([heuristic.name for heuristic in heuristics]) + ")"
        terms_in_both_domains_count=np.count_nonzero(self._appear_in_all_domains())
        voting_scores = [ h.votes(terms_in_both_domains_count) for h in heuristics]
        #voting_pos = [ h.positions() for h in heuristics]
        #stress_votes=[vs[self.stress_idx] for vs in voting_scores]
        #stress_pos=[vs[self.stress_idx] for vs in voting_pos]
        scores=np.array(voting_scores).sum(axis=0)
        return BTermHeuristic(name, scores )

    def calculate_ensemble_average_position(self,heuristic_names):
        heuristics = [self.calculate_heuristics(heuristic_name) for heuristic_name in heuristic_names]
        name = "AvgPos(" + ",".join([heuristic.name for heuristic in heuristics]) + ")"
        position_scores = []

        for h in heuristics:
            positions = h.positions()
            h_position_scores = positions / (len(positions) * 1.)

            position_scores.append(h_position_scores)
        scores = np.array(position_scores).mean(axis=0)

        return BTermHeuristic(name, scores)

    def _calculate_all(self):
        basic_h_names=[a for a in dir(self) if not a.startswith('_') and not a.startswith("calculate")]
        hevristic_names=basic_h_names+[('Sum',basic_h_names),('Vote',basic_h_names)]

        return self.calculate_heuristics(hevristic_names)



class BTermHeuristic:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        #self.votes=votes if votes else self._calculate_votes()

    def votes(self,num_of_terms_in_both_domains):
        positions = self.positions()  #double argsort: position on in the spot of the element
        print num_of_terms_in_both_domains
        print self.positions().shape[0]
        top_terms_ratio=num_of_terms_in_both_domains/(3.*self.positions().shape[0])
        print top_terms_ratio
        #return np.array(positions >= positions[int(len(positions) * 2 / 3.0)-1],dtype=int)
        #a=np.percentile(positions, 200./3)
        #non_zero_scores=np.array(self.scores>0,dtype=int)
        print 100*(1-top_terms_ratio)
        print self.positions().shape[0]*(1-top_terms_ratio)
        print int(self.positions().shape[0]*(1-top_terms_ratio))

        print "dfd"
        print np.percentile(positions, 100*(1-top_terms_ratio))
        #return np.array(positions >= np.percentile(positions, 100*(1-top_terms_ratio)),dtype=int)#*non_zero_scores
        return np.array(positions >= int(self.positions().shape[0]*(1-top_terms_ratio)),dtype=int)#*non_zero_scores

    def positions(self):
        ''' Ranks scores, from the smallest to the largest score
            Out[22]: array([1, 1, 1, 1, 5, 6, 7, 8, 9])
            In[23]: rankdata(a,'average')
            Out[23]: array([ 2.5,  2.5,  2.5,  2.5,  5. ,  6. ,  7. ,  8. ,  9. ])
        '''
        return rankdata(self.scores,'average')
        #return self.scores.argsort().argsort() + 1

    def __repr__(self):
        return '<BTermHeuristic name: %s>' % (self.name)
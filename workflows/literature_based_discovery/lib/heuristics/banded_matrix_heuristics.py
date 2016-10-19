# from sklearn.ensemble import RandomForestClassifier
# from sklearn.svm import SVC, LinearSVC
import copy
import scipy
from scipy.sparse import csr_matrix, rand
from workflows.literature_based_discovery.lib.heuristics.band_matrices import alternatingBi
# from workflows.textflows import BowDataset
from workflows.literature_based_discovery.lib.heuristics.memoizator import memoized
import numpy as np
__author__ = 'matic'
#
# from memoizator import memoized
# import numpy as np
# from misclassification_indices import MisclassificationIndices
#
# ###OUTLIER BASED HEURISITCS
# from sklearn.neighbors import  NearestCentroid
# import os
# import sys,string
# print os.getcwd()
# from collections import defaultdict
# from math import log
# from diagonalization_helpers import *
#from pyroc import ROCData,plot_multiple_roc
# from scipy.sparse import lil_matrix, csr_matrix
# from scipy.sparse import lil_matrix
# from scipy.sparse.linalg import spsolve
# from numpy.linalg import solve, norm
# from numpy.random import rand
#
# import time
# import numpy as np
# from PIL import Image, ImageDraw

class BandedMatrixBasedHeuristicCalculations():



    # def load_sparse(filename):
    #     # centers = []
    #     nz = 0
    #     with open('initsp.dat', 'r') as f:
    #         line = f.readline().split(',')
    #         nRows = int(line[0])
    #         nCols = int(line[1])
    #         matrix = lil_matrix((nRows, nCols))
    #         i=0
    #         for line in f:
    #             l = line.split(',')
    #             nz += len(l)
    #             matrix[i, l] = 1
    #             print l
    #             # centers.append(sum([int(x) for x in l]) * 1.0 / len(l))
    #             i += 1
    #     # print "Number of nonzero values: %i" % nz
    #     return np.array(matrix) #.tocsr()

    # def load_types(filename, type1):
    #     types = []
    #     with open(filename, 'r') as f:
    #         for line in f:
    #             a = line.split()
    #             types.append(1 if a[1] == type1 else 0)
    #     return types
    @memoized
    def _binary_matrix(self):
        '''tf-idf on entire matrix'''
        # a=rand(10,5,density=0.5,format='csr')
        # a.data=scipy.sign(a.data)
        # return a
        binary_matrix=csr_matrix(self._tfidf_matrix(),copy=True)
        binary_matrix.data=scipy.sign(binary_matrix.data)
        return binary_matrix

    @memoized
    def _greens_per_word(self):
        '''tf-idf on domain A'''
        idx_A = np.where(self._classes == self._HeuristicCalculations__A_class)[0]
        selected_matrix=self._binary_matrix()[idx_A]
        return np.array(selected_matrix.sum(axis=0))[0]

    @memoized
    def _blues_per_word(self):
        '''tf-idf on domain C'''
        idx_C = np.where(self._classes == self._HeuristicCalculations__C_class)[0]
        selected_matrix= self._binary_matrix()[idx_C]
        return np.array(selected_matrix.sum(axis=0))[0]


    @memoized
    def _banded_matrix(self):
        '''tf-idf on entire matrix'''
        return alternatingBi(self._binary_matrix(),50)

    @memoized
    def _greens_on_diag_per_word(self):
        '''tf-idf on domain A'''
        idx_A = np.where(self._classes == self._HeuristicCalculations__A_class)[0]
        _,fully_banded,_,column_permutation=self._banded_matrix()

        fully_banded_A=fully_banded[idx_A]
        print fully_banded_A.shape
        return np.array(self._reverse_column_permute(fully_banded_A,column_permutation).sum(axis=0))[0]

    @memoized
    def _blues_on_diag_per_word(self):
        '''tf-idf on domain C'''
        idx_C = np.where(self._classes == self._HeuristicCalculations__C_class)[0]
        _,fully_banded,_,column_permutation=self._banded_matrix()
        fully_banded_C=fully_banded[idx_C]
        return np.array(self._reverse_column_permute(fully_banded_C,column_permutation).sum(axis=0))[0]


    def test(self):
        # print "start\tOK"
        #
        #
        # #CONVERT DOCUMENT STRING TO
        # prefix=sys.argv[1]+"/"
        # print "File in:", prefix
        # #prefix='C:\\Users\\matic\\AppData\\Local\\Temp\\aahpoqs5.lcp\\'
        # dataset_file=open(prefix+"documents.lndoc", 'r')
        # line = dataset_file.readline()    # Invokes readline() method on file
        # text_per_document={}
        # class_per_document={}
        #
        #
        # i=0
        # count=0
        #
        # while line:
        #     if line!="\n" and i%1==0:
        #         spl=line.split("\t")
        #         class_per_document[count]=spl[1]
        #         text_per_document[count]=spl[2].split("\n")[0].split(" ")
        #         if "" in text_per_document[count]:
        #             text_per_document[count].remove("")
        #
        #         count+=1
        #     i+=1
        #     line = dataset_file.readline()
        # dataset_file.close()
        # classes=list(set(class_per_document.values()))
        #
        # #TF-IDF and BOW
        # words = set()
        # tf_idfs = {}
        #
        # for train in text_per_document.keys():
        #     for word in text_per_document[train]:
        #         words.add(word)
        #
        # word_count=defaultdict(int)
        # for document_text in text_per_document.values():
        #     for word in set(document_text):
        #         word_count[word]+=1
        #
        # len_train_text=len(text_per_document)
        # words_sorted_by_frequency=sorted(word_count.items(),key=lambda a: a[1],reverse=True)
        #
        #
        # #-----------------CALCULATE TF-IDFS-----------------
        # print "compute tf-idf"
        # for train, train_words in text_per_document.items():
        #     train_word_count=defaultdict(int)
        #     tf_idfs[train] = {}
        #     for word in train_words:
        #         train_word_count[word]+=1
        #
        #     for word,tf in train_word_count.items():
        #         idf = log(len_train_text / float(word_count[word]))
        #         tf_idfs[train][word] = tf * idf
        word_to_idx=self._bow_model.vectorizer.vocabulary

        print np.array(self._binary_matrix().sum(axis=0))[0]

        banded_matrix,fully_banded,row_permutation,column_permutation=self._banded_matrix()
        print np.array(self._reverse_column_permute(banded_matrix,column_permutation).sum(axis=0))[0]


        print banded_matrix.shape
        print fully_banded.shape
        print np.array(self._reverse_column_permute(fully_banded,column_permutation).sum(axis=0))[0]

        #sorted_words = sorted(list(words)) #TODO need to set
        #nums=0
        #tfnnull=0
        max_tfidf=banded_matrix.max()


        with_inverse=False
        inverse_only=False

        # if with_inverse:
        #     write_to_init_file_inv(class_per_document,text_per_document,sorted_words,prefix+"init.dat_inv")
        #     write_to_init_file(class_per_document,text_per_document,sorted_words,prefix+"init.dat")
        #     _,col_perm_rev_inv=get_permutations(prefix,filename=prefix+"init_inv.dat")
        #     col_perm_rev,row_perm_rev=get_permutations(prefix,filename=prefix+"init.dat")
        # elif inverse_only:
        #     col_perm_rev_inv=False
        #     write_to_init_file_inv(class_per_document,text_per_document,sorted_words,prefix+"init.dat_inv")
        #     col_perm_rev,row_perm_rev=get_permutations(prefix,filename=prefix+"init_inv.dat")
        # else:
        # col_perm_rev_inv=False
        # write_to_init_file(class_per_document,text_per_document,sorted_words,prefix+"init.dat")
        # col_perm_rev,row_perm_rev=get_permutations(prefix)
        #
        # col_perm={}
        # for k,v in col_perm_rev.items():
        #     col_perm[v]=k
        #
        # col_perm_inv=False
        # if col_perm_rev_inv:
        #     col_perm_inv={}
        #     for k,v in col_perm_rev_inv.items():
        #         col_perm_inv[v]=k


        #-----------------CROSSBEE SCORES-----------------
        jursic_word_score=False
        max_word_score=False

        #-----------------heuristicS-----------------
        # from heuristic_functions import *
        #
        # print len(sorted_words),len(row_perm_rev),len(col_perm_rev)
        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()

        b=33


    #heuristic #1:
    def heuristic1(self):
        '''no of documents of different colour than diag's colour'''

        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()
        greens_on_diag_per_word=self._greens_on_diag_per_word()
        blues_on_diag_per_word=self._blues_on_diag_per_word()
        #all_words=set(greens_on_diag_per_word.keys()+blues_on_diag_per_word.keys())

        scores=[]
        for i in range(len(greens_per_word)):
            if greens_on_diag_per_word[i]==0 or blues_on_diag_per_word[i]==0: #if diag has one color per word
                scores.append(greens_per_word[i] if greens_on_diag_per_word[i]==0 else blues_per_word[i])
            else:
                scores.append(0)

        #print word_scores
        return np.array(scores) #[[w,s*1./word_scores[0][1]] for w,s in word_scores]


    #heuristic #2:
    def heuristic2(self):
        '''no of documents of different colour than diag's colour divided by the number of documents on the diagonal of the selected colour'''
        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()
        greens_on_diag_per_word=self._greens_on_diag_per_word()
        blues_on_diag_per_word=self._blues_on_diag_per_word()

        scores=[]
        for i in range(len(greens_per_word)):
            if greens_on_diag_per_word[i]!=0 or blues_on_diag_per_word[i]!=0: #if diag has one color per word
                max_score=max(greens_on_diag_per_word[i], blues_on_diag_per_word[i])

                score=(blues_per_word[i] if greens_on_diag_per_word[i]==max_score else greens_per_word[i])*1./max_score
                scores.append(score)#greens_per_word[word] if greens_on_diag_per_word[word]==0 else blues_per_word[word]])
            else:
                scores.append(0)

        #print word_scores
        return np.array(scores) #[[w,s*1./word_scores[0][1]] for w,s in word_scores]



    #heuristic #3:
    def heuristic3(self):
        '''1/heuristic2'''
        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()
        greens_on_diag_per_word=self._greens_on_diag_per_word()
        blues_on_diag_per_word=self._blues_on_diag_per_word()

        scores=[]
        for i in range(len(greens_per_word)):
            if greens_on_diag_per_word[i]!=0 or blues_on_diag_per_word[i]!=0: #if diag has one color per word
                max_score=max(greens_on_diag_per_word[i], blues_on_diag_per_word[i])

                score=max_score*1./((blues_per_word[i] if greens_on_diag_per_word[i]==max_score else greens_per_word[i])+0.000000000000000000000001)
                scores.append(score)#greens_per_word[word] if greens_on_diag_per_word[word]==0 else blues_per_word[word]])
            else:
                scores.append(0)

        return np.array(scores) #[[w,s*1./word_scores[0][1]] for w,s in word_scores]



    #heuristic #4:
    def heuristic4(self):
        '''get color of diag, see the diag strength, diag_strength*ex_of_diff_colour/ex_of_diag_colou'''
        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()
        greens_on_diag_per_word=self._greens_on_diag_per_word()
        blues_on_diag_per_word=self._blues_on_diag_per_word()

        scores=[]
        for i in range(len(greens_per_word)):
            if greens_on_diag_per_word[i]!=0 or blues_on_diag_per_word[i]!=0: #if diag has one color per word
                max_score=max(greens_on_diag_per_word[i], blues_on_diag_per_word[i])
                print greens_per_word[i] , greens_on_diag_per_word[i],blues_per_word[i],blues_on_diag_per_word[i],max_score

                if (greens_per_word[i] if greens_on_diag_per_word[i]==max_score else blues_per_word[i])!=0:
                    score=max_score*1.*(blues_per_word[i] if greens_on_diag_per_word[i]==max_score else greens_per_word[i])/(greens_per_word[i] if greens_on_diag_per_word[i]==max_score else blues_per_word[i])
                else:
                    score=0
                scores.append(score)#greens_per_word[word] if greens_on_diag_per_word[word]==0 else blues_per_word[word]])
            else:
                scores.append(0)

        return np.array(scores) #[[w,s*1./word_scores[0][1]] for w,s in word_scores]

    def heuristic5(self):
        '''get color of diag, see the diag strength, diag_strength*ex_of_diff_colour/ex_of_diag_colou'''
        greens_per_word=self._greens_per_word()
        blues_per_word=self._blues_per_word()
        greens_on_diag_per_word=self._greens_on_diag_per_word()
        blues_on_diag_per_word=self._blues_on_diag_per_word()
        freq_ratio=self.freq_ratio()

        scores=[]
        for i in range(len(greens_per_word)):
            if greens_on_diag_per_word[i]!=0 or blues_on_diag_per_word[i]!=0: #if diag has one color per word
                max_score=max(greens_on_diag_per_word[i], blues_on_diag_per_word[i])
                print greens_per_word[i] , greens_on_diag_per_word[i],blues_per_word[i],blues_on_diag_per_word[i],max_score

                if (greens_per_word[i] if greens_on_diag_per_word[i]==max_score else blues_per_word[i])!=0:
                    score=max_score*1.*(blues_per_word[i] if greens_on_diag_per_word[i]==max_score else greens_per_word[i])/(greens_per_word[i] if greens_on_diag_per_word[i]==max_score else blues_per_word[i])
                else:
                    score=0
                scores.append(score)#greens_per_word[word] if greens_on_diag_per_word[word]==0 else blues_per_word[word]])
            else:
                scores.append(freq_ratio[i])

        return np.array(scores) #[[w,s*1./word_scores[0][1]] for w,s in word_scores]


        #calculate_colours(prefix,sorted_words,row_perm_rev,col_perm_rev,class_per_document,classes)
        # greens_on_diag_per_word,blues_on_diag_per_word=calculate_diag_colours(prefix,sorted_words,row_perm_rev,col_perm_rev,class_per_document,classes)
        # labels=['Hevristika1','Hevristika2','Hevristika3','Hevristika4']
        #
        #
        # heuristics=[heuristic1,heuristic2,heuristic3,heuristic4]
        # scores=[sorted(heuristic(greens_per_word,blues_per_word,greens_on_diag_per_word,blues_on_diag_per_word),key=lambda a: (1 if greens_per_word.get(a[0])!=0 and blues_per_word.get(a[0])!=0 else 0),reverse=True) for heuristic in heuristics]



        #b-term generation
        # if sell!="ideal_toy":
        #     b_term_list=['5_ht','5_hydroxytryptamine','5_hydroxytryptamine_receptor','anti_aggregation','anticonvulsant','anti_inflammatory','antimigraine','arterial_spasm','brain_serotonin','calcium_antagonist','calcium_blocker','calcium_channel','calcium_channel_blocker','cerebral_vasospasm','convulsion','convulsive','coronary_spasm','cortical_spread_depression','diltiazem','epilepsy','epileptic','epileptiform','hypoxia','indomethacin','inflammatory','nifedipine','paroxysmal','platelet_aggregation','platelet_function','prostacyclin','prostaglandin','prostaglandin_e1','prostaglandin_synthesis','reactivity','seizure','serotonin','spasm','spread','spread_depression','stress','substance_p','vasospasm','verapamil']
        #
        # b_terms=set(word for word in b_term_list if greens_per_word.get(word)!=0 and blues_per_word.get(word)!=0)
        #
        # print [(word,greens_per_word.get(word),blues_per_word.get(word)) for word in b_term_list]
        # print b_term_list
        # print b_terms
        b_terms=set([])
        #-----------------DRAW IMAGES-----------------
        # draw_matrix(sorted_words,jursic_word_score,max_word_score,identity_permutation(len(col_perm_rev)),identity_permutation(len(row_perm_rev)),class_per_document,
        #     prefix+"1_inital",prefix+"init",b_terms,{},classes)
        # draw_matrix(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,class_per_document,
        #     prefix+"2_after_col_perm",prefix+"min_flips_output_2_columns_permuted_matrix",b_terms,col_perm_inv,classes)
        # draw_matrix(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,class_per_document,
        #     prefix+"3_banded_matrix",prefix+"min_flips_output_6_visual_banded_matrix",b_terms,col_perm_inv,classes)
        # draw_matrix(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,class_per_document,
        #     prefix+"5_after_row_perm",prefix+"min_flips_output_7_original_banded_matrix",b_terms,col_perm_inv,classes)
        #
        #-----------------GENERATE JAVASCRIPT FILE-----------------

        #doc_outliers=find_domain_outliers(prefix,class_per_document)
        #generate_js_file(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,class_per_document,text_per_document,prefix,b_terms,greens_per_word,blues_per_word,classes,col_perm_rev_inv,col_perm_inv,doc_outliers)

        #-----------------PLOT ROC-----------------
        # print "Results"
        # #create image where word columns are sorted by heuristic4 scores
        # best_heuristic_scores_permutation={}
        # heuristic_4_words_by_score=[a[0] for a in scores[3]]
        # missing_j=len(heuristic_4_words_by_score)
        # for j,old_j in col_perm_rev.items():
        #     word=sorted_words[old_j]
        #     if word in heuristic_4_words_by_score:
        #         score_j=heuristic_4_words_by_score.index(word)
        #     else:
        #         score_j=missing_j
        #         missing_j+=1
        #
        # for word,score in scores[3]:
        #     print "%s\t%d" % (word,score)
        #
        # draw_matrix(sorted_words,jursic_word_score,max_word_score,col_perm_rev,row_perm_rev,class_per_document,
        #     prefix+"6_after_scores_perm",prefix+"min_flips_output_7_original_banded_matrix",b_terms,best_heuristic_scores_permutation,classes)


        #print json.dumps(word,score in scores[3])

    @staticmethod
    def _reverse_column_permute(matrix,column_permutation):
        reversed_column_permutations=np.argsort(column_permutation)
        return matrix[:,reversed_column_permutations]



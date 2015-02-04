from itertools import izip
from workflows.nltoolkit.lib.classification import train_classifier,apply_bow_classifier

__author__ = 'matic'

class MisclassificationIndices:
    @staticmethod
    def calculate(classifier,bow_dataset,n_folds=3,seed=0):  #, widget):
        from sklearn.cross_validation import StratifiedKFold
        noisyIndices = []

        stf = StratifiedKFold(bow_dataset.labels, n_folds=n_folds, random_state=seed)
        folds = [(list(train_index), list(test_index)) for train_index, test_index in stf]

        for i in range(n_folds):
            train_indices, test_indices = folds[i]
            train_data,test_data = bow_dataset.split(train_indices,test_indices)

            #apply classifier
            trained_classifier=train_classifier({'classifier': classifier,
                                                 'training_data':train_data})['trained_classifier']
            #predict
            predictions=apply_bow_classifier({'trained_classifier':trained_classifier,
                                  'testing_dataset':test_data})['predictions']
            #classifier.fit(train_data,)
            #predictions = classifier.predict(test_data)

            for indice, real_class, prediction in izip(test_indices, test_data.labels, predictions):
                if real_class != prediction.max():
                    noisyIndices.append(indice)
                    #widget.progress = int((i+1)*1.0/k*100)
                    #widget.save()
        # END test_fold
        return {'inds': sorted(noisyIndices), 'name': classifier.__class__.__name__}


from itertools import izip

__author__ = 'matic'

class MisclassificationIndices:
    @classmethod
    def calculate(cls,classifier,data,labels,n_folds=3,seed=0):  #, widget):
        from sklearn.cross_validation import StratifiedKFold, KFold
        noisyIndices = []

        stf = StratifiedKFold(labels, n_folds=n_folds, random_state=seed)
        folds = [(list(train_index), list(test_index)) for train_index, test_index in stf]

        for i in range(n_folds):
            train_indices, test_indices = folds[i]
            train_data = data[train_indices]
            train_labels = labels[train_indices]
            test_data = data[test_indices]
            test_labels = labels[test_indices]

            classifier.fit(train_data, train_labels)
            predictions = classifier.predict(test_data)

            for indice, real_class, predicted_class in izip(test_indices, test_labels, predictions):
                if real_class != predicted_class:
                    noisyIndices.append(indice)
                    #widget.progress = int((i+1)*1.0/k*100)
                    #widget.save()
        # END test_fold
        return {'indices': sorted(noisyIndices), 'name': classifier.__class__.__name__}


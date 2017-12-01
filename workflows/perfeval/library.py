def benchmark(input_dict):
    import time
    in_att = input_dict.get('in_att', None)
    start_time= input_dict.get('start_time', None)
    time_diff=(time.time()-start_time) if start_time else time.time()
    return {'out_att': in_att, 'time_diff': time_diff}


def perfeval_classification_statistics(input_dict):
    from sklearn import metrics
    labels = input_dict['true_and_predicted_labels']
    pos_label = input_dict.get('pos_label', None)

    # Check if we have true and predicted labels for each fold
    if labels and type(labels[0][0]) == list:
        try:
            # Flatten
            y_true, y_pred = [], []
            for fold_labels in labels:
                y_true.extend(fold_labels[0])
                y_pred.extend(fold_labels[1])
            labels = [y_true, y_pred]
        except:
            raise Exception('Expected true and predicted labels for each fold, but failed.' + 
                            'If you wish to provide labels for each fold separately it should look like: ' + 
                            '[[y_true_1, y_predicted_1], [y_true_2, y_predicted_2], ...]')
    if len(labels) != 2:
        raise Exception('Wrong input structure, this widget accepts labels in the form: [y_true, y_pred]')
    
    y_true, y_pred = labels
    
    classes = set()
    classes.update(y_true + y_pred)
    classes = sorted(list(classes))

    # Assign integers to classes
    class_to_int = {}
    for i, cls_label in enumerate(classes):
        class_to_int[cls_label] = i

    y_true = [class_to_int[lbl] for lbl in y_true]
    y_pred = [class_to_int[lbl] for lbl in y_pred]

     # AUC is defined only for binary classes
    if len(classes) == 2:
        auc = metrics.roc_auc_score(y_true, y_pred)
        avg = 'binary'
    else:
        avg = 'weighted'
        auc = 'undefined for multiple classes' #

    accuracy = metrics.accuracy_score(y_true, y_pred)
    precision = metrics.precision_score(y_true, y_pred, average=avg)
    recall = metrics.recall_score(y_true, y_pred, average=avg)
    f1 = metrics.f1_score(y_true, y_pred, average=avg)
    confusion_matrix = []#metrics.confusion_matrix(y_true, y_pred)

   
    return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 
            'f1': f1, 'auc': auc, 'confusion_matrix': confusion_matrix}


def extract_actual_and_predicted_features(input_dict):
    adc = input_dict['adc']
    annotation_actual = input_dict['annotation_actual']
    annotation_predicted = input_dict['annotation_predicted']
    if not annotation_actual.startswith('Token/'):
        annotation_actual = 'Token/' + annotation_actual
    if not annotation_predicted.startswith('Token/'):
        annotation_predicted = 'Token/' + annotation_predicted
    predicted = []
    actual = []
    for doc in adc.documents:
        actual.extend(doc.get_annotation_texts(annotation_actual))
        predicted.extend(doc.get_annotation_texts(annotation_predicted))

    '''
    #remove NONE tags
    filtered_predicted = []
    filtered_actual = []
    for i in range(len(predicted)):
        if actual[i] == u'-NONE-' and predicted[i] != u'-NONE-':
            pass
            #print(predicted[i], actual[i])
        else:
            filtered_predicted.append(predicted[i])
            filtered_actual.append(actual[i])

    actual = filtered_actual
    predicted = filtered_predicted
    '''

    if 'lowercase' in input_dict and input_dict['lowercase']:
        for i in range(len(predicted)):
            predicted[i] = predicted[i].lower()
            actual[i] = actual[i].lower()
    
    return {'actual_and_predicted': [actual, predicted]}


def eval_to_2d_table(input_dict):
    return {}    

import re

def lexicology_get_all_synsets(input_dict):
    if input_dict['corpus'].lower()=='wordnet':
        from nltk.corpus import wordnet as wn
        synsets = {}
        for word in input_dict['words']:
            synsets[word] = wn.synsets(word)
        return {'synsets' : synsets}

def lexicology_get_word_synsets(input_dict):
    if input_dict['corpus'].lower()=='wordnet':
        from nltk.corpus import wordnet as wn
        return {'synsets':wn.synsets(input_dict['word'])}


def read_string_in_slovene(input_dict):
    return {}


def lexicology_mesh_filter(input_dict):
    return {'output_file':'svoboden kot pticek na veji'}

def lexicology_mesh_filter_finished(postdata, input_dict, output_dict):
    import json
    from os.path import normpath, join, dirname

    #widget_id = postdata.get('widget_id')[0]
    ngrams = input_dict.get('ngrams')
    print ngrams
    selected_categories=postdata.get('selected[]')
    terms_per_category=json.load(open(normpath(join(dirname(__file__),'data/mesh_terms_per_category.json'))))
    # for k,v in terms_per_category.items():
    #     terms_per_category[k]=list(v)
    # import json
    # json.dump(terms_per_category,open(normpath(join(dirname(__file__),'data/mesh_terms_per_category.json')),'w'))

    terms=set()
    for category in selected_categories:
        for term in terms_per_category[category]:

            if ngrams:
                single_words=term.split(" ")
                print "SW:",single_words
                for n in range(2 if len(single_words)>1 else 1,len(single_words)+1):
                    grams = set([" ".join(single_words[i:i+n]) for i in xrange(len(single_words)-n+1)])
                    terms |= grams
                    print grams
            else:
                terms.add(term)
    # import time
    # unique_filename=time.strftime("%Y-%m-%d-%H-%M-%S")
    # output_file_name="C:/Users/matic/workspace/iClowdFlow/mothra/public/files/1/terms_"+str(unique_filename)+".txt"
    # with open(output_file_name,'w') as of:
    #     for term in terms:
    #         of.write("%s\n" % term)

    return {'term_list':list(terms)}






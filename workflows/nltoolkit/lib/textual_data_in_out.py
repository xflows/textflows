import urllib
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
from workflows.textflows import *
import os.path
import time
import re
import zipfile
import document_converters


def load_adc(input_dict):
    """
    This widget processes text and loads it into ADC (Annotated Document Corpus) structure. The input file contains one
    document per line - the whole line represents text from the body of a document. In case lines contain more document
    properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

    :param input: file path, string or list
    :param tab_separated_title: document title is separated from the text with \t. Example: title \t start of text
    :param leading_labels: documents has labels infront of the text. Example: !LB1 !Lb2 !LBL \t start of text
    :return adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    """
    input_text = input_dict[u"input"]
    tab_separated_title = input_dict['tab_separated_title'] == "true"
    leading_labels = input_dict['leading_labels'] == "true"

    docs, source, source_date,titles=_process_input(input_text,leading_labels)

    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    documents, labels = _process_adc(docs, tab_separated_title, leading_labels, titles)
    features = {u"Source": source, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date, "Labels": json.dumps(labels)}
    
    return {"adc": DocumentCorpus(documents=documents, features=features)}


def load_ptb_corpus(input_dict):
    input_text = input_dict[u"input"]
    leading_labels = False
    docs, source, source_date,titles=_process_input(input_text,leading_labels)
    tagged_sents = []
    for doc in docs:
        l = []
        doc = doc.replace('\n', '')
        sent = ""
        depth = 0
        for character in doc:
            if character == '(':
                depth = depth + 1
            elif character == ')':
                depth = depth - 1
            sent += character
            if depth == 0 and len(sent) > 0 and not sent.isspace():
                l.append(sent)
                sent = ""
        for sent in l:
            tagged_sent = []
            match = re.findall(r'\(([^\(\)]*)\)',sent)
            for m in match:
                tagged_word = m.strip().split(" ")
                if len(tagged_word) == 2:
                    tagged_word = [tagged_word[1], tagged_word[0]]
                    tagged_sent.append(tagged_word)
            tagged_sents.append(tagged_sent)

    return {"ptb_corpus": tagged_sents}


def ptb_to_adc_converter(input_dict):
    corpus = input_dict['ptb_corpus']
    annotation_feature = input_dict['annotation_name']
    annotations = []
    string_list = []
    docs = []
    title = u"Document1"
    features = {u"contentType": u"Text", u"sourceFileLine": '1'}
    position = 0
    for i, sentence in enumerate(corpus):
        if i%100 == 0 and i != 0 and i != (len(corpus) - 1):
            annotation = Annotation(0, position , "TextBlock")
            annotations.append(annotation)
            rawtext = " ".join(string_list)
            document = Document(title, rawtext, annotations, features)
            docs.append(document)
            annotations = []
            string_list = []
            title = u"Document" + str(i)
            features = {u"contentType": u"Text", u"sourceFileLine": '1'}
            position = 0

        sentence_start = position
        for word, tag in sentence:
            string_list.append(word)
            word_length = len(word)
            annotation_features = {annotation_feature: tag}
            annotation = Annotation(position, position + word_length - 1, "Token", annotation_features)
            annotations.append(annotation)
            position = position + word_length + 1
        if position > sentence_start:
            annotation = Annotation(sentence_start, position - 1, "Sentence")
            annotations.append(annotation)
    annotation = Annotation(0, position , "TextBlock")
    annotations.append(annotation)
    rawtext = " ".join(string_list)
    document = Document(title, rawtext, annotations, features)
    docs.append(document)
    source = "list"
    source_date = "unknown"
    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    features = {u"Source": source, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date, "Labels": []}
    adc = DocumentCorpus(documents=docs, features=features)

    return {"adc": adc}


def crawl_url_links(input_dict):
    """
    This widget takes either a list of url links or a string, where each url is in a separate line. For every inputted url,
    the system crawls the page and extracts content using the readability library.

    :param urls: file path, string or list
    :param label: label which is set to all documents
    :return adc: Annotated Document Corpus (workflows.textflows.DocumentCorpus)
    """

    extractor_name=input_dict.get('extractor','DefaultExtractor')
    import requests
    label=input_dict['label']
    urls,_, source, source_date=_process_input(input_dict['input'],False)


    docs=[]
    titles=[]
    for url in urls:
        print url
        try:
            r = requests.get(url)
        except ConnectionError:
            continue
        if r.status_code==200:
            html=r.text
            from boilerpipe.extract import Extractor
            extractor = Extractor(extractor=extractor_name, html=html)

            titles.append(url)
            text=''
            if label:
                text+='!'+label+'\t'
            text+=extractor.getText()
            docs.append(text)


    corpus_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
    documents, labels = _process_adc(docs, False, label, titles)
    features = {u"Source": source, u"SourceDate": source_date, u"CorpusCreateDate": corpus_date,
                "Labels": json.dumps([label]) if label else '[]'}

    return {"adc": DocumentCorpus(documents=documents, features=features)}


def search_with_faroo(input_dict):
    faroo_search="http://www.faroo.com/api?q={query}&start=1&length={length}&l=en&src=web&f=json&key={key}"
    file_name="workflows/nltoolkit/package_data/faroo_api_key.json"

    limit=int(input_dict.get('limit','50'))
    query=input_dict['query']

    if not query:
        raise StandardError("Please specify some search keywords.")

    urls=[]
    if os.path.isfile(file_name):
        with open(file_name) as data_file:
            api=json.load(data_file)
            query = '%27' + urllib.quote(query) + '%27'

            response=requests.get(faroo_search.format(key=api, query=query, length=limit))

            if response.status_code==200:
                results=json.loads(response.text)['results']
                for result in results:
                    urls.append(result['url'])
            else:
                raise StandardError(response.content())

    else:
        raise StandardError("Please create specify your Bing Api key in workflows/nltoolkit/package_data/faroo_api_key.json")

    return {'urls': urls}

def search_with_bing(input_dict):
    file_name="workflows/nltoolkit/package_data/bing_api_key.json"

    limit=int(input_dict.get('limit','50'))
    query=input_dict['query']

    if not query:
        raise StandardError("Please specify some search keywords.")

    urls=[]
    if os.path.isfile(file_name):
        with open(file_name) as data_file:
            api=json.load(data_file)
            query = '%27' + urllib.quote(query) + '%27'

            base_url = 'https://api.datamarket.azure.com/Bing/Search/Web'
            url = base_url + '?Query=' + query + '&$top=' + str(limit) + '&$format=json'

            # create credential for authentication
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"

            auth = HTTPBasicAuth(api, api)
            headers = {'User-Agent': user_agent}

            response_data = requests.get(url, headers=headers, auth = auth)
            result_list = response_data.json()['d']['results']

            for result in result_list:
                #{u'Description': u'Reading the newest QubeGB reviews is a thing that could possibly be amazed for. This UK based communication firm gives a great choice of services to their customers.', u'Title': u'Kemi Anita Dasilva Ibru', u'Url': u'http://sfasf.com/', u'__metadata': {u'type': u'WebResult', u'uri': u"https://api.datamarket.azure.com/Data.ashx/Bing/Search/Web?Query='sfasf'&$skip=0&$top=1"}, u'DisplayUrl': u'sfasf.com', u'ID': u'b5811fb0-d21d-4868-a4ee-be32e3eae759'}
                urls.append(result['Url'])
    else:
        raise StandardError("Please create specify your Bing Api key in workflows/nltoolkit/package_data/bing_api_key.json")


    return {'urls': urls}


def load_mysql_document_corpus(input_dict):
    user = str(input_dict['user'])
    password = str(input_dict['password'])
    host = str(input_dict['host'])
    database_name = str(input_dict['database'])

    text_column_name = str(input_dict['text_column_name'])
    title_column_name = str(input_dict['title_column_name'])
    label_column_name = str(input_dict['label_column_name'])
    table_name = str(input_dict['table_name'])


    import MySQLdb
    db=MySQLdb.connect(passwd=password,user=user,db=database_name,host=host)
    c=db.cursor()
    c.execute("""SELECT %s, %s, %s FROM %s""" % (title_column_name,text_column_name,label_column_name,table_name))

    documents=[]
    labels=set()
    for (title, text, label) in c:
        doc_labels=[t.rstrip() for t in label.split(",")]
        labels.update(doc_labels)
        features={"Labels": json.dumps(doc_labels) }
        documents.append(Document(name=title,
                              features=features,
                              text=unicode(text),
                              annotations=[Annotation(span_start=0,span_end=max(0, len(unicode(text)) - 1),
                                                      type=u"TextBlock", features={})]))
    c.close()
    features = {u"Source": 'MySQL DB: '+database_name, u"CorpusCreateDate": unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())),
                "Labels": json.dumps(list(labels)) }
    return {'adc': DocumentCorpus(documents=documents, features=features)}



def _process_input(input_text,tab_separated_title):
    source = "list"
    source_date = "unknown"
    titles = []


    #check if input is a file
    if type(input_text) != list and os.path.exists(input_text):
        source = os.path.basename(input_text)
        seconds = os.path.getctime(input_text)
        source_date = unicode(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(seconds)))
        ext = os.path.splitext(input_text)[1]

        if ext == ".zip":
            f = zipfile.ZipFile(input_text, "r")
            dir = os.path.dirname(input_text)
            f.extractall(dir)
            input_text = []

            if len(f.namelist()) == 0:
                raise Exception("Zip file is empty!")

            for name in f.namelist():
                #OSX can have a journaling file in it or the file is a directory
                if name not in ["._.DS_Store", ".DS_Store", "__MACOSX"] and name[-1] != "/":
                    filename, text = document_converters.document_to_text(dir + os.sep + name)
                    input_text.append(text)
                    if not tab_separated_title:
                        titles.append(filename)
        else:
            filename, input_text = document_converters.document_to_text(input_text)

    #check if input is a string
    if type(input_text) == unicode or type(input_text) == str:
        source = "string" if source == "list" else source
        input_text = re.split("[\r\n]", input_text)

    return input_text, source, source_date,titles

def _process_adc(texts,  tab_separated_title, leading_labels, titles=[]):
    """
    function parses title and labels for documents from text and it sets annnotation for each document.

    :param texts: list of documents
    :param tab_separated_title: document title is separated from the text with \t. Example: title \t start of text
    :param leading_labels: documents has labels infront of the text. Example: !LB1 !Lb2 !LBL \t start of text
    :return: list of documents, uniq list of labels
    """
    documents = []
    corpus_labels = set()
    for i, text in enumerate(texts):
        if text:
            title = u"Document" + unicode(i + 1) if titles == [] else titles[i]
            features = {u"contentType": u"Text", u"sourceFileLine": unicode(i)}
    
            if tab_separated_title:
                #example: title \t start of text
                text = text.split("\t")
                title = unicode(text[0])
                text = "\t".join(text[1:])
    
            if leading_labels:
                #example: !LB1 !Lb2 !LBL \t start of text
                text = text.split("\t")
                doc_labels=[]
                for label in [f.strip() for f in text[0].split("!") if f != u""]:
                    features[label] = "true"
                    corpus_labels.add(label)
                    doc_labels.append(label)
                text = "".join(text[1:])
                features["Labels"]=json.dumps(doc_labels)
    
            documents.append(Document(name=title,
                                      features=features,
                                      text=unicode(text),
                                      annotations=[Annotation(span_start=0,
                                                              span_end=max(0, len(unicode(text)) - 1),
                                                              type=u"TextBlock",
                                                              features={})]))
    return documents, list(corpus_labels)


def get_plain_texts(input_dict):
    """
    Widget transforms Annotated Document Corpus to string.

    :param adc: Annotated Document Corpus.
    :param feature_annotation: Select a feature annotation.
    :param delimiter: Delimiter for token concatenation.
    :param include_doc_id: Include Document Identifier.
    :return: String with all documents in Annotated Document Corpus.

    """

    adc = input_dict['adc']
    annotation = input_dict['token_annotation']
    feature_annotation = input_dict['feature_annotation']
    if feature_annotation:
        annotation+="/"+feature_annotation
    delimiter = input_dict['delimiter']
    includeDocId = input_dict['include_doc_id'] == "true"

    output_dict = {"strings": []}
    for document in adc.documents:
        output_dict["strings"].append((document.name+": " if includeDocId else "") + delimiter.join([t[1] for t in document.get_annotations_with_text(annotation)]))
    return output_dict


def display_document_corpus(input_dict):
    #implemented in visualization_views.py
    return {}
    

def display_annotation_statistic(input_dict):
    #implemented in visualization_views.py
    return {}

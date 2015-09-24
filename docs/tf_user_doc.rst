Category Data In/Out
====================
Category Latino
---------------

Widget: Convert Corpus to XML String
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_to_xml_image.png
   :width: 50
   :height: 50
Automatically generated widget from function SaveADCToXml in package latino. The original function signature: SaveADCToXml.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Output: XML String


Widget: Convert XML String to Corpus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/xml_to_adc_image.png
   :width: 50
   :height: 50
Automatically generated widget from function LoadADCFromXml in package latino. The original function signature: LoadADCFromXml.

* Input: XML String (System.String)
* Output: Annotated Document Corpus


Widget: Get Plain Texts
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_to_text_image.png
   :width: 50
   :height: 50
Automatically generated widget from function GetDocStrings in package latino. The original function signature: GetDocStrings.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Token Annotation (System.String)

  * Default value: TextBlock
* Parameter: Feature Condition (Condition which tokens to include based on their features.
  Format examples:
  -Feature1 (don't include tokens with Feature1 set ta any value)
  -Feature1=Value1 (don't include tokens with Feature1 set to the value Value1)
  -Feature1 +Feature2 (don't include tokens with Feature1 set unless it has also Feature2 set)
  -Feature1=Value1 +Feature2 (don't include tokens with Feature1 set to Value1 unless it has also Feature2 set to any value)...)
* Parameter: Delimiter for token concatenation (System.String)
* Parameter: Include Document Identifier (System.Boolean)
* Output: Texts


Widget: Load Document Corpus From File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/load_adc_from_file_image.png
   :width: 50
   :height: 50
This widges processes raw text file and loads the texts into ADC (Annotated Document Corpus) structure. The input file contains one document per line - the whole line represents text from the body of a document. In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

* Input: Raw Text File (Input Text File: Contains one document per line - the whole line represents text from the body of a document.)
* Parameter: Text before the first tabulator [/t] represents the title of a document (System.Boolean)

  * Default value: false
* Parameter: First words in a line (after optional title) with preceding exclamation (!) present labels (System.Boolean)

  * Default value: false
* Output: Annotated Document Corpus


Widget: Load Document Corpus From String
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/load_adc_from_file_image.png
   :width: 50
   :height: 50
This widges processes raw text file and loads the texts into ADC (Annotated Document Corpus) structure. The input file contains one document per line - the whole line represents text from the body of a document. In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

* Input: String (Input Text String: Contains one document per line - the whole line represents text from the body of a document.)
* Parameter: Text before the first tabulator [/t] represents the title of a document (System.Boolean)

  * Default value: false
* Parameter: First words in a line (after optional title) with preceding exclamation (!) present labels (System.Boolean)

  * Default value: false
* Output: Annotated Document Corpus


Widget: Get Plain Texts
------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_to_text_image.png
   :width: 50
   :height: 50
Widget transforms Annotated Document Corpus to string.

* Input: Annotated Document Corpus (Annotated Document Corpus.)
* Parameter: Feature Annotation (Select a feature annotation.)

  * Default value: Stem
* Parameter: Token Annotation (Select token annotation.)

  * Default value: Token
* Parameter: Delimiter for token concatenation (Delimiter for token concatenation.)

  * Default value:  
* Parameter: Include Document Identifier (Include Document Identifier.)
* Output: Texts (String with all documents in Annotated Document Corpus.)


Widget: Load Document Corpus
-----------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/load_adc_from_file_image.png
   :width: 50
   :height: 50
This widget processes input text and loads it into ADC (Annotated Document Corpus) structure. The input text contains one document per line - the whole line represents text from the body of a document. In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

* Input: Input (Input can be a string (str) or a file (fil).)
* Parameter: Text before the first tabulator [/t] represents the title of a document (Text before the first tabulator [/t] represents the title of a document.)

  * Default value: false
* Parameter: First words in a line (after optional title) with preceding exclamation (!) present labels (First words in a line (after optional title) with preceding exclamation (!) present labels.)

  * Default value: false
* Output: Annotated Document Corpus (Annotated Document Corpus.)


Widget: Load Document Corpus From String
-----------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/load_adc_from_file_image.png
   :width: 50
   :height: 50
This widget processes input text and loads it into ADC (Annotated Document Corpus) structure. The input text contains one document per line - the whole line represents text from the body of a document. In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

* Input: String (Input Text String: Contains one document per line - the whole line represents text from the body of a document.)
* Parameter: Text before the first tabulator [/t] represents the title of a document (Text before the first tabulator [/t] represents the title of a document.)

  * Default value: false
* Parameter: First words in a line (after optional title) with preceding exclamation (!) present labels (First words in a line (after optional title) with preceding exclamation (!) present labels.)

  * Default value: false
* Output: Annotated Document Corpus (Annotated Document Corpus.)


Widget: Load Document Corpus From File
---------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/load_adc_from_file_image.png
   :width: 50
   :height: 50
This widget processes raw text file and loads the texts into ADC (Annotated Document Corpus) structure. The input file contains one document per line - the whole line represents text from the body of a document. In case lines contain more document properties (i.e.: ids, titles, labels,...) than other widgets should be used to load ADC structure.

* Input: Raw Text File (Input Text File: Contains one document per line - the whole line represents text from the body of a document.)
* Parameter: Text before the first tabulator [/t] represents the title of a document (Text before the first tabulator [/t] represents the title of a document.)

  * Default value: false
* Parameter: First words in a line (after optional title) with preceding exclamation (!) present labels (First words in a line (after optional title) with preceding exclamation (!) present labels.)

  * Default value: false
* Output: Annotated Document Corpus (Annotated Document Corpus.)

Category Scikit_classifiers
===========================

Widget: Create Integer List
----------------------------
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/construction_work .png
   :width: 50
   :height: 50
* Parameter: Integer List String (Comma or new-line separated list of integers)

  * Default value: 3
2
1
4
* Parameter: Sort list (Should the list be sorted)

  * Default value: true
* Output: Integer List (List of integers)


Widget: Filter Integers
------------------------
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/construction_work .png
   :width: 50
   :height: 50
* Input: Integer List (List of integers)
* Output: Filtered Integer List (Filtered list of integers)


Widget: Sum Integers
---------------------
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/construction_work .png
   :width: 50
   :height: 50
* Input: Integer List (List of integers)
* Output: Sum (Sum of integer list)


Widget: Display Summation
--------------------------
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/construction_work .png
   :width: 50
   :height: 50
* Input: Integer List (List of integers)
* Input: Sum (Sum (possibly correct) of integer list)
* Outputs: Popup window which shows widget's results

Category Document Corpus
========================
Category Latino
---------------

Widget: Display Document Corpus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/view_adc_image.png
   :width: 50
   :height: 50
Automatically generated widget from function DisplayDocumentCorpus_PYTHON in package latino. The original function signature: DisplayDocumentCorpus_PYTHON.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Outputs: Popup window which shows widget's results


Widget: Statistics
~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_info_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CorpusStatistics in package latino. The original function signature: CorpusStatistics.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Output: Number of Documents
* Output: Number of Features
* Output: Statistics


Widget: Extract Feature
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_extract_feature_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ExtractDocumentsFeatures in package latino. The original function signature: ExtractDocumentsFeatures.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Extracted Feature Name (System.String)
* Output: List of Extracted Features


Widget: Add Feature
~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_add_feature_image.png
   :width: 50
   :height: 50
Automatically generated widget from function AddDocumentsFeatures in package latino. The original function signature: AddDocumentsFeatures.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Feature Values (Array of Labels) (System.Collections.Generic.List`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Parameter: New Feature Name (System.String)

  * Default value: feature
* Parameter: New Feature Value Prefix (System.String)
* Output: Annotated Document Corpus


Widget: Add Computed Feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_add_feature_image.png
   :width: 50
   :height: 50
Automatically generated widget from function AddComputedFeatures in package latino. The original function signature: AddComputedFeatures.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: New Feature Name (System.String)

  * Default value: feature
* Parameter: New Feature Computataion (System.String)

  * Default value: {feature2:name}{feature3}, {feature1:value}
* Parameter: Old Features Specification (Comma separated list of names of old features used in the 'New Feature Computataion'.)

  * Default value: feature1, feature2
* Output: Annotated Document Corpus


Widget: Add Set Feature
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_add_set_feature_image.png
   :width: 50
   :height: 50
Automatically generated widget from function MarkDocumentsWithSetFeature in package latino. The original function signature: MarkDocumentsWithSetFeature.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Feature Name (System.String)

  * Default value: set
* Parameter: Feature Value Prefix (System.String)
* Parameter: Num of Sets (System.Int32)

  * Default value: 10
* Parameter: Assign Sets Randomly (System.Boolean)

  * Default value: true
* Parameter: Use Seed for Random (System.Boolean)

  * Default value: false
* Parameter: Random Seed (System.Int32)

  * Default value: 0
* Output: Annotated Document Corpus


Widget: Split
~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_split_image.png
   :width: 50
   :height: 50
Automatically generated widget from function SplitDocumentsByFeatureValue in package latino. The original function signature: SplitDocumentsByFeatureValue.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Feature Condition (System.String)
* Parameter: Discard The Rest (The Filtered Out) (System.Boolean)

  * Default value: false
* Output: Filtered Annotated Document Corpus
* Output: The Rest of Annotated Document Corpus


Widget: Extract Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/adc_split_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ExtractDocuments in package latino. The original function signature: ExtractDocuments.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: List of Document Indexes to be Extracted (System.Collections.Generic.List`1[[System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Parameter: Discard The Rest (The Filtered Out) (System.Boolean)

  * Default value: false
* Output: Annotated Document Corpus of Extracted Documents
* Output: Annotated Document Corpus of the Rest of Documents


Widget: Merge Corpora
~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Automatically generated widget from function JoinDocumentsCorpora in package latino. The original function signature: JoinDocumentsCorpora.

* Input: Annotated Document Corpus (System.Collections.Generic.List`1[[LatinoInterfaces.DocumentCorpus, LatinoInterfaces, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Merged Annotated Document Corpus


Widget: Add Feature
--------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_add_feature_image.png
   :width: 50
   :height: 50
Add a feature to Annotated Document Corpus.

* Input: Annotated Document Corpus
* Input: Feature Values  (List of feature values)
* Parameter: New Feature Name

  * Default value: feature
* Parameter: New Feature Value Prefix
* Output: Annotated Document Corpus


Widget: Display Document Corpus
--------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/view_adc_image.png
   :width: 50
   :height: 50
Display Document Corpus widget displays ADC (Annotated Document Corpus) structure. It shows a detail view for selected document with annotations.

* Input: Annotated Document Corpus (Annotated Document Corpus.)
* Outputs: Popup window which shows widget's results


Widget: Extract Documents
--------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_split_image.png
   :width: 50
   :height: 50
Extract documents, given document indices, from Annotated Document Corpus.

* Input: Annotated  (Annotated Document Corpus.)
* Input: List of Document Indexes to be Extracted
* Parameter: Discard The Rest (The Filtered Out)

  * Default value: false
* Output: Annotated Document Corpus of Extracted Documents
* Output: Annotated Document Corpus of Extracted Documents


Widget: Extract Feature
------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_extract_feature_image.png
   :width: 50
   :height: 50
Extract documents features.

* Input: Annotated Document Corpus (Annotated Document Corpus.)
* Parameter: Extracted Feature Name
* Output: List of Extracted Features


Widget: Merge Corpora
----------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Merge multiple Annotated Document Corpuses into one.

* Input: Annotated 
* Output: Merged Annotated Document Corpus


Widget: NLTK Document Corpus
-----------------------------
.. image:: ../workflows/static/widget-icons/question-mark.png
   :width: 50
   :height: 50
NLTK corpus readers. The modules in this package provide functions that can be used to read corpus files in a variety of formats. These functions can be used to read both the corpus files that are distributed in the NLTK corpus package, and corpus files that are part of external corpora.

Please see http://nltk.googlecode.com/svn/trunk/nltk_data/index.xml for a complete list. Install corpora using nltk.download().

Corpus has the following available functions:
words(): list of str
sents(): list of (list of str)
paras(): list of (list of (list of str))
tagged_words(): list of (str,str) tuple
tagged_sents(): list of (list of (str,str))
tagged_paras(): list of (list of (list of (str,str)))
chunked_sents(): list of (Tree w/ (str,str) leaves)
parsed_sents(): list of (Tree with str leaves)
parsed_paras(): list of (list of (Tree with str leaves))
xml(): A single xml ElementTree
raw(): unprocessed corpus contents

* Parameter: NLTK Document Corpus Name (NTLK Document Corpus Name)

  * Possible values: 

    * Brown
    * Cess Esp (spanish)
    * Floresta
    * Treebank

  * Default value: brown
* Output: NTLK document corpus (NLTK document corpus name)


Widget: Split
--------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_split_image.png
   :width: 50
   :height: 50
Split Annotated Document Corpus by conditions with features and values.

* Input: Annotated Document Corpus (Annotated )
* Parameter: Feature Condition
* Parameter: Discard The Rest (The Filtered Out)
* Output: Filtered Annotated Document Corpus
* Output: The Rest of Annotated Document Corpus


Widget: Statistics
-------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_info_image.png
   :width: 50
   :height: 50
Statistics of Annotated Document Corpus.

* Input: Annotated Document Corpus
* Output: Number of Documents (Number of Documents.)
* Output: Number of Features (Number of Features.)
* Output: Statistics (Statistics.)


Widget: Add Computed Document Features
---------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_add_feature_image.png
   :width: 50
   :height: 50
TODO

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: New Feature Name (System.String)

  * Default value: feature
* Parameter: New Feature Computataion (System.String)

  * Default value: {feature2:name}{feature3}, {feature1:value}
* Output: Annotated Document Corpus


Widget: Add Computed Token Features
------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/adc_add_feature_image.png
   :width: 50
   :height: 50
For every annotation of the selected type generate an additional feature. Between { } a feature name can be entered and it will be replaced with its value.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: New Feature Name (System.String)

  * Default value: feature
* Parameter: Annotation Name (Add features to tokens of this type.)

  * Default value: Token
* Parameter: New Feature Computataion (Values for the new features. Between { } a feature name can be entered and it will be replaced with its value.)

  * Default value: {Stem}_{POS Tag}
* Output: Annotated Document Corpus

Category Latino
===============
Category Tokenization
=====================
Category Latino
---------------
Category Advanced
~~~~~~~~~~~~~~~~~

Widget: Split Sentences Hub (Text)
```````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/token_sentence_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TokenizeStringString in package latino. The original function signature: TokenizeStringString.

* Input: Text (System.Object)
* Input: Tokenizer (Latino.TextMining.ITokenizer)
* Output: Text


Widget: Tokenizer Hub (Text)
`````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TokenizeStringWords in package latino. The original function signature: TokenizeStringWords.

* Input: Text (System.Object)
* Input: Tokenizer (Latino.TextMining.ITokenizer)
* Output: String


Widget: Universal Multiple Tokenizer Hub
`````````````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/token_multi_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TokenizeMultiple in package latino. The original function signature: TokenizeMultiple.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Tokenizer (System.Collections.IList)
* Parameter: Annotations to be tokenized (Which annotated part of document to be splited)

  * Default value: TextBlock
* Parameter: Annotations to be produced (How to annotate found sentences)

  * Default value: Token
* Output: Annotated Document Corpus


Widget: Max Entropy Sentence Splitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_sentence_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructEnglishMaximumEntropySentenceDetector in package latino. The original function signature: ConstructEnglishMaximumEntropySentenceDetector.

* Output: Sentence Tokenizer


Widget: Split Sentences Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_sentence_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TokenizeSentences in package latino. The original function signature: TokenizeSentences.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Tokenizer (Latino.TextMining.ITokenizer)
* Parameter: Annotation to be tokenized (Which annotated part of document to be splited)

  * Default value: TextBlock
* Parameter: Annotation to be produced (How to annotate found sentences)

  * Default value: Sentence
* Output: Annotated Document Corpus


Widget: Max Entorpy Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructEnglishMaximumEntropyTokenizer in package latino. The original function signature: ConstructEnglishMaximumEntropyTokenizer.

* Parameter: Alpha Numeric Optimization (System.Boolean)

  * Default value: true
* Output: Tokenizer


Widget: Unicode Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructUnicodeTokenizer in package latino. The original function signature: ConstructUnicodeTokenizer.

* Parameter: Filter (Latino.TextMining.TokenizerFilter)

  * Possible values: 

    * AlphaLoose: accept tokens that contain at least one alphabetic character
    * AlphaStrict: accept tokens that contain alphabetic characters only
    * AlphanumLoose: accept tokens that contain at least one alphanumeric character
    * AlphanumStrict: accept tokens that contain alphanumeric characters only
    * None: accept all tokens

  * Default value: None
* Parameter: Minimal Token Length (System.Int32)

  * Default value: 1
* Output: Tokenizer


Widget: Regex Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructRegexTokenizer in package latino. The original function signature: ConstructRegexTokenizer.

* Parameter: Regular Expression (System.String)

  * Default value: \p{L}+(-\p{L}+)*
* Parameter: Ignore Unknown Tokens (System.Boolean)
* Parameter: Ignore Case (System.Boolean)
* Parameter: Multiline (System.Boolean)
* Parameter: Explicit Capture (System.Boolean)
* Parameter: Compiled (System.Boolean)
* Parameter: Singleline (System.Boolean)
* Parameter: Ignore Pattern Whitespace (System.Boolean)
* Parameter: Right To Left (System.Boolean)
* Parameter: ECMA Script (System.Boolean)
* Parameter: Culture Invariant (System.Boolean)
* Output: Tokenizer


Widget: Simple Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructSimpleTokenizer in package latino. The original function signature: ConstructSimpleTokenizer.

* Parameter: Type (Latino.TextMining.TokenizerType)

  * Possible values: 

    * AllChars: equivalent to [^\s]+
    * AlphaOnly: equivalent to \p{L}+
    * AlphanumOnly: equivalent to [\p{L}\d]+

  * Default value: AllChars
* Parameter: Minimal Token Length (System.Int32)

  * Default value: 1
* Output: Tokenizer


Widget: Tokenizer Hub
~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/token_word_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TokenizeWords in package latino. The original function signature: TokenizeWords.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Tokenizer (Latino.TextMining.ITokenizer)
* Parameter: Annotation to be tokenized (Which annotated part of document to be splited)

  * Default value: TextBlock
* Parameter: Annotation to be produced (How to annotate found sentences)

  * Default value: Token
* Output: Annotated Document Corpus

Category Nltk
-------------

Widget: Line Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Tokenize a string into its lines, optionally discarding blank lines.

* Parameter: Blank Lines (blanklines: Indicates how blank lines should be handled.  Options are:
          - discard: strip blank lines out of the token list before returning it.
             A line is considered blank if it contains only whitespace characters.
          - keep: leave all blank lines in the token list.
          - discard-eof: if the string ends with a newline, then do not generate
             a corresponding token ``''`` after that newline.)

  * Possible values: 

    * discard
    * discard-eof
    * keep

  * Default value: discard
* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Regex Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
The Regex Tokenizer splits a string into substrings using a regular expression.

* Parameter: Regular Expression (The pattern used to build this tokenizer.
          (This pattern may safely contain capturing parentheses.))

  * Default value: \p{L}+(-\p{L}+)*
* Parameter: Gaps (True if this tokenizer's pattern should be used
          to find separators between tokens; False if this
          tokenizer's pattern should be used to find the tokens
          themselves.)
* Parameter: Discard empty (True if any empty tokens `''`
          generated by the tokenizer should be discarded.  Empty
          tokens can only be generated if  Gaps is set.)
* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: S-Expression Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
S-Expression Tokenizer is used to find parenthesized expressions in a
string.  In particular, it divides a string into a sequence of
substrings that are either parenthesized expressions (including any
nested parenthesized expressions), or other whitespace-separated
tokens

* Parameter: Parentheses ( A two-element sequence specifying the open and close parentheses
          that should be used to find sexprs.  This will typically be either a
          two-character string, or a list of two strings.)

  * Default value: ()
* Parameter: Strict (If true, then raise an exception when tokenizing an ill-formed sexpr.)

  * Default value: true
* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Simple Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
These tokenizers divide strings into substrings using the string split() method.

Space Tokenizer - Tokenize a string using the space character as a delimiter, which is the same as s.split(' ').
Tab Tokenizer - Tokenize a string use the tab character as a delimiter, the same as s.split('\t').
Char Tokenizer - Tokenize a string into individual characters.  
Whitespace Tokenizer - Tokenize a string on whitespace (space, tab, newline).
Blankline Tokenizer - Tokenize a string, treating any sequence of blank lines as a delimiter. Blank lines are defined as lines containing no characters, except for space or tab characters.
Word Punct Tokenizer - Tokenize a text into a sequence of alphabetic and non-alphabetic characters, using the regexp ``\w+|[^\w\s]+``.

* Parameter: Type (Select a tokenizer.
  
  Space Tokenizer - Tokenize a string using the space character as a delimiter, which is the same as s.split(' ').
  
  Tab Tokenizer - Tokenize a string use the tab character as a delimiter, the same as s.split('\t').
  
  Char Tokenizer - Tokenize a string into individual characters.  
  
  Whitespace Tokenizer - Tokenize a string on whitespace (space, tab, newline).
  
  Blankline Tokenizer - Tokenize a string, treating any sequence of blank lines as a delimiter. Blank lines are defined as lines containing no characters, except for space or tab characters.
  
  Word Punct Tokenizer - Tokenize a text into a sequence of alphabetic and non-alphabetic characters, using the regexp ``\w+|[^\w\s]+``.)

  * Possible values: 

    * Blankline Tokenizer
    * Char Tokenizer
    * Space Tokenizer
    * Tab Tokenizer
    * Whitespace Tokenizer
    * WordPunct Tokenizer

  * Default value: wordpunct_tokenizer
* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Stanford Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
A tokenizer divides text into a sequence of tokens, which roughly correspond to "words".

* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Text Tiling Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
Tokenize a document into topical sections using the TextTiling algorithm. This algorithm detects subtopic shifts based on the analysis of lexical co-occurrence patterns.

* Parameter: Pseudosentence size (Pseudosentence size.)

  * Default value: 20
* Parameter: Size (Size (in sentences) of the block used in the block comparison method. )

  * Default value: 10
* Parameter: Stopwords ( A list of stopwords that are filtered out (defaults to NLTK's stopwords corpus). Example: the, a)

  * Default value: None
* Parameter: Smoothing width (The width of the window used by the smoothing method.)

  * Default value: 2
* Parameter: Smoothing rounds (The number of smoothing passes.)

  * Default value: 1
* Parameter: Similarity method (The method used for determining similarity scores: Block comparison (default) or Vocabulary introduction.)

  * Possible values: 

    * Block comparison
    * Vocabulary introduction

  * Default value: BLOCK_COMPARISON
* Parameter: Cutoff policy (The policy used to determine the number of boundaries: HC (default) or LC.)

  * Possible values: 

    * HC
    * LC

  * Default value: HC
* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Punkt Sentence Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
A sentence tokenizer which uses an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences; and then uses that model to find sentence boundaries. This approach has been shown to work well for many European languages.

* Output: Tokenizer (A python dictionary containing the Tokenizer object and its arguments.)


Widget: Treebank Word Tokenizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_image.png
   :width: 50
   :height: 50
The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank.
    This is the method that is invoked by ``word_tokenize()``.  It assumes that the
    text has already been segmented into sentences, e.g. using ``sent_tokenize()``.

    This tokenizer performs the following steps:

    - split standard contractions, e.g. ``don't`` -> ``do n't`` and ``they'll`` -> ``they 'll``
    - treat most punctuation characters as separate tokens
    - split off commas and single quotes, when followed by whitespace
    - separate periods that appear at the end of line

        >>> from nltk.tokenize import TreebankWordTokenizer
        >>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\n\\nThanks.'''
        >>> TreebankWordTokenizer().tokenize(s)
        ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.',
        'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
        >>> s = "They'll save and invest more."
        >>> TreebankWordTokenizer().tokenize(s)
        ['They', "'ll", 'save', 'and', 'invest', 'more', '.']

    NB. this tokenizer assumes that the text is presented as one sentence per line,
    where each line is delimited with a newline character.
    The only periods to be treated as separate tokens are those appearing
    at the end of a line.

* Output: Tokenizer


Widget: Tokenizer Hub
----------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/token_word_do_image.png
   :width: 50
   :height: 50
Apply the *tokenizer* object on the Annotated Document Corpus (*adc*):

1. first select only annotations of type *input_annotation*,
2. apply the tokenizer
3. create new annotations *output_annotation* with the outputs of the tokenizer.

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: Tokenizer (Python dictionary containing the Tokenizer object and its arguments.)
* Parameter: Annotation to be tokenized (Which annotated part of document to be splitted.)

  * Default value: TextBlock
* Parameter: Annotation to be produced (How to annotate the newly discovered tokens.)

  * Default value: Token
* Output: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))

Category POS Tagging
====================
Category Latino
---------------
Category Advanced
~~~~~~~~~~~~~~~~~

Widget: POS Tagger Hub (Text)
``````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/tag_pos_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function PosTagString in package latino. The original function signature: PosTagString.

* Input: Text (System.Object)
* Input: POS Tagger (OpenNLP.Tools.PosTagger.EnglishMaximumEntropyPosTagger)
* Parameter: Output Feature Name (System.String)

  * Default value: posTag
* Output: String


Widget: Max Entropy POS Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructEnglishMaximumEntropyPosTagger in package latino. The original function signature: ConstructEnglishMaximumEntropyPosTagger.

* Parameter: Beam Size (System.Int32)

  * Default value: 3
* Output: POS Tagger


Widget: POS Tagger Hub
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_pos_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function PosTag in package latino. The original function signature: PosTag.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: POS Tagger (OpenNLP.Tools.PosTagger.EnglishMaximumEntropyPosTagger)
* Parameter: Sentence's Annotation (System.String)

  * Default value: Sentence
* Parameter: Element's Annotation (System.String)

  * Default value: Token
* Parameter: Output Feature Name (System.String)

  * Default value: posTag
* Output: Annotated Document Corpus

Category Nltk
-------------

Widget: POS Affix Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
A tagger that chooses a token's tag based on a leading or trailing
substring of its word string.  (It is important to note that these
substrings are not necessarily "true" morphological affixes).  In
particular, a fixed-length substring of the word is looked up in a
table, and the corresponding tag is returned.  Affix taggers are
typically constructed by training them on a tagged corpus.

* Input: Training Corpus (A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta, or an Annotated Document Corpus in the standard TextFlows' adc format)
* Input: Backoff Tagger (A backoff tagger, to be used by the new tagger if it encounters an unknown context.)
* Parameter: Affix Length (The length of the affixes that should be considered during training and tagging.  Use negative numbers for suffixes.)

  * Default value: -3
* Parameter: Cutoff (If the most likely tag for a context occurs fewer than *cutoff* times, then exclude it from the context-to-tag table for the new tagger.)

  * Default value: 0
* Parameter: Minimum Stem Length (Any words whose length is less than min_stem_length+abs(affix_length) will be assigned a tag of None by this tagger.)

  * Default value: 2
* Output: POS Tagger (A python dictionary containing the POS tagger object and its arguments.)


Widget: POS Brill's rule-based Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
"""Brill's transformational rule-based tagger.  Brill taggers use an
initial tagger (such as ``tag.DefaultTagger``) to assign an initial
tag sequence to a text; and then apply an ordered list of
transformational rules to correct the tags of individual tokens.
These transformation rules are specified by the ``BrillRule``
interface.

Brill taggers can be created directly, from an initial tagger and
a list of transformational rules; but more often, Brill taggers
are created by learning rules from a training corpus, using either
``BrillTaggerTrainer`` or ``FastBrillTaggerTrainer``.

* Input: Training Corpus (A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta, or an Annotated Document Corpus in the standard TextFlows' adc format)
* Input: Initial Tagger (The initial tagger. Brill taggers use an initial tagger (such as ``DefaultTagger``) to assign an initial tag sequence to a text.)
* Parameter: Max Rules (The maximum number of transformations to be created)

  * Default value: 200
* Parameter: Min Score (The minimum acceptable net error reduction that each transformation must produce in the corpus.)

  * Default value: 2
* Parameter: Templates (Templates to be used in training TODO: meaning?!
  
  Options:

  - nltkdemo18:
      Return 18 templates, from the original nltk demo, in multi-feature syntax
  - nltkdemo18plus:
      Return 18 templates, from the original nltk demo, and additionally a few
      multi-feature ones (the motivation is easy comparison with nltkdemo18)
  - brill24:
      Return 24 templates of the seminal TBL paper, Brill (1995)
  - fntbl37:
      Return 37 templates taken from the postagging task of the
      fntbl distribution http://www.cs.jhu.edu/~rflorian/fntbl/
      (37 is after excluding a handful which do not condition on Pos[0];
      fntbl can do that but the current nltk implementation cannot.))

  * Possible values: 

    * brill24
    * fntbl37
    * nltkdemo18
    * nltkdemo18plus

  * Default value: brill24
* Output: POS Tagger (A python dictionary containing the POS tagger object and its arguments.)


Widget: POS Classifier-based Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
A sequential tagger that uses a classifier to choose the tag for
each token in a sentence.  The featureset input for the classifier
is generated by a feature detector function::

    feature_detector(tokens, index, history) -> featureset

Where tokens is the list of unlabeled tokens in the sentence;
index is the index of the token for which feature detection
should be performed; and history is list of the tags for all
tokens before index.

Construct a new classifier-based sequential tagger.

* Input: Training Corpus (A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta, or an Annotated Document Corpus in the standard TextFlows' adc format)
* Input: Backoff Tagger (A backoff tagger, to be used by the new tagger if it encounters an unknown context.)
* Input: Classifier (The classifier that should be used by the tagger.  This is useful if you want to use a manually constructed classifier for POS tagging.)
* Parameter: Cutoff Probability (If specified, then this tagger will fall back on its backoff tagger if the probability of the most likely tag is less than *cutoff_prob*.)
* Output: POS Tagger (A python dictionary containing the POS tagger object and its arguments.)


Widget: POS Default Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
A tagger that assigns the same tag to every token.

    >>> from nltk.tag.sequential import DefaultTagger
    >>> default_tagger = DefaultTagger('NN')
    >>> default_tagger.tag('This is a test'.split())
    [('This', 'NN'), ('is', 'NN'), ('a', 'NN'), ('test', 'NN')]

This tagger is recommended as a backoff tagger, in cases where
a more powerful tagger is unable to assign a tag to the word
(e.g. because the word was not seen during training).

* Parameter: Default tag (The default tag "-None-". Set this to a different tag, such as "NN", to change the default tag.)

  * Default value: -None-
* Output: POS Tagger (A python dictionary containing the POS tagger object and its arguments.)


Widget: POS N-gram Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_image.png
   :width: 50
   :height: 50
A tagger that chooses a token's tag based on its word string and
on the preceding n word's tags.  In particular, a tuple
(tags[i-n:i-1], words[i]) is looked up in a table, and the
corresponding tag is returned.  N-gram taggers are typically
trained on a tagged corpus.

Train a new NgramTagger using the given training data or
the supplied model.  In particular, construct a new tagger
whose table maps from each context (tag[i-n:i-1], word[i])
to the most frequent tag for that context.  But exclude any
contexts that are already tagged perfectly by the backoff
tagger.

* Input: Training Corpus (A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta, or an Annotated Document Corpus in the standard TextFlows' adc format)
* Input: Backoff Tagger (A backoff tagger, to be used by the new tagger if it encounters an unknown context.)
* Parameter: N-gram (N-gram is a contiguous sequence of n items from a given sequence of text or speech.)

  * Default value: 1
* Parameter: Cutoff (If the most likely tag for a context occurs fewer than *cutoff* times, then exclude it from the context-to-tag table for the new tagger.)

  * Default value: 0
* Output: POS Tagger (A python dictionary containing the POS tagger object and its arguments.)


Widget: POS Tagger Hub
-----------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_do_image.png
   :width: 50
   :height: 50
TODO

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: POS Tagger (OpenNLP.Tools.PosTagger.EnglishMaximumEntropyPosTagger)
* Parameter: Sentence's Annotation (System.String)

  * Default value: Sentence
* Parameter: Element's Annotation (System.String)

  * Default value: Token
* Parameter: Output Feature Name (System.String)

  * Default value: POS Tag
* Parameter: Take first k letters from POS tag

  * Possible values: 

    * 1
    * 2
    * 3
    * all

  * Default value: -1
* Output: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))


Widget: Extract POS Tagger Name
--------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_pos_do_image.png
   :width: 50
   :height: 50
Returns a string with pretty POS tagger name.

* Input: POS Tagger
* Output: POS Tagger Name

Category Bag of Words
=====================
Category Latino
---------------
Category Advanced
~~~~~~~~~~~~~~~~~

Widget: Construct BOW Model (Text)
```````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/bow_space_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructBowSpace in package latino. The original function signature: ConstructBowSpace.

* Input: Textual Documents (Array of strings) (System.Object)
* Input: Tokenizer (Latino.TextMining.ITokenizer)
* Input: Stemmer or Lemmatizer (Tagger) (Latino.TextMining.IStemmer)
* Input: Stopwords (Array of Stopwords) (System.Collections.Generic.List`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Parameter: Maximum N-Gram Length (System.Int32)

  * Default value: 2
* Parameter: Minimum Word Freqency (System.Int32)

  * Default value: 5
* Parameter: Word Weighting Type (Latino.TextMining.WordWeightType)

  * Possible values: 

    * Log Df Tf Idf
    * Term Freq
    * Tf Idf
    * Tf Idf Safe

  * Default value: TfIdf
* Parameter: Cut Low Weights Percentage (System.Double)

  * Default value: 0.2
* Parameter: Normalize Vectors (System.Boolean)

  * Default value: true
* Output: Bag of Words Model
* Output: Dataset


Widget: Get Terms
``````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/get_vocabulary_image.png
   :width: 50
   :height: 50
Automatically generated widget from function GetVocabulary in package latino. The original function signature: GetVocabulary.

* Input: BOW Model (Latino.TextMining.BowSpace)
* Parameter: Index of First Retrieved Word (System.Int32)

  * Default value: 1
* Parameter: Maximum Words Retrieved (Use 0 for no limit.)

  * Default value: 0
* Output: Terms


Widget: Process New Documents (Text)
`````````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/process_new_txt_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ProcessNewDocumentsFromString in package latino. The original function signature: ProcessNewDocumentsFromString.

* Input: Documents = (Nested) List of Strings (System.Object)
* Input: Bag of Words Model (Latino.TextMining.BowSpace)
* Output: Dataset


Widget: Create Term Dataset
````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/get_vocabulary_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CreateTermDatasetFromAdc in package latino. The original function signature: CreateTermDatasetFromAdc.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Bag of Words Model (Latino.TextMining.BowSpace)
* Output: Term Dataset


Widget: Construct BOW Model and Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/bow_space_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructBowSpace in package latino. The original function signature: ConstructBowSpace.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Token Annotation (System.String)

  * Default value: Token
* Parameter: Stem Feature Name (System.String)

  * Default value: stem
* Parameter: Stopword Feature Name (System.String)

  * Default value: stopword
* Parameter: Label Document Feature Name (System.String)

  * Default value: label
* Parameter: Maximum N-Gram Length (System.Int32)

  * Default value: 2
* Parameter: Minimum Word Freqency (System.Int32)

  * Default value: 5
* Parameter: Word Weighting Type (Latino.TextMining.WordWeightType)

  * Possible values: 

    * Log Df Tf Idf
    * Term Freq
    * Tf Idf
    * Tf Idf Safe

  * Default value: TfIdf
* Parameter: Cut Low Weights Percentage (System.Double)

  * Default value: 0.2
* Parameter: Normalize Vectors (System.Boolean)

  * Default value: true
* Output: Bag of Words Model
* Output: Dataset


Widget: Parse Document Corpus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ParseDocuments in package latino. The original function signature: ParseDocuments.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Bag of Words Model (Latino.TextMining.BowSpace)
* Output: Parsed Document Corpus


Widget: Get Vocabulary Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/get_vocabulary_image.png
   :width: 50
   :height: 50
Automatically generated widget from function GetVocabularyTable in package latino. The original function signature: GetVocabularyTable.

* Input: Bag of Words Model (Latino.TextMining.BowSpace)
* Parameter: Index of First Retrieved Word (System.Int32)

  * Default value: 1
* Parameter: Maximum Words Retrieved (System.Int32)

  * Default value: 500
* Output: Vocabulary Table


Widget: Create Dataset
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/process_new_adc_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ProcessNewDocumentsFromADC in package latino. The original function signature: ProcessNewDocumentsFromADC.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Bag of Words Model (Latino.TextMining.BowSpace)
* Output: Dataset


Widget: Construct BOW Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/bow_space_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructBowModel in package latino. The original function signature: ConstructBowModel.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Parameter: Token Annotation (System.String)

  * Default value: Token
* Parameter: Stem Feature Name (System.String)

  * Default value: stem
* Parameter: Stopword Feature Name (System.String)

  * Default value: stopword
* Parameter: Label Document Feature Name (System.String)

  * Default value: label
* Parameter: Maximum N-Gram Length (System.Int32)

  * Default value: 2
* Parameter: Minimum Word Freqency (System.Int32)

  * Default value: 5
* Parameter: Word Weighting Type (Latino.TextMining.WordWeightType)

  * Possible values: 

    * Log Df Tf Idf
    * Term Freq
    * Tf Idf
    * Tf Idf Safe

  * Default value: TfIdf
* Parameter: Cut Low Weights Percentage (System.Double)

  * Default value: 0.2
* Parameter: Normalize Vectors (System.Boolean)

  * Default value: true
* Output: Bag of Words Model


Widget: Construct BoW Dataset and BoW Model Constructor
--------------------------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/bow_space_image.png
   :width: 50
   :height: 50
The Construct BoW Dataset and BoW Model Constructor widget takes as an input an ADC data object and generates a sparse BoW model dataset (which can be then handed to i.e. a classifier). The widget takes as an input also several user defined parameters, such as weighting type, minimum word frequency, ngram length ...

Besides the sparse BoW model dataset this widget also outputs a BowModelConstructor instance. This additional object contains settings which allow repetition of the feature construction steps on another document corpus. These settings include the inputted parameters, as well as the learned term weights and vocabulary.

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: Controlled Vocabulary (List of terms which will be used for building the vocabulary. Parameter 'Maximum N-gram Length' from in this widget is also applied to the vocabulary. The final vocabulary is the intersection of the controlled vocabulary and the dataset vocabulary.)
* Parameter: Token Annotation (This is the type of Annotation instances, which mark parts of the document (e.g., words, sentences or a terms), which will be used for generating the vocabulary and the dataset.)

  * Default value: Token
* Parameter: Feature Name (If present, the model will be constructed out of annotations' feature values instead of document text. For example, this is useful when we wish build the BoW model using stems instead of the original word forms.)

  * Default value: Stem
* Parameter: Stopword Feature Name (This is an annotation feature name which was used to tag tokens as stop words. These tokens will be excluded from the BoW representational model. If blank, no stop words will be used.)

  * Default value: StopWord
* Parameter: Label Document Feature Name (This is the name of the document feature which will be used for class labeling examples in the dataset. If blank, the generated sparse dataset will be unlabeled.)

  * Default value: Labels
* Parameter: Maximum N-Gram Length (The upper boundary of the range of n-values for different n-grams to be extracted. All values of n such that 1 <= n <= max_ngram will be used.)

  * Default value: 2
* Parameter: Minimum Word Freqency (When building the vocabulary ignore terms that have a term frequency strictly lower than the given threshold. This value is also called cut-off in the literature.)

  * Default value: 5
* Parameter: Word Weighting Type (The user can select among various weighting models for assigning weights to features)

  * Possible values: 

    * Log Df TF-IDF
    * TF-IDF
    * TF-IDF Safe
    * Term Frequency

  * Default value: tf_idf
* Parameter: Cut Low Weights Percentage (System.Double)

  * Default value: 0.2
* Parameter: Normalize Vectors (The weighting methods can be further modified by vector normalization. If the user opts to use it in TextFlows the L2 regularization is performed.)

  * Default value: true
* Output: Bag of Words Model Constructor (Bag of Words Model Constructor (BowModelConstructor) gathers utilities to build feature vectors from annotated document corpus.)
* Output: BOW Model Dataset (Sparse BOW feature vectors.)


Widget: Create BoW Dataset using the BoW Model Constructor
-----------------------------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/process_new_adc_image.png
   :width: 50
   :height: 50
TODO:

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: Bag of Words Model Constructor (Latino.TextMining.BowSpace)
* Output: BOW Model Dataset (Sparse BOW feature vectors.)

Category Stemming
=================
Category Latino
---------------
Category Advanced
~~~~~~~~~~~~~~~~~

Widget: Stemming Tagger Hub (Text)
```````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stem_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TagStringStemLemma in package latino. The original function signature: TagStringStemLemma.

* Input: Text (System.Object)
* Input: Token Tagger (System.Object)
* Parameter: Output Feature Name (System.String)

  * Default value: stem
* Output: String (string or array of strings (based on the input))


Widget: Lemma Tagger LemmaGen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructLemmaSharpLemmatizer in package latino. The original function signature: ConstructLemmaSharpLemmatizer.

* Parameter: Language (Latino.TextMining.Language)

  * Possible values: 

    * Bulgarian
    * Czech
    * English
    * Estonian
    * French
    * German
    * Hungarian
    * Italian
    * Romanian
    * Serbian
    * Slovene
    * Spanish

  * Default value: English
* Output: Lemmatizer (Tagger)


Widget: Stem Tagger Snowball
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructSnowballStemmer in package latino. The original function signature: ConstructSnowballStemmer.

* Parameter: Language (Latino.TextMining.Language)

  * Possible values: 

    * Danish
    * Dutch
    * English
    * Finnish
    * French
    * German
    * Italian
    * Norwegian
    * Portuguese
    * Russian
    * Spanish
    * Swedish

  * Default value: English
* Output: Stemmer (Tagger)


Widget: Stemming Tagger Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stem_do_image.png
   :width: 50
   :height: 50
Taggs the given annotated document corpus with the given tagger.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Token Tagger (Token Annotation of the token to be tagged. If also the feature name is used than the feature value of selected token will be tagged.
  Usage: 
  1. TokenName
  2. TokenName/FeatureName
  If multiple taggers are used then one line per tagger must be specified.)
* Parameter: Token Annotation (System.String)

  * Default value: Token
* Parameter: Output Feature Name (System.String)

  * Default value: stem
* Output: Annotated Document Corpus

Category Nltk
-------------

Widget: ISRI Stemmer
~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
ISRI Arabic stemmer based on algorithm: Arabic Stemming without a root dictionary. Information Science Research Institute. University of Nevada, Las Vegas, USA. A few minor modifications have been made to ISRI basic algorithm.

See the source code of this module for more information. isri.stem(token) returns Arabic root for the given token. The ISRI Stemmer requires that all tokens have Unicode string types. If you use Python IDLE on Arabic Windows you have to decode text first using Arabic '1256' coding.

* Output: Stemmer (Tagger)


Widget: Regex Stemmer
~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
A stemmer that uses regular expressions to identify morphological affixes.  Any substrings that match the regular expressions will be removed.

* Parameter: Pattern (The regular expression that should be used to
          identify morphological affixes.)
* Parameter: Minimum length of string (The minimum length of string to stem.)

  * Default value: 0
* Output: Stemmer (Tagger)


Widget: RSLP Stemmer
~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
A stemmer for Portuguese.

* Output: Stemmer (Tagger)


Widget: Snowball Stemmer
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
The following languages are supported:
    Danish, Dutch, English, Finnish, French, German,
    Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian,
    Spanish and Swedish.

    The algorithm for English is documented here:
    Porter, M. \"An algorithm for suffix stripping.\"
    Program 14.3 (1980): 130-137.

    The algorithms have been developed by Martin Porter.
    These stemmers are called Snowball, because Porter created
    a programming language with this name for creating
    new stemming algorithms. There is more information available
    at http://snowball.tartarus.org/

* Parameter: Language (The following languages are supported: Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish and Swedish.)

  * Possible values: 

    * Danish
    * Dutch
    * English
    * Finnish
    * French
    * German
    * Hungarian
    * Italian
    * Norwegian
    * Portuguese
    * Romanian
    * Russian
    * Spanish
    * Swedish

  * Default value: danish
* Parameter: Ignore stopwords (If set to True, stopwords are
                           not stemmed and returned unchanged.
                           Set to False by default.)
* Output: Stemmer (Tagger)


Widget: WordNet Lemmatizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
WordNet Lemmatizer
    
Lemmatize using WordNet's built-in morphy function. Returns the input word unchanged if it cannot be found in WordNet.

* Output: Stemmer (Tagger)


Widget: Lancaster Stemmer
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
A word stemmer based on the Lancaster stemming algorithm.

        >>> from nltk.stem.lancaster import LancasterStemmer
        >>> st = LancasterStemmer()
        >>> st.stem('maximum')     # Remove "-um" when word is intact
        'maxim'
        >>> st.stem('presumably')  # Don't remove "-um" when word is not intact
        'presum'
        >>> st.stem('multiply')    # No action taken if word ends with "-ply"
        'multiply'
        >>> st.stem('provision')   # Replace "-sion" with "-j" to trigger "j" set of rules
        'provid'
        >>> st.stem('owed')        # Word starting with vowel must contain at least 2 letters
        'ow'
        >>> st.stem('ear')         # ditto
        'ear'
        >>> st.stem('saying')      # Words starting with consonant must contain at least 3
        'say'
        >>> st.stem('crying')      #     letters and one of those letters must be a vowel
        'cry'
        >>> st.stem('string')      # ditto
        'string'
        >>> st.stem('meant')       # ditto
        'meant'
        >>> st.stem('cement')      # ditto
        'cem'

* Output: Stemmer (Tagger)


Widget: Porter Stemmer
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_image.png
   :width: 50
   :height: 50
This is the Porter stemming algorithm, ported to Python from the version coded up in ANSI C by the author. It follows the algorithm presented in 

Porter, M. "An algorithm for suffix stripping." Program 14.3 (1980): 130-137.

only differing from it at the points marked --DEPARTURE-- and --NEW--
below.

For a more faithful version of the Porter algorithm, see
http://www.tartarus.org/~martin/PorterStemmer/

* Output: Stemmer (Tagger)


Widget: Stem/Lemma Tagger Hub
------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stem_do_image.png
   :width: 50
   :height: 50
Taggs the given annotated document corpus with the given tagger.

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: Token Tagger (Token Annotation of the token to be tagged. If also the feature name is used than the feature value of selected token will be tagged.
  Usage: 
  1. TokenName
  2. TokenName/FeatureName
  If multiple taggers are used then one line per tagger must be specified.)
* Parameter: Token Annotation (System.String)

  * Default value: Token
* Parameter: Output Feature Name (System.String)

  * Default value: Stem
* Output: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))

Category Dataset
================
Category Latino
---------------

Widget: Add Labels
~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/dataset_add_labels_image.png
   :width: 50
   :height: 50
Automatically generated widget from function AddLabelsToDocumentVectors in package latino. The original function signature: AddLabelsToDocumentVectors.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Labeles (Array of Strings) (System.Collections.Generic.List`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Output: Dataset


Widget: Extract Labels
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/dataset_extract_labels_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ExtractDatasetLabels in package latino. The original function signature: ExtractDatasetLabels.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Labels (Array of Strings)


Widget: Remove Labels
~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/dataset_remove_labels_image.png
   :width: 50
   :height: 50
Automatically generated widget from function RemoveDocumentVectorsLabels in package latino. The original function signature: RemoveDocumentVectorsLabels.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Dataset


Widget: Split
~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/dataset_split_simple_image.png
   :width: 50
   :height: 50
Automatically generated widget from function DatasetSplitSimple in package latino. The original function signature: DatasetSplitSimple.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Parameter: Percentage (System.Double)

  * Default value: 10
* Parameter: Random Seed (-1 for random (time dependet) random seed)

  * Default value: -1
* Output: Dataset with Extracted Set
* Output: Dataset of Remaining Sets


Widget: Split to Predefined Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/dataset_split_predef_image.png
   :width: 50
   :height: 50
Automatically generated widget from function DatasetSplitPredefined in package latino. The original function signature: DatasetSplitPredefined.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Sets (List with predefined set numbers) (System.Int32[])
* Input: SetId (System.Int32)
* Output: Dataset with Extracted Set
* Output: Dataset of Remaining Sets


Widget: Dataset to Object
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Automatically generated widget from function DatasetToObject in package latino. The original function signature: DatasetToObject.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Standard Object Representataion of Dataset (List<Tuple<int,string,Dictionary<int,double>>> explained as: (List of Examples)<(Example Tuple)<(Id) int,(Label) string,(BOW Dictionary)<(Word Id) int,(Word Weight) double>>>)


Widget: Object to Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ObjectToDataset in package latino. The original function signature: ObjectToDataset.

* Input: Standard Object Representataion of Dataset (List<Tuple<int,string,Dictionary<int,double>>> explained as: (List of Examples)<(Example Tuple)<(Id) int,(Label) string,(BOW Dictionary)<(Word Id) int,(Word Weight) double>>>)
* Output: Dataset


Widget: Add Labels
-------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/dataset_add_labels_image.png
   :width: 50
   :height: 50
Automatically generated widget from function AddLabelsToDocumentVectors in package latino. The original function signature: AddLabelsToDocumentVectors.

* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Labeles (Array of Strings) (System.Collections.Generic.List`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Output: Dataset

Category Stop Words
===================
Category Latino
---------------
Category Advanced
~~~~~~~~~~~~~~~~~

Widget: Stop Word Tagger Hub (Text)
````````````````````````````````````
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stop_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TagStringStopwords in package latino. The original function signature: TagStringStopwords.

* Input: Text (System.Object)
* Input: Token Tagger (string or array of strings)
* Parameter: Output Feature Name (System.String)

  * Default value: stopword
* Output: String (string or array of strings (based on the input))


Widget: Stop Word Sets
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/get_stop_image.png
   :width: 50
   :height: 50
Automatically generated widget from function GetStopWords in package latino. The original function signature: GetStopWords.

* Parameter: Language (Latino.TextMining.Language)

  * Possible values: 

    * Bulgarian
    * Czech
    * Danish
    * Dutch
    * English
    * Finnish
    * French
    * German
    * Hungarian
    * Italian
    * Norwegian
    * Portuguese
    * Romanian
    * Russian
    * Serbian
    * Slovene
    * Spanish
    * Swedish

  * Default value: English
* Output: StopWords


Widget: Stop Word Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stop_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructStopWordsTagger in package latino. The original function signature: ConstructStopWordsTagger.

* Input: Stopwords (List of stopwords)
* Parameter: Ignore Case (If true than words are marked stopword regardless of their casing.)

  * Default value: true
* Output: Stop Word Tagger


Widget: Stop Word Tagger Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_stop_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TagADCStopwords in package latino. The original function signature: TagADCStopwords.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Token Tagger (System.Object)
* Parameter: Token Annotation (System.String)

  * Default value: Token
* Parameter: Output Feature Name (System.String)

  * Default value: stopword
* Output: Annotated Document Corpus

Category Nltk
-------------

Widget: Stop Word Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stop_image.png
   :width: 50
   :height: 50
Constructs a python stop word tagger object.

* Input: Stop Words (A list or string (stop words separated by new lines) of stop words.)
* Parameter: Ignore Case (If true than words are marked as stop word regardless of their casing.)

  * Default value: true
* Output: Stop Word Tagger (A python dictionary containing the StopWordTagger object and its arguments.)


Widget: Stop Word Tagger Hub
-----------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/tag_stop_do_image.png
   :width: 50
   :height: 50
Apply the *stop_word_tagger* object on the Annotated Document Corpus (*adc*):

1. first select only annotations of type Token Annotation *element_annotation*,
2. apply the stop_word tagger
3. create new annotations *output_feature* with the outputs of the stop word tagger.

* Input: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))
* Input: Stop Word Tagger (A python dictionary containing the stop word tagger object and its arguments.)
* Parameter: Token Annotation (Which annotated part of document to be searched for stopwords.)

  * Default value: Token
* Parameter: Output Feature Name (How to annotate the newly discovered stop word features.)

  * Default value: StopWord
* Output: Annotated Document Corpus (Annotated Document Corpus (workflows.textflows.DocumentCorpus))

Category Similarity Matrix
==========================
Category Latino
---------------

Widget: Calculate Similarity Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/calc_sim_matrix_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CalculateSimilarityMatrix in package latino. The original function signature: CalculateSimilarityMatrix.

* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Parameter: Similarity Threshold (System.Double)

  * Default value: 0
* Parameter: Full Matrix (not only Lower Triangular) (System.Boolean)

  * Default value: true
* Output: Similarity Matrix


Widget: Convert Matrix to Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/sim_matrix_to_table_image.png
   :width: 50
   :height: 50
Automatically generated widget from function SparseMatrixToTable in package latino. The original function signature: SparseMatrixToTable.

* Input: Sparse Matrix (Latino.SparseMatrix`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Output: Matrix Table


Widget: Calculate Similarity Matrix
------------------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/calc_sim_matrix_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CalculateSimilarityMatrix in package latino. The original function signature: CalculateSimilarityMatrix.

* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Parameter: Similarity Threshold (System.Double)

  * Default value: 0
* Parameter: Full Matrix (not only Lower Triangular) (System.Boolean)

  * Default value: true
* Output: Similarity Matrix

Category Clustering
===================
Category Latino
---------------

Widget: KMeans Clusterer
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clusterer_kmeans_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructKMeansClusterer in package latino. The original function signature: ConstructKMeansClusterer.

* Parameter: K (Number of Clusteres) (System.Int32)

  * Default value: 10
* Parameter: Centroid Type (Latino.Model.CentroidType)

  * Possible values: 

    * Avg
    * Nrm L2
    * Sum

  * Default value: NrmL2
* Parameter: Similarity Measure (LatinoInterfaces.SimilarityModel)

  * Possible values: 

    * Cosine
    * Dot Product

  * Default value: Cosine
* Parameter: Random Seed (-1: Use Always Different) (System.Int32)

  * Default value: -1
* Parameter: Eps (System.Double)

  * Default value: 0.0005
* Parameter: Trials (Num of Initializations) (System.Int32)

  * Default value: 1
* Output: Clusterer


Widget: KMeans Fast Clusterer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clusterer_kmenas_fast_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructKMeansFastClusterer in package latino. The original function signature: ConstructKMeansFastClusterer.

* Parameter: K (Number of Clusteres) (System.Int32)

  * Default value: 10
* Parameter: Random Seed (-1: Use Always Different) (System.Int32)

  * Default value: -1
* Parameter: Eps (System.Double)

  * Default value: 0.0005
* Parameter: Trials (Num of Initializations) (System.Int32)

  * Default value: 1
* Output: Clusterer


Widget: Hierarchical Bisecting Clusterer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clusterer_hierarchial_bisec_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructHierarchicalBisectingClusterer in package latino. The original function signature: ConstructHierarchicalBisectingClusterer.

* Parameter: Min Quality (System.Double)

  * Default value: 0.2
* Output: Clusterer


Widget: Clustering Hub
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clustering_hub_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ClusterDocumentVectors in package latino. The original function signature: ClusterDocumentVectors.

* Input: Clusterer (LatinoInterfaces.IClusterer)
* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Clustering Results


Widget: Clustering Results Info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clustering_result_info_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ClusteringResultsInfo in package latino. The original function signature: ClusteringResultsInfo.

* Input: Clustering Results (Latino.Model.ClusteringResult)
* Output: Document Labels (Array of Clusteres Ids)
* Output: Clusters Tree


Widget: View Clusters
~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/cluster_viewer_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ViewClusters_PYTHON in package latino. The original function signature: ViewClusters_PYTHON.

* Input: Clustering Results (System.Object)
* Outputs: Popup window which shows widget's results

Category Scikit
---------------

Widget: k-Means
~~~~~~~~~~~~~~~~
.. image:: ../workflows/static/widget-icons/question-mark.png
   :width: 50
   :height: 50
The KMeans algorithm clusters data by trying to separate samples in n groups of equal variance, minimizing a criterion known as the inertia <inertia> or within-cluster sum-of-squares. This algorithm requires the number of clusters to be specified. It scales well to large number of samples and has been used across a large range of application areas in many different fields.

* Parameter: Number of clusters (The number of clusters to form as well as the number of centroids to generate.)

  * Default value: 8
* Parameter: Max iterations (Maximum number of iterations of the k-means algorithm for a single run.)

  * Default value: 300
* Parameter: Tolerance (Relative tolerance with regards to inertia to declare convergence.)

  * Default value: 1e-4
* Output: Clustering


Widget: Clustering Hub
-----------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/clustering_hub_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ClusterDocumentVectors in package latino. The original function signature: ClusterDocumentVectors.

* Input: Clusterer (LatinoClowdFlows.IClusterer)
* Input: Dataset (Latino.Model.IUnlabeledExampleCollection`1[[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Clustering Results

Category Classification
=======================
Category Latino
---------------

Widget: Nearest Centroid Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_centroid_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructCentroidClassifier in package latino. The original function signature: ConstructCentroidClassifier.

* Parameter: Similarity Model (LatinoInterfaces.SimilarityModel)

  * Possible values: 

    * Cosine
    * Dot Product

  * Default value: Cosine
* Parameter: Normalize Centorids (System.Boolean)

  * Default value: false
* Output: Centroid Classifier


Widget: Naive Bayes Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_naive_bayes_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructNaiveBayesClassifier in package latino. The original function signature: ConstructNaiveBayesClassifier.

* Parameter: Normalize (System.Boolean)

  * Default value: false
* Parameter: Log Sum Exp Trick (System.Boolean)

  * Default value: true
* Output: Classifier


Widget: SVM Binary Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_svm_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructSvmBinaryClassifier in package latino. The original function signature: ConstructSvmBinaryClassifier.

* Parameter: C (zero implies default value ([avg. x*x]^-1))

  * Default value: 0
* Parameter: Biased Hyperplane (System.Boolean)

  * Default value: true
* Parameter: Kernel Type (Latino.Model.SvmLightKernelType)

  * Possible values: 

    * Linear
    * Polynomial
    * Radial Basis Function
    * Sigmoid

  * Default value: Linear
* Parameter: Kernel Parameter Gamma (System.Double)

  * Default value: 1
* Parameter: Kernel Parameter D (System.Double)

  * Default value: 1
* Parameter: Kernel Parameter S (System.Double)

  * Default value: 1
* Parameter: Kernel Parameter C (System.Double)

  * Default value: 0
* Parameter: Eps (System.Double)

  * Default value: 0.001
* Parameter: Max Iterations (System.Int32)

  * Default value: 100000
* Parameter: Custom Parameter String (System.String)
* Output: Classifier


Widget: SVM Multiclass Fast Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_svm_fast_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructSvmMulticlassFast in package latino. The original function signature: ConstructSvmMulticlassFast.

* Parameter: C (System.Double)

  * Default value: 5000
* Parameter: Eps (System.Double)

  * Default value: 0.1
* Output: Classifier


Widget: Majority Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_majority_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructMajorityClassifier in package latino. The original function signature: ConstructMajorityClassifier.

* Output: Classifier


Widget: Maximum Entropy Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_max_entropy_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructMaximumEntropyClassifier in package latino. The original function signature: ConstructMaximumEntropyClassifier.

* Parameter: Move Data (System.Boolean)

  * Default value: false
* Parameter: Num of Iterations (System.Int32)

  * Default value: 100
* Parameter: CutOff (System.Int32)

  * Default value: 0
* Parameter: Num of Threads (System.Int32)

  * Default value: 1
* Parameter: Normalize (System.Boolean)

  * Default value: false
* Output: Classifier


Widget: Maximum Entropy Fast Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_max_entropy_fast_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructMaximumEntropyClassifierFast in package latino. The original function signature: ConstructMaximumEntropyClassifierFast.

* Parameter: Move Data (System.Boolean)

  * Default value: false
* Parameter: Num of Iterations (System.Int32)

  * Default value: 100
* Parameter: CutOff (System.Int32)

  * Default value: 0
* Parameter: Num of Threads (System.Int32)

  * Default value: 1
* Parameter: Normalize (System.Boolean)

  * Default value: false
* Output: Classifier


Widget: Knn Classifier
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_knn_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructKnnClassifier in package latino. The original function signature: ConstructKnnClassifier.

* Parameter: Similarity Model (LatinoInterfaces.SimilarityModel)

  * Possible values: 

    * Cosine
    * Dot Product

  * Default value: Cosine
* Parameter: K (Neighbourhood) (System.Int32)

  * Default value: 10
* Parameter: Soft Voting (System.Boolean)

  * Default value: true
* Output: Classifier


Widget: Knn Fast Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_knn_fast_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructKnnClassifierFast in package latino. The original function signature: ConstructKnnClassifierFast.

* Parameter: K (Neighbourhood) (System.Int32)

  * Default value: 10
* Parameter: Soft Voting (System.Boolean)

  * Default value: true
* Output: Classifier


Widget: Accuracy Claculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/accuracy_calc_from_labels_image.png
   :width: 50
   :height: 50
Automatically generated widget from function AccuracyClaculation in package latino. The original function signature: AccuracyClaculation.

* Input: True Labels (System.Collections.IList)
* Input: Predicted Labels (System.Collections.IList)
* Output: Accuracy
* Output: Statistics (Statistics:confusionMatrix: first level of confusion matrix dictionary present true labels (first input) while the second, inner layer, presents predicted labels (second output).
  Stataistics:additinalScores: dictionary's id presents the label that was considered positive for calculation and dictionary's value are actual additioanl scores.)


Widget: Cross Validation
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classif_cross_valid_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CrossValidation in package latino. The original function signature: CrossValidation.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Parameter: Num of Sets (System.Int32)

  * Default value: 10
* Parameter: Assign Sets Randomly (System.Boolean)

  * Default value: true
* Parameter: Use Seed for Random (System.Boolean)

  * Default value: false
* Parameter: Random Seed (System.Int32)

  * Default value: 0
* Output: Data Object with results


Widget: Cross Validation (Predefined Splits)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classif_cross_valid_predef_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CrossValidationPredefSplits in package latino. The original function signature: CrossValidationPredefSplits.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Sets (List with predefined set numbers) (System.Collections.Generic.List`1[[System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Output: Data Object with results


Widget: Multiple Splits Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classif_cross_valid_predef_image.png
   :width: 50
   :height: 50
Automatically generated widget from function CrossValidationPredefMultiSplits in package latino. The original function signature: CrossValidationPredefMultiSplits.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Input: Multiple Set Indexes (Dictionary with multiple predefined split element indexes. {"train0":[1,2,3],"test0":[4,5],"train1":[2,3,4],"test1":[5,6]})
* Output: Data Object with results


Widget: Predict Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classification_predict_image.png
   :width: 50
   :height: 50
Automatically generated widget from function PredictClassification in package latino. The original function signature: PredictClassification.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Prediction(s)
* Output: Labeled dataset


Widget: Prediction Info
~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/clasification_info_image.png
   :width: 50
   :height: 50
Automatically generated widget from function PredictionInfo in package latino. The original function signature: PredictionInfo.

* Input: Prediction(s) (System.Collections.Generic.List`1[[Latino.Model.Prediction`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Lable(s) (Array of Strings)
* Output: Prediction Info(s)


Widget: Train Classifier Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classifier_train_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TrainClassifier in package latino. The original function signature: TrainClassifier.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Classifier


Widget: View Classifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/classif_result_view_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ViewClasssifications_PYTHON in package latino. The original function signature: ViewClasssifications_PYTHON.

* Input: Prediction(s) (System.Object)
* Outputs: Popup window which shows widget's results

Category Nltk
-------------

Widget: Naive Bayes Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/classifier_naive_bayes_image.png
   :width: 50
   :height: 50
A classifier based on the Naive Bayes algorithm.  In order to find the
probability for a label, this algorithm first uses the Bayes rule to
express P(label|features) in terms of P(label) and P(features|label):

|                       P(label) * P(features|label)
|  P(label|features) = ------------------------------
|                              P(features)

The algorithm then makes the 'naive' assumption that all features are
independent, given the label:

|                       P(label) * P(f1|label) * ... * P(fn|label)
|  P(label|features) = --------------------------------------------
|                                         P(features)

Rather than computing P(featues) explicitly, the algorithm just
calculates the denominator for each label, and normalizes them so they
sum to one:

|                       P(label) * P(f1|label) * ... * P(fn|label)
|  P(label|features) = --------------------------------------------
|                        SUM[l]( P(l) * P(f1|l) * ... * P(fn|l) )

* Parameter: Normalize (System.Boolean)

  * Default value: false
* Parameter: Log Sum Exp Trick (System.Boolean)

  * Default value: true
* Output: Classifier

Category Scikit
---------------

Widget: Decision Tree Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/scikit_Tree-icon.png
   :width: 50
   :height: 50
A decision tree is a decision support tool that uses a tree-like graph or model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility.

* Parameter: Max features (The number of features to consider when looking for the best split:
  If int, then consider max_features features at each split.
  If float, then max_features is a percentage and int(max_features * n_features) features are considered at each split.
  If “auto”, then max_features=sqrt(n_features).
  If “sqrt”, then max_features=sqrt(n_features).
  If “log2”, then max_features=log2(n_features).
  If None, then max_features=n_features.)

  * Default value: auto
* Parameter: Max depth  (The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples. )

  * Default value: 100
* Output: Classifier


Widget: Gaussian Naive Bayes Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/classifier_naive_bayes_image.png
   :width: 50
   :height: 50
Gaussian Naive Bayes.  When dealing with continuous data, a typical assumption is that the continuous values associated with each class are distributed according to a Gaussian distribution.

* Output: Classifier


Widget: Logistic regression Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/scikit_LogisticRegression.png
   :width: 50
   :height: 50
Logistic regression, despite its name, is a linear model for classification rather than regression. Logistic regression is also known in the literature as logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model, the probabilities describing the possible outcomes of a single trial are modeled using a logistic function.

* Parameter: Penalty (Used to specify the norm used in the penalization.)

  * Possible values: 

    * l1
    * l2

  * Default value: l1
* Parameter: C (Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.)

  * Default value: 1.0
* Output: Classifier


Widget: Multinomial Naive Bayes Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/classifier_naive_bayes_image.png
   :width: 50
   :height: 50
The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work.

* Parameter: Fit prior (Whether to learn class prior probabilities or not.
          If false, a uniform prior will be used.)
* Parameter: Alpha (Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing). )

  * Default value: 1.0
* Output: Classifier


Widget: SVM Classifier
~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/classifier_svm_image.png
   :width: 50
   :height: 50
Implementation of Support Vector Machine classifier using libsvm: the kernel can be non-linear but its SMO algorithm does not scale to large number of samples as LinearSVC does. Furthermore SVC multi-class mode is implemented using one vs one scheme while LinearSVC uses one vs the rest.

* Parameter: C (Penalty parameter C of the error term.)

  * Default value: 1.0
* Parameter: Degree (Degree of the polynomial kernel function (‘poly’). Ignored by all other kernels.)

  * Default value: 3
* Parameter: Kernel (Specifies the kernel type to be used in the algorithm. It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable. If none is given, ‘rbf’ will be used. If a callable is given it is used to precompute the kernel matrix.)

  * Possible values: 

    * linear
    * poly
    * precomputed
    * rbf
    * sigmoid

  * Default value: rbf
* Output: Classifier


Widget: SVM Linear Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/classifier_svm_image.png
   :width: 50
   :height: 50
Similar to Support Vector Classification with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better (to large numbers of samples).

* Parameter: C (Penalty parameter C of the error term.)

  * Default value: 1.0
* Parameter: Loss (Specifies the loss function. ‘l1’ is the hinge loss (standard SVM) while ‘l2’ is the squared hinge loss.)

  * Possible values: 

    * l1
    * l2

  * Default value: l2
* Parameter: Penalty (Specifies the norm used in the penalization. The ‘l2’ penalty is the standard used in SVC. The ‘l1’ leads to coef_ vectors that are sparse.)

  * Possible values: 

    * l1
    * l2

  * Default value: l2
* Parameter: Multi class (Determines the multi-class strategy if y contains more than two classes. ovr trains n_classes one-vs-rest classifiers, while crammer_singer optimizes a joint objective over all classes. While crammer_singer is interesting from an theoretical perspective as it is consistent it is seldom used in practice and rarely leads to better accuracy and is more expensive to compute. If crammer_singer is choosen, the options loss, penalty and dual will be ignored.)

  * Possible values: 

    * crammer singer
    * ovr

  * Default value: ovr
* Output: Classifier


Widget: k-Nearest Neighbours Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/scikit_classifiers/static/scikit_classifiers/icons/widget/classifier_knn_image.png
   :width: 50
   :height: 50
Classifier implementing the k-nearest neighbors vote.

* Parameter: Number of neighbors (Number of neighbors to use by default for k_neighbors queries.)

  * Default value: 5
* Parameter: Algorithm (Algorithm used to compute the nearest neighbors:
  ‘ball_tree’ will use BallTree
  ‘kd_tree’ will use KDTree
  ‘brute’ will use a brute-force search.
  ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.
  Note: fitting on sparse input will override the setting of this parameter, using brute force.)

  * Possible values: 

    * ball tree
    * brute
    * kd tree
    * most appropriate (automatically)

  * Default value: auto
* Parameter: Weights (weight function used in prediction. Possible values:
  ‘uniform’ : uniform weights. All points in each neighborhood are weighted equally.
  ‘distance’ : weight points by the inverse of their distance. in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away.
  [callable] : a user-defined function which accepts an array of distances, and returns an array of the same shape containing the weights.
  Uniform weights are used by default.)

  * Possible values: 

    * distance
    * uniform

  * Default value: uniform
* Output: Classifier


Widget: Apply Classifier Hub
-----------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/classification_predict_image.png
   :width: 50
   :height: 50
TODO

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Parameter: Calculate class probabilities (Calculate classification class probabilities. May slow down algorithm prediction.)

  * Default value: true
* Output: Prediction(s)
* Output: Labeled dataset


Widget: Train Classifier Hub
-----------------------------
.. image:: ../workflows/nltoolkit/static/nltoolkit/icons/widget/classifier_train_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TrainClassifier in package latino. The original function signature: TrainClassifier.

* Input: Classifier (Latino.Model.IModel`1[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Input: Dataset (Latino.Model.LabeledDataset`2[[System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[Latino.SparseVector`1[[System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]], Latino, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]])
* Output: Classifier


Widget: Extract Classifier Name
--------------------------------
.. image:: ../workflows/static/widget-icons/question-mark.png
   :width: 50
   :height: 50
Returns a string with pretty classifier name.

* Input: Classifier
* Output: Classifier Name


Widget: Extract Actual and Predicted Values
--------------------------------------------
.. image:: ../workflows/static/widget-icons/question-mark.png
   :width: 50
   :height: 50
Takes as an input classifier predictions and the ADC object, the predictions were made on. Outputs a combined list of actual and predicted values which can be used e.g. by the Classification Statistics widget.

* Input: Predictions (Classification Predictions)
* Input: Dataset (BoW Dataset)
* Output: Actual and Predicted Values (List of Actual and Predicted Values)

Category Lexicology
===================
Category Controlled Vocabularies
--------------------------------

Widget: MeSH vocabulary builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/static/widget-icons/question-mark.png
   :width: 50
   :height: 50
Constructs vocabulary from selected top categories in MeSH hierarchy.

* Parameter: N-grams (Construct n-grams subsets of words from a MeSH term)
* Output: List of MeSH terms (List of MeSH terms.)

Category Helpers
================
Category Tagging
----------------

Widget: Universal Multiple Tagger Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_multiple_do_image.png
   :width: 50
   :height: 50
Automatically generated widget from function TagADCMultiple in package latino. The original function signature: TagADCMultiple.

* Input: Annotated Document Corpus (LatinoInterfaces.DocumentCorpus)
* Input: Token Tagger (System.Collections.IList)
* Parameter: Token Annotation [ / Feature Name ] (one line per each tagger) (Token Annotation of the token to be tagged. If also the feature name is used than the feature value of selected token will be tagged.
  Usage: 
  1. TokenName
  2. TokenName/FatureName
  3. GroupTokenName/TokenName/FatureName
  If multiple taggers are used then one line per tagger must be specified.)

  * Default value: Token
* Parameter: Output Feature Name (one line per each tagger) (Output feature name specifies how the token will be tagged (assigend the feature to)
  If multiple taggers are used then one line per tagger must be specified.)

  * Default value: tag
* Output: Annotated Document Corpus


Widget: Condition Tagger
~~~~~~~~~~~~~~~~~~~~~~~~~
.. image:: ../workflows/latino/static/latino/icons/widget/tag_condition_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ConstructConditionTagger in package latino. The original function signature: ConstructConditionTagger.

* Parameter: Feature Condition (Condition which tokens to include based on their features.
  Format examples:
  -Feature1 (don't include tokens with Feature1 set ta any value)
  -Feature1=Value1 (don't include tokens with Feature1 set to the value Value1)
  -Feature1 +Feature2 (don't include tokens with Feature1 set unless it has also Feature2 set)
  -Feature1=Value1 +Feature2 (don't include tokens with Feature1 set to Value1 unless it has also Feature2 set to any value)...)
* Parameter: output Feature Value (System.String)

  * Default value: true
* Parameter: Put token/feature text as the output feature value (If set to true than token or token's feature text is asigned as output feature value)
* Output: Tagger


Widget: Advanced Object Viewer
-------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/object_advanced_view_image.png
   :width: 50
   :height: 50
Displays any input.

* Input: Object (Any type of object.)
* Parameter: Attribute (The depth of the object display)
* Parameter: Maximum Output Length (System.Int32)

  * Default value: 5000
* Outputs: Popup window which shows widget's results


Widget: Random Cross Validation Sets
-------------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/helper_general.png
   :width: 50
   :height: 50
Automatically generated widget from function RandomCrossValidationSets in package latino. The original function signature: RandomCrossValidationSets.

* Input: Example List (Not required, but if set, then it overrides parameter 'numOfExamples' and len(examples) is used for 'numOfExamples'. This should be a type implementing Count, Count() or Length.)
* Parameter: Num of Examples (This determines the length of the set id list. If input 'examples' is set then len(examples) is used for 'numOfExamples' and this setting is overriden.)

  * Default value: 100
* Parameter: Num of Sets (System.Int32)

  * Default value: 10
* Parameter: Assign Sets Randomly (System.Boolean)

  * Default value: true
* Parameter: Use Seed for Random (System.Boolean)

  * Default value: false
* Parameter: Random Seed (System.Int32)

  * Default value: 0
* Output: Example SetIds List


Widget: Random Sequential Validation Sets
------------------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/helper_general.png
   :width: 50
   :height: 50
Automatically generated widget from function RandomSequentialValidationSets in package latino. The original function signature: RandomSequentialValidationSets.

* Input: Example List (Not required, but if set, then it overrides parameter 'numOfExamples' and len(examples) is used for 'numOfExamples'. This should be a type implementing Count, Count() or Length.)
* Parameter: Num of Examples (This determines the length of the set id list. If input 'examples' is set then len(examples) is used for 'numOfExamples' and this setting is overriden.)

  * Default value: 100
* Parameter: Num of Sets (System.Int32)

  * Default value: 10
* Parameter: Assign Sets Randomly (If not set then sets are exactly evenly distributet across the whole dataset.)

  * Default value: true
* Parameter: Use Seed for Random (System.Boolean)

  * Default value: false
* Parameter: Random Seed (System.Int32)

  * Default value: 0
* Parameter: Size of Train Set (May be specified as absolute number or number foloweed by '%' to denote the percentage of the whole dataset.)

  * Default value: 40%
* Parameter: Size of Test Set (May be specified as absolute number or number foloweed by '%' to denote the percentage of the whole dataset.)

  * Default value: 10%
* Parameter: Size of Space Between Train and Test Set (May be specified as absolute number or number foloweed by '%' to denote the percentage of the whole dataset.)

  * Default value: 1%
* Output: Multiple Set Indexes


Widget: Advanced Object to String Converter
--------------------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/latino_widget_image.png
   :width: 50
   :height: 50
Displays any input.

* Input: Object (Any type of object.)
* Parameter: Attribute (The attribute of the object to display)
* Parameter: Maximum Output Length (System.Int32)

  * Default value: 500000
* Output: Object String Representation


Widget: C#.NET Snippet
-----------------------
.. image:: ../workflows/latino/static/latino/icons/widget/csharp_snippet_image.png
   :width: 50
   :height: 50
Runs c#.NET snippet. You can use variable which is provided on the input by the name "in1" .. "inN". Whatever you want to otput needs to be asigned to the variable "out1" before the code is terminated

* Input: Snippet Input Parameter(s) (input can be accesed as variable "in1" .. "inN" inside the code)
* Parameter: C# Snippet Code (Input can be accesed as variable "in1" .. "inN" inside the code and output can be accesed/assigned as variable "out1" inside the code.)

  * Default value: // This is the C#.NET Code Snippet where you can modify the data.
// Varaible "in1" .. "inN" contains whatever you connected to the input port
// Input variables are correctly typed.
// Whatever is assigned to the variable "out1" will be transfered to the output port.
out1 = in1;
* Parameter: Namespace Section (using directives) (System.String)

  * Default value: using System;
using System.Collections.Generic;
using System.Linq;
using Latino;
using Latino.TextMining;
using LatinoInterfaces;
* Parameter: Additional References (imports) (System.String)

  * Default value: System.dll
System.Xml.dll
System.Core.dll
workflows\textflows_dot_net\bin\Latino.dll
workflows\textflows_dot_net\bin\LatinoWorkflows.dll
workflows\textflows_dot_net\bin\LatinoInterfaces.dll
* Output: out (output can be accesed/assigned as variable "out1" inside the code)
* Output: Console Output
* Output: Possible compile/runtime errors
* Output: Generated Code


Widget: Display Table
----------------------
.. image:: ../workflows/latino/static/latino/icons/widget/table_view_image.png
   :width: 50
   :height: 50
Automatically generated widget from function ShowTable_PYTHON in package latino. The original function signature: ShowTable_PYTHON.

* Input: Table (System.Object)
* Outputs: Popup window which shows widget's results


Widget: Get Multi Set Indexes
------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/helper_general.png
   :width: 50
   :height: 50
Generates multiple set indexes from a list of predefined set numbers. See widgets "Cross Validation (Predefined Splits)" and "Multiple Splits Validation"

* Input: Sets (List with predefined set numbers) (System.Collections.Generic.List`1[[System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]])
* Output: Multiple Set Indexes


Widget: Flatten String Hierarchy
---------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/flatten_string_hierarchy_image.png
   :width: 50
   :height: 50
Automatically generated widget from function FlattenObjectToStringArray in package latino. The original function signature: FlattenObjectToStringArray.

* Input: data (System.Object)
* Output: flatData


Widget: Generate Integer Range
-------------------------------
.. image:: ../workflows/latino/static/latino/icons/widget/range_create_integers_image.png
   :width: 50
   :height: 50
Automatically generated widget from function GenerateIntegerRange in package latino. The original function signature: GenerateIntegerRange.

* Parameter: Start (System.Int32)

  * Default value: 0
* Parameter: Stop (System.Int32)

  * Default value: 10
* Parameter: Step (System.Int32)

  * Default value: 1
* Output: Range


Widget: Python Snippet
-----------------------
.. image:: ../workflows/latino/static/latino/icons/widget/python_snippet_image.png
   :width: 50
   :height: 50
Runs python snippet. You can use variable which is provided on the input by the name "in1" .. "inN". Whatever you want to otput needs to be asigned to the variable "out1" before the code is terminated

* Input: in (input can be accesed as variable "in1" .. "inN" inside the code)
* Parameter: Python Snippet Code (Input can be accesed as variable "in1" .. "inN" inside the code and output can be accesed/assigned as variable "out1" inside the code.)

  * Default value: # This is the Python Code Snippet where you can modify the data however is needed.
# Varaible "in1" .. "inN" contains whatever you connected to the input port
# Whatever is assigned to the variable "out1" will be transfered to the output port.

out1 = in1
* Output: out (output can be accesed/assigned as variable "out1" inside the code)


Widget: Split Object
---------------------
.. image:: ../workflows/latino/static/latino/icons/widget/object_split_image.png
   :width: 50
   :height: 50
Automatically generated widget from function SplitObject_PYTHON in package latino. The original function signature: SplitObject_PYTHON.

* Input: object (System.Object)
* Parameter: Object Modifier (if one wants to extract object's attributes, leading dot should be used.)
* Output: object


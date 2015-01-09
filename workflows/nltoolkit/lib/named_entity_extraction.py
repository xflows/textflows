import nltk

# with open('football.txt', 'r') as f:
#     sample = f.read().encode('ascii', 'ignore')
#
# sentences = nltk.sent_tokenize(sample)
sentences=["CNN.com delivers the latest breaking news and information on the latest top stories, weather, business, entertainment, politics, and more",
           "Flights to London's Gatwick Airport were diverted and departures delayed for a time Monday after a Virgin Atlantic plane made an emergency landing, the airport said."]
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)


def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print set(entity_names)
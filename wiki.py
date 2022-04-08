import wikipedia
from textblob import TextBlob

# Obtain Wikipedia summary method
def getWiki(sentence):
    blob = TextBlob(sentence)
    # POS tag the sentence
    tagged = blob.tags
    # Keep record of any noun phrases in the sentence
    np = blob.noun_phrases
    nn = []
    question = False
    # Determine if the sentence is a question and keep record of any noun(s)
    for word,pos in tagged:
        if pos == 'WP':
            question = True
        if pos == 'NN' or pos == 'NNS':
            nn.append(word)

    # If the sentence is a question, search Wikipedia with the first noun phrase or noun found
    # If the search is ambiguous (multiple pages with the same noun (phrase), ask for clarification
    if question:
        if len(np) != 0:
            try:
                summary = wikipedia.summary(np[0], sentences=1, auto_suggest=False)
                learnMore = " If you would like to learn more, please visit: " + wikipedia.page(np[0], auto_suggest=False).url
                q = ". Is there anything else you would like to share?"
                result = summary + learnMore + q
            except wikipedia.DisambiguationError as e:
                result = "Sorry, could you be more a little more specific? There are many Wikipedia pages with the title '" + np[0] + "' in it."
        else:
            try:
                summary = wikipedia.summary(nn[0], sentences=1, auto_suggest=False)
                learnMore = " If you would like to learn more, please visit: " + wikipedia.page(nn[0], auto_suggest=False).url
                q = ". Is there anything else you would like to share?"
                result = summary + learnMore + q
            except wikipedia.DisambiguationError as e:
                result = "Sorry, could you be more a little more specific? There are many Wikipedia pages with the title '" + nn[0] + "' in it."
        return result
    else:
        return -1

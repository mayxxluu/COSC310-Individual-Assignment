import wikipedia
from textblob import TextBlob

def getWiki(sentence):
    phrase = sentence
    blob = TextBlob(phrase)
    tagged = blob.tags
    np = blob.noun_phrases
    nn = []
    question = False
    for word,pos in tagged:
        if pos == 'WP':
            question = True
        if pos == 'NN' or pos == 'NNS':
            nn.append(word)

    if question:
        if len(np) != 0:
            try:
                print(np[0])
                summary = wikipedia.summary(np[0], sentences=1)
                learnMore = "\nIf you would like to learn more, please visit: " + wikipedia.page(np[0]).url
                q = "\nIs there anything else you would like to share?"
                result = summary + learnMore + q
            except wikipedia.DisambiguationError as e:
                result = "Sorry, could you be more a little more specific? There are many Wikipedia pages with the title '" + np[0] + "' in it."
        else:
            try:
                print(nn[0])
                summary = wikipedia.summary(nn[0], sentences=1)
                learnMore = "\nIf you would like to learn more, please visit: " + wikipedia.page(nn[0]).url
                q = "\nIs there anything else you would like to share?"
                result = summary + learnMore + q
            except wikipedia.DisambiguationError as e:
                result = "Sorry, could you be more a little more specific? There are many Wikipedia pages with the title '" + nn[0] + "' in it."
        return result
    else:
        return -1

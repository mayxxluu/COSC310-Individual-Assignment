from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#stop words are words like the, they and then
stopWords = set(stopwords.words('english'))

class SpellingMistakes:
    def spelling_mistakes(str):
        tokenizer = RegexpTokenizer(r'\w+')
        sentString = tokenizer.tokenize(str)
        count = 0
        for i in sentString:
            strip = i.rstrip()
            if not wn.synsets(strip):
                if not strip in stopWords:
                    while(not wn.synsets(i) or i in stopWords):
                        print("Word you spelt wrong: "+i)
                        val = input("Spell "+i+" again correctly: ")
                        i=val
                        sentString[count] = val
            count += 1
        return sentString
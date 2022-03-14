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
        for words in sentString:
            strip = words.rstrip()
            if not wn.synsets(strip):
                if not strip in stopWords:
                    while(not wn.synsets(words) or words in stopWords):
                        print("Word you spelt wrong: " + words)
                        val = input("Spell " + words +" again correctly: ")
                        words=val
                        sentString[count] = val
            count += 1
        return sentString

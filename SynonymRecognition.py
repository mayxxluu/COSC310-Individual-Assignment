import nltk # Import NLTK to use wordnet
from nltk.corpus import wordnet   #Import wordnet from the NLTK
# You can find tag information: https://www.guru99.com/pos-tagging-chunking-nltk.html
class SynonymRecognition:
    def synonym_recognition(word, tag): # Takes in a word and a tag from POS tagger
        synonym_list = [] # Stores the synonym
        # Wordnet only supports 4 tags: Nouns, verbs, adjectives and adverbs
        # Wordnet stores synonyms in a 2-d list, therefore we must use 2 loops to get all lists
        
        # NLTK has 2 tags NN: noun, singular  and NNS: noun plural
        if tag == "NN" or tag == "NNS":
            # Going through wordnet to get all noun synonyms
            for i in wordnet.synsets(word, pos = wordnet.NOUN):
                for j in i.lemmas():
                    synonym_list.append(j.name())    #add the synonyms
            return synonym_list
        
        # NLTK has 3 tags RB: adverb (occasionally, swiftly), singular and RBR: adverb, comparative (greater)
        #                 RBS: adverb, superlative (biggest)
        elif tag == "RB" or tag == "RBR" or tag == "RBS":
            # Going through wordnet to get all adverb synonyms
            for i in wordnet.synsets(word, pos = wordnet.ADV):
                for j in i.lemmas():
                    synonym_list.append(j.name())    #add the synonyms
            return synonym_list
        
        # NLTK has 3 tags JJ: This NLTK POS Tag is an adjective (large), JJR: adjective, comparative (larger), and 
        #                 JJS: adjective, superlative (largest)
        elif tag == "JJ" or tag == "JJR" or tag == "JJS":
            # Going through wordnet to get all adjective synonyms
            for i in wordnet.synsets(word, pos = wordnet.ADJ):
                for j in i.lemmas():
                    synonym_list.append(j.name())    #add the synonyms
            return synonym_list

        # NLTK has 6 VB: verb (ask), VBG: verb gerund (judging), VBD: verb past tense (pleaded)
        #            VBN: verb past participle (reunified), VBP: verb, present tense not 3rd person singular(wrap)
        #            VBZ: verb, present tense with 3rd person singular (bases)
        elif tag == "VB" or tag == "VBG" or tag == "VBD" or tag == "VBN" or tag == "VBP" or tag == "VBZ":
            # Going through wordnet to get all VERB synonyms
            for i in wordnet.synsets(word, pos = wordnet.VERB):
                for j in i.lemmas():
                    synonym_list.append(j.name())    #add the synonyms
            return synonym_list
        # In case tag is not the 4 tags: Nouns, verbs, adjectives and adverbs
        return synonym_list

# Test cases
#print(SynonymRecognition.synonym_recognition("tree", "NN"))
#print(SynonymRecognition.synonym_recognition("desks", "NNS"))

#print(SynonymRecognition.synonym_recognition("swiftly", "RB"))
#print(SynonymRecognition.synonym_recognition("greater", "RBR"))
#print(SynonymRecognition.synonym_recognition("biggest", "RBS"))

#print(SynonymRecognition.synonym_recognition("large", "JJ"))
#print(SynonymRecognition.synonym_recognition("larger", "JJR"))
#print(SynonymRecognition.synonym_recognition("largest", "JJS"))

#print(SynonymRecognition.synonym_recognition("ask", "VB"))
#print(SynonymRecognition.synonym_recognition("judging", "VBG"))
#print(SynonymRecognition.synonym_recognition("pleaded", "VBD"))
#print(SynonymRecognition.synonym_recognition("reunified", "VBN"))
#print(SynonymRecognition.synonym_recognition("wrap", "VBP"))
#print(SynonymRecognition.synonym_recognition("bases", "VBZ"))

#print(SynonymRecognition.synonym_recognition("sdf", "UH"))
#print(SynonymRecognition.synonym_recognition("", "TO"))
#print(SynonymRecognition.synonym_recognition("sdf", ""))
#print(SynonymRecognition.synonym_recognition("WRB", "WRB"))
#print(SynonymRecognition.synonym_recognition("", ""))



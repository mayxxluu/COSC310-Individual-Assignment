import spacy_universal_sentence_encoder

class spaCySentenceSimilarity:
    def spaCy_sentence_similarity(userIn, databaselist):
        # this loads the data
        nlp = spacy_universal_sentence_encoder.load_model('en_use_md')

        # preps spacy with userIn
        userSentence = nlp(userIn)
        bestMatchScore = 0
        bestSentence = ""
        for i in range(len(databaselist)):
            # preps spacy with current prompt in the database
            databaseSentence = nlp(databaselist[i][0])
            # gets the similarity value
            matchScore = databaseSentence.similarity(userSentence)
            # checks if the similarity value is better than the best value
            if(matchScore > bestMatchScore):
                bestMatchScore = matchScore
                bestSentence = databaselist[i][1]
        return bestSentence, bestMatchScore
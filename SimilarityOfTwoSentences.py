from turtle import pos
from SentencePOSTagger import SentencePOSTagger
from SynonymRecognition import SynonymRecognition

from DatabaseToList import DatabaseToList

class SimilarityOfTwoSentences:
    def sentence_similarity(userIn, prompt):
        # A speical case where nothing is inputed
        if len(userIn) == 0 and len(prompt) == 0:
            return round(1.0000, 3)
        
        # splits the user's input sentence to compare
        userSplit = userIn.split()
        
        # splits a database sentence to compare
        promptSplit = prompt.split()
        
        #  used to count the number of sentence_similarities
        count = 0

        # get the POS tags of the user's input sentence
        posUserIn = SentencePOSTagger.sentence_pos_tagger(userIn)
        
        correctValue = 0
        
        if (len(userSplit) <= len(promptSplit)):
            i=0
            while(i < len(userSplit)):
                # call SynonymRecognition and store the list of synonym into synonym
                synonym = SynonymRecognition.synonym_recognition(posUserIn[i][0], posUserIn[i][1])
                # Determines if a word in the input string matches an answer in our database
                # or whether the userSplit[i] matches any word from synonym
                if(userSplit[i] == promptSplit[i] or userSplit[i] in synonym):
                    count+=1
                i+=1
            # in case prompt is inputed nothing
            if len(promptSplit) == 0:
                correctValue = 0.0
            else:
                correctValue = count / len(promptSplit)
        else:
            i=0
            while(i < len(promptSplit)):
                # call SynonymRecognition and store the list of synonym into synonym
                synonym = SynonymRecognition.synonym_recognition(posUserIn[i][0], posUserIn[i][1])
                # Determines if a word in the input string matches an answer in our database
                # or whether the userSplit[i] matches any word from synonym
                if(userSplit[i] == promptSplit[i]): #determines if a word in the input string matches an answer in our database
                    count+=1
                i+=1
            # in case prompt is inputed nothing
            if len(promptSplit) == 0:
                correctValue = 0.0
            else:
                correctValue = count / len(promptSplit)

        return round(correctValue, 3)

# speical case
#print(SimilarityOfTwoSentences.sentence_similarity("", ""))

#print(SimilarityOfTwoSentences.sentence_similarity("", "I like candy"))

#print(SimilarityOfTwoSentences.sentence_similarity("I like cats", ""))

#print(SimilarityOfTwoSentences.sentence_similarity(" ", " "))

#print(SimilarityOfTwoSentences.sentence_similarity("", " "))

#print(SimilarityOfTwoSentences.sentence_similarity(" ", ""))

# Cases where the both sentences equal each aother 
#print(SimilarityOfTwoSentences.sentence_similarity("I like cats", "I desire cats"))

#print(SimilarityOfTwoSentences.sentence_similarity("I like feline", "I desire cats"))

# why is the sentence below 0.333? Because "like" is no-longer a has the tag VBP, but the tag IN. Therefore, the 
# synonym is different
#print(SimilarityOfTwoSentences.sentence_similarity("My like feline", "I desire cats"))

#print(SimilarityOfTwoSentences.sentence_similarity("My like feline", "My desire cats"))

#print(SimilarityOfTwoSentences.sentence_similarity("My like feline ", "My desire cats"))

#print(SimilarityOfTwoSentences.sentence_similarity("My like feline", "My desire cats "))

##print(SimilarityOfTwoSentences.sentence_similarity(" My like feline", "My desire cats"))

#print(SimilarityOfTwoSentences.sentence_similarity("My like feline", " My desire cats"))

# Cases where user's input sentence greater than the database sentence
#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy", "I want candy"))

#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy as well", "I perpetually want candy"))

#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy alot", "I perpetually want sweets"))

#print(SimilarityOfTwoSentences.sentence_similarity(" I always wanted candy alot", "I perpetually want sweets"))

#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy alot", " I perpetually want sweets"))

#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy alot", "I perpetually want sweets "))

#print(SimilarityOfTwoSentences.sentence_similarity("I always wanted candy alot ", "I perpetually want sweets"))

# Cases where user's input sentence less than the database sentence
#print(SimilarityOfTwoSentences.sentence_similarity("I want friends", "I want friends a lot"))

#print(SimilarityOfTwoSentences.sentence_similarity("I desire friends", "I want friends a lot"))

#print(SimilarityOfTwoSentences.sentence_similarity("I want friends", "I want friends a lot"))

# notice how companion is a synonym for friends, but not the other way around
#print(SimilarityOfTwoSentences.sentence_similarity("I want companion", "I want friends a lot"))

#print(SimilarityOfTwoSentences.sentence_similarity("I desire companion", "I want friends a lot"))

# notice how companion is a synonym for friend, but not the other way around
#print(SimilarityOfTwoSentences.sentence_similarity("I desire a companion", "I desire a friend"))

#print(SimilarityOfTwoSentences.sentence_similarity("I desire a friend", "I desire a companion"))

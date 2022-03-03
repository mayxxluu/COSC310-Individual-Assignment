class SimilarityOfTwoSentences:
    def sentence_similarity(userIn, prompt):
        userSplit = userIn.split()
        promptSplit = prompt.split()
        count = 0

        if (len(userSplit) <= len(promptSplit)):
            i=0
            while(i < len(userSplit)):
                if(userSplit[i] == promptSplit[i]): #determines if a word in the input string matches an answer in our database
                    count+=1
                i+=1
        correctValue = count / len(promptSplit)

        return round(correctValue, 3)
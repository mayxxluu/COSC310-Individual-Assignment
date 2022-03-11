from DatabseTopicPrompt import DatabseTopicPrompt

class BotTopicQuestionAsked:
    def bot_topic_question_asked(botTopicList):
        databasePrompt,databaseTopicLength = DatabaseTopicPrompt.database_topic_prompt()
        if len(botTopicList) == databaseTopicLength:
            botTopicList = []
            return databasePrompt
        else:
            while databasePrompt in botTopicList:
                databasePrompt,databaseTopicLength = DatabaseTopicPrompt.database_topic_prompt()
            return databasePrompt
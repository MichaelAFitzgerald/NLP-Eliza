import re


# function that will take the outputted sentence and concat the eliza string to the beginning
def elizaReply(sentence):
    newString = elStr + sentence
    print(newString)


# function that will break a sentence into words by whitespace
def parseInput(sentence):
    sentence = sentence.lower()
    return re.split('\s+', sentence)


# function to be used to take the introductory reply by the user and get their username
def getUserName(sentence):
    wordList = ['hello', 'my', 'name', 'is', 'am', 'i', 'the', "i'm"]
    initialList = parseInput(sentence)
    for word in initialList:
        if word not in wordList:
            userName = word
            userName = userName.capitalize()
            return userName
    print('I am sorry, I do not understand. Please try again')
    tryAgain = input('Please enter your name: ')
    againSentence = parseInput(tryAgain)
    return getUserName(againSentence)


# function that will set the user string after the username has been established
def setUserStr(userName):
    return '=>[' + userName + ']: '


# function that will first parse for any particular keywords
# if none are found in the sentence, will then look for the tense of the sentence
# then send a reply in the rogerian style
def getResponse(sentence):
    # Need to first look for the keywords, then proceed if there's no match
    # This works for present tense

    # I need to change these so that they actually use regex's to a more complete degree
    # function to get the subject of a statement?

    presentResponse = re.sub('I', "Why do you", sentence)
    # Include a regex that will look for a past tense word and change the response
    pastResponse = re.sub('I', "Why did you", sentence)
    # I need to also include a confusion statement
    confusionResponse = "I'm sorry, I didn't understand"
    # Include a regex for future tense statements
    futureResponse = re.sub('I', "Why are you", sentence)
    # future response but with 'am'
    futureAmResponse = re.sub('I am', 'Why are you', sentence)
    # response with a regex to get feel or want
    # method for this?

    word = catchSpecificWord(sentence)
    if word == 'future':
        return futureResponse
    elif word == 'are':
        return futureResponse
    elif word == 'am':
        return futureAmResponse
    elif word == 'want' or word == 'feel':
        return re.sub('I( am)*', 'Why do you ' + word, sentence)
    elif word != 'false':
        return specificWordResponse(word)
    else:
        # need to be able to tell what is the appropriate response to use
        # probably a method to check the tense of a sentence
        wordTense = catchSentenceTense(sentence)
        if wordTense == 'present':
            response = presentResponse
        elif wordTense == 'past':
            response = pastResponse
        elif wordTense == 'future':
            response = futureResponse
        elif wordTense == 'confusion':
            response = confusionResponse
        else:
            response = presentResponse
        return response


# function to check each word in the sentence against the list of specified words
def catchSpecificWord(sentence):
    wordList = parseInput(sentence)
    for word in wordList:
        if word in specificWords:
            return word
    return 'false'


# function that returns specific responses if the user has inputted a sentence
# with a specific word within
def specificWordResponse(word):
    if 'crav' in word:
        return 'Tell me about your cravings'
    elif 'some' in word or 'thing' in word:
        return 'Could you give me an example'
    elif 'go' in word:
        return 'future'
    elif word == 'am':
        return 'are'
    elif word == 'hello':
        return 'Hello, how are you'
    elif 'feel' in word:
        return 'Tell me how you are feeling'
    elif 'want' in word:
        return 'want'


# function that attempts to figure out the tense of the sentence based on the endings of verbs in the sentence
# should also catch nonsensical sentences and return a confusion string
def catchSentenceTense(sentence):
    tenseList = parseInput(sentence)
    for word in tenseList:
        if 'ing' in word:
            return 'present'
        elif 'ed' in word:
            return 'past'
    return 'confusion'


# string that will precede all statements made by eliza
elStr = '->[Eliza]: '

# collection of specific words to catch
specificWords = ['crav', 'some', 'go', 'hello', 'feel', 'thing', 'want', 'am']

# initialization of the eliza bot
elizaReply('Hello, I am Eliza, a helpful psychotherapist')
elizaReply('Could you tell me your name?')
nameStr = input('Please enter your name: ')

# take the list and get the name
userName = getUserName(nameStr)
# string that will precede all statements made by the user
userStr = setUserStr(userName)
elizaReply('Hello ' + userName + '! What is on your mind?')

# after initialization, we continue the loop of the eliza bot
# until the user force quits the application or types 'quit'
while True:
    # string that will contain the input from the user, to be edited and parsed
    userInput = input(userStr)
    if userInput.lower() == 'quit':
        elizaReply('Have a great day!')
        break
    else:
        elizaReply(getResponse(userInput) + '?')

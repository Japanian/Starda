import re

def probCheck(userMessage, recongnizedWords, singleResponse=False, requiredWords=[]):
    messagePts = 0
    hasRequiredWords = True

    for word in userMessage:
        if word in recongnizedWords:
            messagePts += 1

    prc = float(messagePts) / float(len(recongnizedWords))

    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break

    if hasRequiredWords or singleResponse:
        return int(prc * 100)
    else:
        return 0

def verify(message):
    probList = {}

    def response(botResponse, wordsList, singleResponse=False, requiredWords=[]):
        nonlocal probList
        probList[botResponse] = probCheck(message, wordsList, singleResponse, requiredWords)

    # Responses List
    # response("awnser", [what the user have to say], )

    response("Hello!", ["hello", "hey", "hi"], singleResponse=True)
    response("I am a bot created by Japanian", ["who", "are", "you", "u"], requiredWords=["who"])

    bestMatch = max(probList, key=probList.get)
    print(probList)
    return "Sorry I didn\'t understood, can you repeat?" if probList[bestMatch] < 1 else bestMatch

def botResponse(input):
    splitted = re.split(r'\s+|[,;?!.-]\s*', input.lower())
    response = verify(splitted)
    return response

def main():
    print("Hi! I'm Starda, the chatbot made by Japanian")
    while True:
        print(botResponse(input("> ")))
#!usr/bin/python3
def multiple_returns(sentence):
    # check if the sentence is empty
    if not sentence:
        # return None as the first character if the sentence is empty
        return (0, None)
    
    # otherwise, return the length of the sentence and its first character
    return (len(sentence), sentence[0])

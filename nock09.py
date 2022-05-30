import random


def random_middle_sentence(sentence):
    result = []
    for word in sentence.split():
        if len(word)>4:
            word = word[0] + "".join(random.sample(list(word[1:-1]),len(word[1:-1]))) +word[-1]
        result.append(word)
    return " ".join(result)
""
        
    # sentence_middle = sentence[1:-1]

    # if len(sentence_middle)>4:
    #     sentence_middle = random.sample(list(sentence_middle),len(sentence_middle))
    #     sentence_middle = "".join(sentence_middle)
    #     result = sentence[0] +  sentence_middle +sentence[-1]
    # else:
    #     result = sentence
    # return result

sentence1 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(random_middle_sentence(sentence1))

sentence2 = "fuck"
print(random_middle_sentence(sentence2))
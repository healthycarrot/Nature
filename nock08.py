def cipher(sentence):
    return "".join([chr(219-ord(st)) if(st.isascii() and st.islower()) else st for st in sentence ])

sentence = 'the quick brown fox jumps over the lazy dog'
sentence = cipher(sentence)

print(sentence)

sentence = cipher(sentence)

print(sentence)
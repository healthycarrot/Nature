sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = []
word = ""
for char in sentence:

    if char != " " and char !=","  and char != ".":
        word += char
    elif len(word)>0:
        number = len(word)
        words.append(number)
        word = ""


print(words)

# import re

# str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
# str = re.sub('[,\.]', '', str)  # ,と.を除去
# splits = str.split()  # スペースで区切って単語ごとのリストを作成
# ans = [len(i) for i in splits]

# print(ans)




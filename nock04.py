import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

sentence_no_dot = re.sub("[,\.]","",sentence)

words = sentence_no_dot.split()

print(words)

ans = dict()

i=1
for word in words:
    if i==1:
        ans[i] = word[0]
    elif i>=5 and i<=9:
        ans[i] = word[0]
    elif i>=15 and i<=16:
        ans[i] = word[0]
    elif i == 19:
        ans[i] = word[0]
    else:
        ans[i] = word[0]+word[1]
    i = i+1

print(ans)

# str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
# splits = str.split()
# one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 1文字を取り出す単語の番号リスト
# ans = {}
# for i, word in enumerate(splits):
#   if i + 1 in one_ch:
#     ans[word[:1]] = i + 1  # リストにあれば1文字を取得
#   else:
#     ans[word[:2]] = i + 1  # なければ2文字を取得

# print(ans)
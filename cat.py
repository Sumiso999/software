#coding: UTF-8
import builtins


f = open('text.txt','r',encoding = 'UTF-8')

data = f.read()
print(data)

sitei = input('指定のひらがなを入力してください：')

print('この文の中に「' + sitei + '」は' + str(data.count(sitei)) +'個です' )

f.close
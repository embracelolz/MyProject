import io
def load_dic():
    path="dict_no_space.txt"
    text=[]
    file = io.open(path,"r",encoding="utf-8")
    for line in file:
        text.append(line.split("\n")[0])
    return text

def forward_segment(text,dic):
    word_list=[]
    i=0
    while i<len(text):
        longest_word=text[i]
        for j in range(i+1,len(text)+1):
            word=text[i:j]
            if word in dic:
                if len(word)>len(longest_word):
                    longest_word=word
        word_list.append(longest_word)
        i+=len(longest_word)
    return word_list

dic=load_dic()
print(forward_segment("曾文水庫只剩6％！北水南送救旱災　水利署曝難度",dic))
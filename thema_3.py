from nltk.tokenize import word_tokenize #  single import for  split the phrase into single words
from nltk.corpus import wordnet as wn # for synonyms or similar words
from nltk.tag import pos_tag # in order to find if a word is  averb, a noun, adj, adverbe etc.

phrase1 = raw_input("Enter the first phrase: ")
phrase2 = raw_input("Enter the second phrase: ")


List1 = word_tokenize(phrase1) # diaxwrismos protashs se lexeis
List2 = word_tokenize(phrase2)
pos1 = pos_tag(List1) # xarakthrismos kathe lexhs ws rhma, epitheto, ousiastiko, epirrhma klp
pos2 = pos_tag(List2)

ex1 = [] #dhmiourgia listas
ex2 = []

def append_to_list(i,pos,list,ex): #ean h leksh einai epitheto, rhma h ousiastiko tote ti prostathetw se mia nea lista i opoia perilamvanei ta synonima autis tis lexhs

        if pos[i][1] == "VB" or pos[i][1] == "VBD" or pos[i][1] == "VBG" or pos[i][1] == "VBN" or pos[i][1] == "VBP" or pos[i][1] == "VBZ" or  pos[i][1] == "JJ" or pos[i][1] == "JJR" or pos[i][1] == "JJS" or pos[i][1] == "NN" or pos[i][1] == "NNS" or pos[i][1] == "NNP" or pos[i][1] == "NNPS" or pos[i][1] == "" :
            ex.append(wn.synsets(pos[i][0])) #variable ex einai i lista me nta synwnyma twn rimatwn, epithewtwn , ousaistikwn  mias protashs.
        return ex


for i in range(0,len(pos1)):
   append_to_list(i, pos1, List1, ex1)

for i in range(0,len(pos2)):
    append_to_list(i, pos2, List2, ex2)

pl=0
for i in range(0,len(ex1)): # ean mia lexh ths 1hs frashs einai idia me mia lexh ths 2hs frashs, tote metrame se poses lexeis symvainei auto
    for j in range(0,len(ex2)):
        if ex1[i] == ex2[j]:
            pl+=1

if pl == 1:
    print "There is", pl, "common word."
else:
    print "There are", pl, "common words."


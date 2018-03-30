import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

text=[]
file=[]

#taking input of given 10 txt documents

for i in range(10):
    
    text=[]
    file.append(input())

    filename = file[i] 
    file1 = open(filename, 'r')
    text = file1.read().split()
    file1.close()

    
    
    print("\n")
    print("Named Entity Extraction on Document")

    for item1 in text:
        doc=nlp(item1)
        for ent in doc.ents:
            print(ent.text,'/',ent.label_)          

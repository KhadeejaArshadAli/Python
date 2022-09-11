f=open(r"C:\Users\user 2\Desktop\frequency.txt")
sentence=f.read()
print ("The sentence on the text file is :\n",sentence)
frequency={}
for i in sentence:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
    
print ("The frequency of all chracters in the given sentence is :\n"
                                                     + str(frequency))
for characters in sentence:
       ascii=ord(characters)
       print(characters,"\t",ascii)
   

from graphs import Vertex, Graph

wordlist='wordlist.txt'
file=open(wordlist,r)

words={}
g = Graph()

# create word buckets and add words associated with each bucket
for line in file:
    word = line[:-1]
    for i in range(len(word)):
        wordbucket=word[:i]+'_'+word[i:]

        # if word doesnt exist in words dict add it to the list for that bucket
        if wordbucket in words:
            words[wordbucket].append(word)
        # add first word bucket to dictionary
        else:
            words[wordbucket]=[word]

 # Connect all the words within each work bucket together   
for wordbucket in words.keys():
    for word1 in words[wordbucket]:
        for word2 in words[wordbucket]:
            g.addEdge(word1,word2)




from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

all_documents = []
def hash(word):
	length = len(word)
	hashed = 0
	for index in range(length):
		hashed = hashed + (index + 1)*ord(word[index])
	if hashed == 0:
		print(word)
	return hashed

def readfile(doc2read):
	with open(doc2read) as f:
		docus = f.readlines()
	for docu in docus:
		all_documents.append(word_tokenize(docu))
	stop_words = stopwords.words('english')
	new_stops = ["I",".","like",'If','-','(',')',"''",',','``','The','Not','And','<','>','/','br',"'s",'It',"n't",'good','br','This',"''",'would','...','great','really','She','she','My',"'ve"]
	punctuation = list(string.punctuation)
	new_stops.extend(punctuation)
	stop_words.extend(new_stops)
	for stop in stop_words:
		for doc in all_documents:
			for wor in doc:
				if stop == wor:
					doc.remove(wor)

readfile("test.txt")



print(all_documents)
new_all_documents = []
for document in all_documents:
	tmp = []
	for word in document:
		tmp.append(hash(word))
	new_all_documents.append(tmp)
docs = []
for document in new_all_documents:
	docx = ""
	for word in document:
		docx = docx + " " + str(word)
	docs.append(docx)

print(docs)
with open('brewer.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % doc for doc in docs)






# pip install spacy
# python -m spacy download en_core_web_sm
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.request import urlopen
from io import StringIO
from io import BytesIO
#from urllib2 import Request, urlopen
#from StringIO import StringIO
from bs4 import BeautifulSoup

import spacy
import codecs
import PyPDF2 

########################
####  html to text  ####
########################
website = "https://blogs.oracle.com/can-data-be-exciting-v2"
html = urlopen(website).read()
soup = BeautifulSoup(html, "html.parser") #gets rid of html stuff

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
websiteText = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in websiteText.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
websiteText = '\n'.join(chunk for chunk in chunks if chunk)

print ("#############################################")
print ("### website text - stripped of html tags  ###")
print ("#############################################" '\n')
print(websiteText)
print ('\n' '\n')


######################
#### PDF to TEXT  ####
######################
url = 'http://www.oracle.com/us/dm/odc-1st-3rd-partydata-4434136.pdf' 
remoteFile = urlopen(url).read()
#remoteFile = urlopen(Request(url)).read()
memoryFile = BytesIO(remoteFile)
pdfFile = PyPDF2.PdfFileReader(memoryFile)

#open allows you to read the file
#pdfFileObj = open(pdfFile,'rb')

#The pdfReader variable is a readable object that will be parsed
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfFile.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfFile.getPage(count)
    count +=1
    text += pageObj.extractText()

#check pdf is turned to string
print ("##################################")
print ("### pdf parsed into plain text ###") 
print ("##################################" '\n')
print(text)
print (' \n \n ')


######################
####  spaCy stuff ####
######################

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm') 

#text = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
#doc = nlp(text) # process it
#doc.to_disk('/customer_feedback_627.bin') # save the processed Doc

# Process the text for webpage
print ("##############################################")
print ("### processed keywords from the parsed PDF ###")
print ("##############################################"  '\n')
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

print (' \n \n ')


#nlp different newspaper articles
nprDoc = codecs.open('npr.txt', encoding="utf-8").read() # open a document
doc1 = nlp(nprDoc) # process it    

bloombergDoc = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
doc2 = nlp(bloombergDoc) # process it

chinaDoc = codecs.open('newspaper-from-china.txt', encoding="utf-8").read() # open a document
doc3 = nlp(chinaDoc) #process it

# Determine semantic similarities
print ("################################################################################################################")
print ("### semantic similarities - Comparing the same article published by NPR, Bloomberg & Chinese Newspaper #########")
print ("################################################################################################################")
print (' \n ' )

#doc1 = nlp(u"A federal criminal court had in January convicted Sinovel of paying an Austria-based employee of American Superconductor Corp. to steal the source code for #software that powered wind turbines. ")
#doc2 = nlp(u"Chinese turbine maker Sinovel Wind Group Co. must pay $59 million for stealing trade secrets from wind technology firm, American Superconductor Corp., a U.S. #judge ruled.")
similarity = doc1.similarity(doc2)
print(doc1.text) 
print('\n \n \n') 
print(doc2.text)
print ('\n') 
print ("########################################################")
print ("### similarity score between npr & bloomberg ###########")
print ("########################################################")
print ('\n')
print(similarity)
print ('\n')
print ("####################################################################")
print ("### similarity score between npr and chinese newspaper's version ###")
print ("####################################################################")
print ('\n')
similarityTwo = doc1.similarity(doc3)
print(similarityTwo)

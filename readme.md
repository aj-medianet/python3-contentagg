This python script uses SpaCy - https://github.com/explosion/spaCy

Here's what it does:

1. Takes a website url, strips it of it's html tags, gives plain text
2. Takes a pdf and converts it to plain text
3. Parses keywords from the website and/or pdf
4. Can take 2 articles/text and gives a similarity score. Uses SpaCy's NLP to process each article using vector objects. 
   Great for flaggin duplicates.
   
   
**************************************************************************
   
To run the program from the command line with python 3:

git clone git@github.com:aj-medianet/content-aggregator.git

cd content-aggregator/

source venv/bin/activate

**************************************************************************

Install python libraries - you must already have pip installed:

pip3 install bs4

pip3 install spacy

pip3 install PyPDF2

python3 -m spacy download en

**************************************************************************

Then run the program:

python main.py

**************************************************************************

To get out of the virtual envirnment run:

deactivate

**************************************************************************
   
Future developments:

1. Smart keywords & machine learning on those keywords.
2. Add a summarizer option


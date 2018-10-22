This python script uses SpaCy - https://github.com/explosion/spaCy

Here's what it does:

1. Takes a website url, strips it of it's html tags, gives plain text
2. Takes a pdf and converts it to plain text
3. Parses keywords from the website and/or pdf
4. Can take 2 articles/text and gives a similarity score. Uses SpaCy's NLP to process each article using vector objects. 
   Great for flaggin duplicates.
   
Future developments:

1. Smart keywords & machine learning on those keywords.
2. Add a summarizer option


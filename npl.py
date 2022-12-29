import spacy
import pt_core_news_sm
# Load the English language model
nlp = pt_core_news_sm.load()
# Define the input text
text = "Eu amo Pizza"

# Process the text using the NLP model



doc = nlp(text)
# Iterate over the tokens in the document

for chunk in doc:
    print(chunk.text)
    
# Output: the quick brown fox jump over the lazy dog .

# Spacy is the features 

# Tokenization ? Segmenting Text into words punctuantions Mark etc
# Part-of-speech Assigning word types to tokens like verb or noun


# Dependency Parsing ? Assigning syntactic dependency
# labes describing the relations between Individual tokens like 
# betweeen individual tokens like subject or object

# Text Classification Assigning Categories or labels to a whole document, or parts
# of a documentation.

# Rule-based Matching Finding sequences of token bases on ther texts and linguistic annotations similiar to regular expressions

# Traininh Updating and improving a statistical model`s predictions 

# Serialization Saving objects to files or byte strings 


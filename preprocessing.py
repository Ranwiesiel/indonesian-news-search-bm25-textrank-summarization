import pandas as pd
from datetime import datetime
import regex as re
import string

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

# Function to clean text
def clean_text(text):
    if pd.isnull(text):
        return ""
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='replace')
    # Remove escape characters (\r, \n, \t, \\)
    text = re.sub(r'\\r|\\n|\\t|\\\\', ' ', str(text))
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove leading unwanted chars like ", -", "- ", ", "
    text = re.sub(r'^[,\-\s]+', '', text)
    # Strip leading/trailing whitespace again
    text = text.strip()
    return text

def convert_timestamp(ts):
    try:
        if pd.isnull(ts):
            return ""
        # Replace comma with dot (if any)
        ts_str = str(ts).replace(',', '.')
        # Convert to float
        ts_float = float(ts_str)
        # Convert from milliseconds to seconds
        ts_seconds = ts_float / 1000
        # Convert to datetime
        dt = datetime.fromtimestamp(ts_seconds)
        # Format string
        return dt.strftime('%Y-%m-%d')
        # return dt
    except Exception as e:
        return ""
        
def segment_sentences(text):
  return sent_tokenize(text)

# Apply lowercase to each sentence in the list
def lowercase_sentences(sentences):
        return [sentence.lower() for sentence in sentences]

def remove_punctuation(sentences):
    return ["".join([char for char in sentence if char not in string.punctuation]) for sentence in sentences]

factory = StopWordRemoverFactory()
stopword_remover = factory.create_stop_word_remover()

def remove_stopwords(sentences):
    return [stopword_remover.remove(sentence) for sentence in sentences]

factory = StemmerFactory()
stemmer = factory.create_stemmer()
def stemmer_(sentences):
    return [stemmer.stem(sentence) for sentence in sentences]

def join_sentences(sentences):
        return " ".join(sentences)

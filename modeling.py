from preprocessing import *
from schema import *
from whoosh.index import create_in

import os
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

import kagglehub
import pandas as pd

# Download latest version
# path = kagglehub.dataset_download("rizkia14/berita-indo")

# datasets = "datasets/tempo Jun19 May20.csv"
# df = pd.read_csv(path + "/tempo Jun19 May20.csv", delimiter=';', encoding='utf-8')

datasets = "datasets/tempo_with_summaries.csv"
df = pd.read_csv(datasets, delimiter=',', encoding='utf-8')

df.dropna(inplace=True)

# Preprocessing
df['content'] = df['content'].apply(clean_text)
df['title'] = df['title'].apply(clean_text)
df['datetime'] = df['datetime'].apply(convert_timestamp)

# Tokenisasi
df['content'] = df['content'].astype(str)
df['content_sentences'] = df['content'].apply(segment_sentences)

# Apply lowercase to each sentence in the list
df['content_sentences'] = df['content_sentences'].apply(lowercase_sentences)

# Remove punctuation
df['content_sentences'] = df['content_sentences'].apply(remove_punctuation)

# stemmer
df['content_sentences'] = df['content_sentences'].apply(stemmer_)

# Remove stopwords
df['content_sentences'] = df['content_sentences'].apply(remove_stopwords)

# Join sentences into a single string
df['content_sentences'] = df['content_sentences'].apply(join_sentences)

ix = create_in("indexdir", schema)
writer = ix.writer()

for i, row in df.iterrows():
    # Clean text
    content = row['content_sentences']
    # Add to index
    writer.add_document(
        path=str(i),
        title=row['title'],
        original_content=row['content'],
        content_processed=content,
        datetime=row['datetime'],
        tags=row['tags'],
        summarization=row['summary']
    )

writer.commit()


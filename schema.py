from whoosh.fields import *

schema = Schema(
    path=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    original_content=TEXT(stored=True),
    content_processed=TEXT(stored=False),
    tags=KEYWORD(stored=True),
    summarization=TEXT(stored=True),
    datetime=DATETIME(stored=True, sortable=True),
)

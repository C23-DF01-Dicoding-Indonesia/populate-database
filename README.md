# Populate Database

This repository contains the code for populating the [Pinecone](https://www.pinecone.io/) database with the Dicoding proprietary dataset.

The `create_search_index.py` script is used to create an index for semantic search on the Dicoding discussion forum and modules.

The `data/search.json` file contains the data that will be used to create the index and has the following format:

```json
{
    "document_id": "unique id of the document, a string",
    "title": "title of the document, a string",
    "content_display": "content of the document, a string comprising the title and content",
    "target_embedding": "embedding of the document with carlesoctav/multi-qa-en-id-mMiniLMv2-L6-H384, a list of floats"
}
```

The `create_auto_tag_index.py` script is used to create an index for auto-tagging on the Dicoding discussion forum.

The `data/auto_tag.json` file contains the data that will be used to create the index and has the following format:

```json
{
    "context": "content of the document, a string comprising the title and content",
    "tags": "tags of the document, a list of strings",
    "target_embedding": "embedding of the document with carlesoctav/multi-qa-en-id-mMiniLMv2-L6-H384, a list of floats"
}
```

If your data doesn't have a `target_embedding`, you can use the `embedding-endpoint` from another repository to obtain the embedding for your data.

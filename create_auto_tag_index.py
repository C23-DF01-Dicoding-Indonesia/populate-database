import os
import pinecone
import json 

# get api key from app.pinecone.io
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# find your environment next to the api key in pinecone console
PINECONE_ENV = os.environ.get('PINECONE_ENVIRONMENT')
VECTOR_LENGTH = 384

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

index_name = 'auto-tag-ml'

# only create index if it doesn't exist
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=VECTOR_LENGTH,
        metric="dotproduct"
    )

# now connect to the index
index = pinecone.GRPCIndex(index_name)


with open('data/auto_tag.json') as f:
    cache = json.load(f)


from tqdm.auto import tqdm

for i, data in tqdm(enumerate(cache)):
    # find end of batch
    # create IDs batch
    ids = i
    # create metadata batch
    metadatas = {
            'tags': data['tags'],
        }
    
    # create embeddings
    xc = data["target_embedding"]
    # create records list for upsert
    records = [
        {
            'id': str(ids),
            "values": xc,
            "metadata": metadatas,
        }
    ]
    # upsert to Pinecone
    index.upsert(vectors=records)

# check number of records in the index
index.describe_index_stats()

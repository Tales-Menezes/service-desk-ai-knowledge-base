# Cognitive Search Index Design

## Index Name
knowledge-base-index

## Fields

- id (Edm.String, key)
- content (Edm.String, searchable)
- client (Edm.String, filterable)
- category (Edm.String, filterable)
- title (Edm.String, searchable)
- source_document (Edm.String)
- chunk_id (Edm.Int32)
- embedding (Collection(Edm.Single))

## Chunking Strategy
Documents are split into chunks of approximately 700 tokens
with an overlap of 100 tokens to preserve context across sections.

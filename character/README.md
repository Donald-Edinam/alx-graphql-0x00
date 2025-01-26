# ALX GraphQL Project: Character Information Retrieval

## Objective
Learners will write a GraphQL query to retrieve a specific character’s information using their ID.

## Endpoint
Use the following endpoint to execute your queries.

## Instructions
1. Write a GraphQL query using the `character(id: ID!)` field to fetch the details of a character.
2. Use the following IDs: 1, 2, 3, 4.
3. Include the following fields in your query:
    - id
    - name
    - status
    - species
    - type
    - gender

## Repository Structure
- **GitHub repository:** alx-graphql-0x00
- **Directory:** character
- **Files:**
  - `README.md`
  - `character-id-1.graphql`
  - `character-id-1-output.json`
  - `character-id-2.graphql`
  - `character-id-2-output.json`
  - `character-id-3.graphql`
  - `character-id-3-output.json`
  - `character-id-4.graphql`
  - `character-id-4-output.json`

## Example Query
```graphql
query {
  character(id: 1) {
     id
     name
     status
     species
     type
     gender
  }
}
```

## Example Output
```json
{
  "data": {
     "character": {
        "id": "1",
        "name": "Rick Sanchez",
        "status": "Alive",
        "species": "Human",
        "type": "",
        "gender": "Male"
     }
  }
}
```
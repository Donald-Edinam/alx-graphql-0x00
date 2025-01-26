# Loop through each character ID
for character_id in character_ids:
    # Define the GraphQL query
    query = f"""
    query GetCharacterById {{
      character(id: {character_id}) {{
        id
        name
        status
        species
        type
        gender
      }}
    }}
    """

    # Save the query to a .graphql file
    query_file = f"character-id-{character_id}.graphql"
    with open(query_file, 'w') as f:
        f.write(query)

    print(f"Query saved to {query_file}")
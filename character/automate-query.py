import requests
import json

# Define the GraphQL endpoint
url = "https://rickandmortyapi.com/graphql"

# Define the list of character IDs to query
character_ids = [1, 2, 3, 4]

# Loop through each character ID
for character_id in character_ids:
    # Define the GraphQL query
    query = f"""
    {{
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

    # Send the request to the GraphQL endpoint
    response = requests.post(url, json={'query': query})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Define the output filename
        output_file = f"character-id-{character_id}-output.json"

        # Save the response to a JSON file
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Output saved to {output_file}")
    else:
        print(f"Failed to fetch data for character ID {character_id}. Status code: {response.status_code}")

# Loop through each character ID to create .graphql files
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
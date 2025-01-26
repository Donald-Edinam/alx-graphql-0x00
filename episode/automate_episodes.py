import requests
import json

# Define the GraphQL endpoint
url = "https://rickandmortyapi.com/graphql"

# Define the list of episode IDs to query
episode_ids = [1, 2, 3, 4]

# Loop through each episode ID
for episode_id in episode_ids:
    # Define the GraphQL query
    query = f"""
    {{
      episode(id: {episode_id}) {{
        id
        name
        air_date
        episode
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
        output_file = f"episode-id-{episode_id}-output.json"

        # Save the response to a JSON file
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Output saved to {output_file}")
    else:
        print(f"Failed to fetch data for episode ID {episode_id}. Status code: {response.status_code}")

# Loop through each episode ID to create .graphql files
for episode_id in episode_ids:
    # Define the GraphQL query
    query = f"""
    query GetEpisodeById {{
      episode(id: {episode_id}) {{
        id
        name
        air_date
        episode
      }}
    }}
    """

    # Save the query to a .graphql file
    query_file = f"episode-id-{episode_id}.graphql"
    with open(query_file, 'w') as f:
        f.write(query)

    print(f"Query saved to {query_file}")
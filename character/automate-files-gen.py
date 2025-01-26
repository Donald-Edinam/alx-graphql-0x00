import requests
import json

# Define the GraphQL endpoint
url = "https://rickandmortyapi.com/graphql"

# Define the list of pages to query
pages = [1, 2, 3, 4]

# Loop through each page
for page in pages:
    # Define the GraphQL query
    query = f"""
    {{
      characters(page: {page}) {{
        results {{
          id
          name
          status
          image
        }}
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
        output_file = f"characters-page-{page}-output.json"

        # Save the response to a JSON file
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Output saved to {output_file}")
    else:
        print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")

# Loop through each page to create .graphql files
for page in pages:
    # Define the GraphQL query
    query = f"""
    query GetCharactersByPage {{
      characters(page: {page}) {{
        results {{
          id
          name
          status
          image
        }}
      }}
    }}
    """

    # Save the query to a .graphql file
    query_file = f"characters-page-{page}.graphql"
    with open(query_file, 'w') as f:
        f.write(query)

    print(f"Query saved to {query_file}")
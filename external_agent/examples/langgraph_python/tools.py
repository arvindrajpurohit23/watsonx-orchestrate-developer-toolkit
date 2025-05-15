from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def web_search_duckduckgo(search_phrase: str):
    """Search the web using duckduckgo."""
    search = DuckDuckGoSearchResults()
    results = search.run(search_phrase) 
    return results

@tool
def news_search_duckduckgo(search_phrase: str):
    """Search news using duckduckgo."""
    search = DuckDuckGoSearchResults(backend="news")
    results = search.run(search_phrase) 
    return results

@tool
#def langflow(search_phrase: str) -> dict:
def langflow(search_phrase: str):
    """Search recipes using langflow ."""
    url = f"http://127.0.0.1:7862/api/v1/run/c1a75a15-dcd4-4478-9c1b-d43195ab7577"    # api url of langflow project
    # Request payload configuration
    payload = {
        "input_value": search_phrase ,  # The input value to be processed by the flow
        "output_type": "chat",  # Specifies the expected output format
        "input_type": "chat"  # Specifies the input format
    }
    # Request headers
    headers = {
        "Content-Type": "application/json",
    }

    #print(search_phrase, "This is the INPUT for Langflow: ")

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        # Print response
        #print(response.text, "This is the OUTPUT of Langflow: ")
    
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")
    
    return response

tool_choices = {
    "web_search_duckduckgo": web_search_duckduckgo,
    "news_search_duckduckgo": news_search_duckduckgo,
    "langflow": langflow,
}


from promptflow import tool
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(search_keywords: str):
    endpoint    = "https://13teamlogdata.search.windows.net"
    credential  = AzureKeyCredential("")
    index_name  = "leejuhae-index"
    api_version = "2024-03-01-preview"

    search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential, api_version=api_version)

    results = search_client.search(  
        search_text=search_keywords
    )

    result_data = []

    for result in results:  
        # if result['@search.score'] > 0.5:
        result_data.append({"meaning": result['meaning'], "flow": result['flow']})
        # print(f"Title: {result['title']}")  
        # print(f"Score: {result['@search.score']}")  
        # print(f"Text:  {result['text']}")  
        # print(f"id:    {result['id']}\n")  

    print(result_data)

    return result_data

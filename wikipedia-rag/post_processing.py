
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(search_result: list):
    # print(search_result[0]['original_entity']['text'])
    # 검색된 여러개의 문서에서 original_entity의 text 부분만 배열로 만들어서 반환

    result_data = []

    for result in search_result:  
        # if result['@search.score'] > 0.5:
        result_answer = result['original_entity']
        result_data.append({"meaning": result_answer['meaning'], "flow": result_answer['flow']})
        # print(f"Title: {result['title']}")  
        # print(f"Score: {result['@search.score']}")  
        # print(f"Text:  {result['text']}")  
        # print(f"id:    {result['id']}\n")  

    print(result_data)

    return result_data

from promptflow import tool
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(search_result: list):
    # print(search_result[0]['original_entity']['text'])
    # 검색된 여러개의 문서에서 original_entity의 text 부분만 배열로 만들어서 반환

    result_data = []

    for result in search_result:  
        
        result_answer = result['original_entity']
        print(result_answer['@search.score'])
        if result_answer['@search.score'] > 0.85:
            result_data.append({"meaning": result_answer['meaning'], "flow": result_answer['flow']})

    print(result_data)

    return result_data
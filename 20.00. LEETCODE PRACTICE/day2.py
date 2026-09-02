from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

def flatten_dictionary(dictionary: DeepNestedDict) -> Dict[str, str]:
    pass # your code goes here
  
# debug your code below
dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary(dict_input))
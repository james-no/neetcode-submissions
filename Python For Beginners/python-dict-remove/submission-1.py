from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for k in keys: # for key(k) in list(keys)
        if k in my_dict: # if key(k) in dictionary(my_dict)
            del my_dict[k] # delete the key from dictionary
    return my_dict

# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))

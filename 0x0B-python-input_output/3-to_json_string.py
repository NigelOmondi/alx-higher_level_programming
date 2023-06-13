#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)""" 


def to_json_string(my_obj):
    """
    Convert an object (string) to its JSON representation.

    Args:
        my_obj: The object (string) to be converted.

    Returns:
        str: The JSON representation of the object.
    """
    if isinstance(my_obj, str):
        # Replace special characters to ensure valid JSON representation
        my_obj = my_obj.replace('"', r'\"')
        my_obj = my_obj.replace('\\', r'\\')
        return '"' + my_obj + '"'
    elif isinstance(my_obj, (int, float, bool)):
        return str(my_obj)
    elif isinstance(my_obj, (list, tuple)):
        elements = [to_json_string(item) for item in my_obj]
        return "[" + ", ".join(elements) + "]"
    elif isinstance(my_obj, dict):
        pairs = [f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()]
        return "{" + ", ".join(pairs) + "}"
    else:
        raise TypeError(f"{my_obj} is not JSON serializable")

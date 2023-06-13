#!/usr/bin/python3
"""A function that returns an object (Python data structure)
   represented by a JSON string
"""


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    def decode_string(s):
        # Remove outer quotes and unescape special characters
        return s[1:-1].replace(r'\"', '"').replace(r'\\', '\\')

    def decode_value(value):
        if value == "true":
            return True
        elif value == "false":
            return False
        elif value == "null":
            return None
        elif value.startswith('"') and value.endswith('"'):
            return decode_string(value)
        elif value.isdigit():
            return int(value)
        elif "." in value:
            return float(value)
        else:
            raise ValueError("Invalid value: {}".format(value))

    def decode_array(array):
        return [decode_value(item.strip()) for item in array[1:-1].split(",")]

    def decode_object(obj):
        result = {}
        key = None
        value = ""
        is_string = False

        for char in obj:
            if char == '"':
                if is_string:
                    result[key] = decode_value(value)
                    is_string = False
                else:
                    key = value
                    is_string = True
                value = ""
            elif char == ":":
                pass
            elif char == ",":
                if is_string:
                    raise ValueError("Expecting property name enclosed in double quotes")
                result[key] = decode_value(value)
                value = ""
            else:
                value += char

        return result

    my_str = my_str.strip()

    if my_str.startswith("[") and my_str.endswith("]"):
        return decode_array(my_str)
    elif my_str.startswith("{") and my_str.endswith("}"):
        return decode_object(my_str)
    else:
        raise ValueError("Invalid JSON string")

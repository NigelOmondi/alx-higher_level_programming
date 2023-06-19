#!/usr/bin/python3
"""Define class base"""


import json


class Base:
    """
    Base class for other classes in the project.

    Attributes:
        __nb_objects (int): Counter for the number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The identifier for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): The list of objects to save to a file.
        """
        filename = cls.__name__ + ".json"
        obj_dicts = []
        if list_objs is not None:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string representation.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: The attribute-value pairs for the instance.

        Returns:
            object: An instance of the class with the attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance with minimum required attributes
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy instance with minimum required attributes
        else:
            dummy = None
        dummy.update(**dictionary)  # Use update method to set the attributes
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    obj_data = obj.to_csv()
                    writer.writerow(obj_data)



    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                obj_list = []
                for obj_data in reader:
                    obj = cls.create_from_csv(obj_data)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

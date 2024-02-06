#!/usr/bin/python3
import json


def new(obj):
    """Set in __objects obj with key <obj_class_name>.id"""
    FileStorage.__object = obj


class FileStorage:
    """Represent an abstracted storage engine.

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
        """
    __file_path = "data.json"
    __object = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__object

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        my_dictionary = {}
        if FileStorage.__object:
            for k, v in FileStorage.__object.items():
                my_dictionary[k] = v
                json_string = json.dumps(my_dictionary)
                with open(FileStorage.__file_path, "w") as in_file:
                    in_file.write(json_string)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as out_file:
                my_dictionary = json.load(out_file)
            for k, v in my_dictionary.items():
                FileStorage.__object[k] = v
        except FileNotFoundError:
            return

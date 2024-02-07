#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


class FileStorage:
    """Represent an abstracted storage engine.

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
        """
    __file_path = "data.json"
    __object = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """Return the dictionary __objects."""
        return self.__object

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = f"{str(obj.__class__.__name__)}.{str(obj.id)}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        my_dictionary = {}
        if self.__object:
            for k, v in self.__object.items():
                my_dictionary[k] = v
                json_string = json.dumps(my_dictionary)
                with open(self.__file_path, "w") as in_file:
                    in_file.write(json_string)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as out_file:
                my_dictionary = json.load(out_file)
            for k, v in my_dictionary.items():
                name = v['__class__']
                self.__object[k] = self.class_dict[name](**v)
        except FileNotFoundError:
            return

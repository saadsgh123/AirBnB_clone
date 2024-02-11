#!/usr/bin/python3
"""
Implementation
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class
    """
    prompt = "(hbnb)"
    classes = {"User", "BaseModel", "State",
               "City", "Amenity", "Place", "Review"}

    def do_EOF(self, line):
        """EOF signal to exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit"""
        return True

    def emptyline(self):
        """Prints empty line when no argument"""
        pass

    def do_create(self, line):
        """Creates new instance specified by user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints based on name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroys instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of instances"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")



#!/usr/bin/python3
"""Command interpreter for the AirBnB clone."""

import cmd
import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit on EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        
        args = shlex.split(arg)
        class_name = args[0]
        
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            }
        
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        
        instance = classes[class_name]()
        
        for item in args[1:]:
            if "=" not in item:
                continue
            
            key, value = item.split("=", 1)
            
            if value.startswith('"') and value.endswith('"'):
                
                value = value[1:-1].replace("_", " ")
            else:
                try:
                    if "." in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                        pass
                    
            if hasattr(instance, key):
                        setattr(instance, key, value)
            else:
                        setattr(instance, key, value)
                        
                        instance.save()
                        print(instance.id)

    def do_show(self, arg):
        """Show an instance based on class name and id."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)

        if obj is None:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances or all instances of a class."""
        args = shlex.split(arg)

        if args and args[0] not in [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            print([
                str(obj) for key, obj in objects.items()
                if key.startswith(args[0] + ".")
            ])

    def do_update(self, arg):
        """Update an instance with a new attribute value."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
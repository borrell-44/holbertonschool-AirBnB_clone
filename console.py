#!/usr/bin/python3

""" entry point of the command interpreter """

import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    """ command interpreter """

    def emptyline(self):
        """ does nothing when emptyline is given """
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n """
        exit()

    def do_EOF(self, line):
        """ quits the program """
        return True

    def do_create(self, args):
        """ creates a new instance of BaseModel """
        if not args:
            print("** class name missing **")
        else:
            arg = list(args.split(" "))
            try:
                obj = eval(arg[0])()
                obj.save()
                print(obj.id)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")

    def do_show(self, args):
        """ prints a string representation of an instace """
        if not args:
            print("** class name missing **")
        else:
            arg = list(args.split(" "))
            try:
                cls = eval(arg[0])()
                con = False
                file = models.storage.all()
                for key in file.keys():
                    obj = file[key]
                    dic = obj.to_dict()
                    if dic["id"] == arg[1] and arg[0] == dic["__class__"]:
                        print(obj)
                        con = True
                if con is False:
                    print("** no instance found **")
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, args):
        """ deletes an instance """
        if not args:
            print("** class name missing **")
        else:
            arg = list(args.split(" "))
            try:
                cls = eval(arg[0])()
                file = models.storage.all()
                con = False
                for key in file.keys():
                    dic = file[key].to_dict()
                    if dic["id"] == arg[1] and arg[0] == dic["__class__"]:
                        del file[key]
                        con = True
                        break
                if con is True:
                    dic = {}
                    for key in file.keys():
                        dic[key] = file[key].to_dict()
                    with open("file.json", "w") as f:
                        f.write(json.dumps(dic))
                if con is False:
                    print("** no instance found **")
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, args):
        """ prints all strings representation of all instances """
        file = models.storage.all()
        if not args:
            for key in file.keys():
                obj = file[key]
                print(obj)
        else:
            try:
                cls = eval(args)()
                for key in file.keys():
                    obj = file[key]
                    dic = obj.to_dict()
                    if dic["__class__"] == args:
                        print(obj)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")

    def do_update(self, args):
        """ update an instace based on the class name and id """
        if not args:
            print("** class name missing **")
            return
        arg = list(args.split(" "))
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return

        try:
            obj = eval(arg[0])()
        except (NameError, SyntaxError):
            print("** class doesn't exist **")
            return

        file = models.storage.all()
        con = True
        for key in file.keys():
            obj = file[key]
            dic = obj.to_dict()
            if arg[1] != dic["id"]:
                con = False
            else:
                break

        if con is False:
            print("** no instance found **")
            return
        setattr(obj, arg[2], arg[3].replace("\"", ""))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

""" entry point of the command interpreter """

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    """ command interpreter """

    def emptyline(self):
        """ does nothing when emptyline is given """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n """
        exit()

    def do_EOF(self, line):
        """ quits the program """
        return True

    def do_create(self, arg):
        """ creates a new instance of BaseModel """
        if not arg:
            print ("** class name missing **")
        elif arg != "BaseModel":
            print ("** class doesn't exist **")
        else:
            base = BaseModel()
            print (base.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

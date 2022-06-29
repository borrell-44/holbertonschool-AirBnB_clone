#!/usr/bin/python3

""" entry point of the command interpreter """

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

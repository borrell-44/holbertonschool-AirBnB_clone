# AirBnB - The console

This project is about creating a console for a future web application project. The console will be able to update, create, and save instances into a file using the JSON syntax for storing the data for the web site.

## Description

### You can start the project by first executing the console file:

vagrant@ubuntu-focal:~/holbertonschool-AirBnB_clone$ ./console.py

### You can use it by using any of these commands:

* create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

* show: Prints the string representation of an instance based on the class name and id.

* destroy: Deletes an instance based on the class name and id (save the change into the JSON file).

* all: Prints all string representation of all instances based or not on the class name.

* update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## Example

(hbnb) create User 

7ad92afc-c549-4b15-b97b-91071ffa3866 

(hbnb) update User 7ad92afc-c549-4b15-b97b-91071ffa3866 first_name "Juan" 

(hbnb) show User 7ad92afc-c549-4b15-b97b-91071ffa3866 

[User] (7ad92afc-c549-4b15-b97b-91071ffa3866) {'id': '7ad92afc-c549-4b15-b97b-91071ffa3866', 'created_at': datetime.datetime(2022, 7, 3, 20, 28, 21, 944913), 'updated_at': datetime.datetime(2022, 7, 3, 20, 29, 4, 862400), 'first_name': 'Juan'} 

(hbnb) destroy User 7ad92afc-c549-4b15-b97b-91071ffa3866 

(hbnb) show User 7ad92afc-c549-4b15-b97b-91071ffa3866 

** no instance found ** 

(hbnb) 


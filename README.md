# plain-database.py
A simple program that gives access to users and that allows you to see who entered and at what time they entered, it is necessary to have a previous list of users who are given access


README for User Authentication Code
This Python code is a simple user authentication program that reads a CSV file named datos.csv to verify if the username provided by the user is in the list of valid users.

Dependencies
The code uses Python's standard library csv and the datetime class from the datetime library.

Usage
To use the code, make sure to have a CSV file named datos.csv with a list of valid usernames. The code will prompt the user to input a username. If the username entered is not in the list, the code will display "Access Denied" and prompt for the username to be entered again. If the username is in the list, the code will display "Access Granted".

In addition, the code adds a new empty user to the end of the list and replaces all usernames in the list with asterisks. It then writes the updated list to the datos.csv file. It also writes the username and the current time to a CSV file named Hora.csv.

Contribution
If you wish to contribute to the code, you can submit a pull request with your changes. Please make sure to follow coding best practices and document your code properly

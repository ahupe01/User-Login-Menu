# User-Login-Menu

In this project I wrote a program named “updatepass” that maintains a password file named “password”.  Each line of the password looks like this:
username:password       
with one username:password entry per line.

When invoked, “updatepass” first reads the password file “password” into a dictionary.  
If the “password” file doesn’t exist on disk then updatepass creates
an empty file named “password”. The program then presents the following menu:
1)	Add Username/Password
2)	Change Password
3)	Delete Username/Password
4)  Exit
If  the user selects “1” the program prompts for a new username and password combination and adds it to the already created dictionary,
provided that the username doesn't already exist in the dictionary
If the user selects “2” the program asks for the username/password combo that needs to be changed, and if the user enters both correctly
they are allowed to change the password– writing the changes to the dictionary
If the user selects “3” the program askw for the username/password combo that needs to be changed, and if the user enters both correctly 
they are allowed to delete the user information from the dictionary.
If the user selects "4", and they must to end the program, all contents of the dictionary are written to the password file.

The special feature of the program is that is an extension of what I learned in my 1st python project. It utilizes the salting/hashing 
and encoding of all the user information to keep a "secure" password file and not one that can be read in plain text

# BaD-DDE
Welcome to the Blockchain at Davis - dApp Development Environment (BaD-DDE)
# What It Is
BaD-DDE is a self-contained, Ubuntu-based environment with all the packages required to participate in Blockchain at Davis (BaD) workshop projects.

It was created to address the growing fustration around `node`, `npm`, and node-related package installation problems members were experiencing on independent computers.

# Dependencies
You will need the following already installed on your system:

* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)

# How To Use It
Create a directory and place the `Vagrantfile` in the desired directory

Then run the following command:
```
vagrant up
```
This will get the environment up and running. 

You will see a folder called `workbench` get created. This is a shared folder from the environment t your system and is where you can test and develop dApps. 

To enter the environment:
```
vagrant ssh
```
To exit the environment (while still in the environment):
```
logout
```

You can have multiple terminals pointing to the environment as long as you run `vagrant ssh` in the directory with the `Vagrantfile`. 

To shut down the environment, perform the following (outside the environment):
```
vagrant suspend
```

If you'd like to start fresh by deleting and reinstalling the environment, perform the following:
```
vagrant destroy
vagrant up
```
# Task

Please implement a program that synchronizes two folders: source and replica. The
program should maintain a full, identical copy of source folder at replica folder.
Synchronization must be one-way: after the synchronization content of the
replica folder should be modified to exactly match content of the source
folder;
Synchronization should be performed periodically.
File creation/copying/removal operations should be logged to a file and to the
console output;
Folder paths, synchronization interval and log file path should be provided
using the command line arguments;

# How to use

you can start from bash with command "python sync_dir.py a 2"
first argument "a" is name of source directory and number "2" are seconds how often data will by copy to directory "replica". 

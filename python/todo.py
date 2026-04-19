# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:57:48 2026

@author: matilda
"""

import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    #open(file name) read
    Input - a task to add to the list
    Return - nothing
    """
    #re-write list with new task and new line
    with open(TASK_FILE, 'a', encoding = 'utf-8') as file:
        file.write(task + '\n')
    
    

def list_tasks():

    with open(TASK_FILE,'r', encoding= 'utf-8') as file:
        tasks = file.readlines()
        counter = 1
        output_string = ''
        #formatting list
        for task in tasks :
            output_string = output_string + str(counter) + '. ' + task
            counter = counter + 1
    # remove whitespace       
    return output_string.strip()


def remove_task(index):
    
    with open(TASK_FILE, 'r', encoding = 'utf-8') as file:
        tasks = file.readlines()
        length = len(tasks)
       
        #delete task that matches the index that is given by user
        if index <= 0 or index > length:
            return tasks
        else:
            del tasks[index - 1]
       
            with open(TASK_FILE, 'w', encoding = 'utf-8') as file:
                file.writelines(tasks)
        
        return tasks

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main() 
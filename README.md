Task Prioritizer CLI

A simple yet effective command-line application that helps users prioritize tasks based on urgency and importance. This tool enables users to categorize tasks, rank them using a scoring system, and focus on high-priority items efficiently. It’s designed for individuals who need a structured way to manage their workload and improve productivity.

Features

Add Tasks – Input a task with a title, description, urgency, and importance.

View Tasks – List all recorded tasks with their priority rankings.

Search Tasks – Find a specific task by its title.

Filter Tasks – Display tasks based on priority level.

Delete Tasks – Remove completed or unnecessary tasks.

User-Friendly CLI – Interactive prompts with input validation and error handling.

Automatic Prioritization – Tasks are ranked based on a scoring system.

Installation

Prerequisites

Ensure you have Python 3 installed on your system.

Setup Instructions

Clone the repository:

git clone <repo-url>
cd task-prioritizer-cli

Install dependencies using Pipenv:

pipenv install

Activate the virtual environment:

pipenv shell

Set up the database:

python lib/db/seed.py

Usage

Run the CLI application with:

python lib/cli.py

Available Commands

Add a Task – Enter a title, description, urgency, and importance.

View All Tasks – List all tasks with their priority scores.

Find a Task by Title – Search for a task using keywords.

Filter Tasks by Priority – View only high, medium, or low-priority tasks.

Delete a Task – Remove a task from the list.

Exit – Close the application.

Task Prioritization System

The priority of a task is calculated using a scoring system based on urgency and importance:

Urgency (1-5 scale)

Importance (1-5 scale)

Priority Score = Urgency × Importance

Tasks with higher scores appear at the top of the list, ensuring that the most critical tasks get attention first.

Database Structure

The application uses a simple database with the following models:

Task – Stores the title, description, urgency, importance, and calculated priority score.

Future Enhancements

Edit tasks after creation.

Export tasks to a CSV or text file.

Implement due dates and reminders.

Introduce a graphical interface for better visualization.

This project is a great tool for organizing and managing your tasks effectively. 

Happy prioritizing! 

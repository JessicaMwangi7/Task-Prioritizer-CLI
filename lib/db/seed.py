from lib.models import session, Task

tasks = [
    Task("Finish CLI project", "Complete the Task Prioritizer CLI", 5, 5),
    Task("Prepare for meeting", "Get documents ready", 3, 4),
]

session.add_all(tasks)
session.commit()

print("Sample tasks added!")

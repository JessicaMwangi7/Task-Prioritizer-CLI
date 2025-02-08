from models import session, Task

# Check if database session is working
try:
    print("Testing database connection...")

    # Create a test task
    new_task = Task(title="Test Task", description="This is a test task", urgency=2, importance=3)
    session.add(new_task)
    session.commit()

    print("✔ Task added successfully!")

    # Fetch all tasks
    tasks = session.query(Task).all()
    print(f"✔ Retrieved {len(tasks)} tasks from the database.")

except Exception as e:
    print(f"Error: {e}")
finally:
    session.rollback()  # Rollback any changes in case of failure
    session.close()

session.query(Task).delete()
session.commit()
print("✔ All test tasks deleted.")

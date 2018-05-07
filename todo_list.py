class Task_manager:
    def __init__(self, user, priority, task):
        self.user = user
        self.priority = priority
        self.task = task

    def add_task(self, user, priority, task):
        task = input("Add task")
        user = input("Please assign a task: ")
        priority = input("Choose priority level 1-5: ")

    def priority(self, priority):
        if priority == 5:
            return "highest priority"
        elif priority == 4:
            return "high priority"
        elif priority == 3:
            return "medium priority"
        elif priority == 2:
            return "low priority"
        else:
            return "Complete when you can"

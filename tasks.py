class Task:
    def __init__(self, name: str, due_date: str, description: str) -> None:
        self.name = name
        self.due_date = due_date
        self.description = description
        self.completed = False # All tasks are marked not done

    def __str__(self) -> str:
        return self.name + ', ' + self.due_date + ', ' + self.description
    
class TaskManager:
    def __init__(self, name) -> None:
        self.name = name
        self.tasks = []
        self.finished_tasks = []
    
    def addTask(self):
        name = input("What is your task's name: ")
        date = input("When is it due: ")
        desc = input("Give a description of your task: ")
        self.tasks.append(Task(name, date, desc))

    def indexTask(self, task_name):
        for i, t in enumerate(self.tasks):
            if t.name==task_name: return i
        return -1

    def removeTask(self, task_to_del: Task):
        for task in self.tasks:
            if task.name==task_to_del:
                self.tasks.remove(task)
                return True
        return False
    
    def listTasks(self):
        print('\n' + f'{self.name}\'s Tasks to be Completed' + '----------------------------------------')
        for task in self.tasks:
            print(task.__str__())
        print('\n')

    def update(self):
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
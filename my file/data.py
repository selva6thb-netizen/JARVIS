class data:
    def __init__(self,topic,task,date):
        self.topic=topic
        self.task=task
        self.date=date
    def display(self): 
        print("Topic:",self.topic)
        print("Task:",self.task)
        print("Date:",self.date)
subject=data(input("enter topic: "),input("enter task: "),input("enter date: "))
subject.display()

file=open("data.txt","a")
file.write(f"Date: {subject.date}\nTopic: {subject.topic}\nTask: {subject.task}\n")
file.close()
    

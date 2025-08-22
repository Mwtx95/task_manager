from django.db import models


# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
    
class TaskList(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'tasklist'

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    due_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasklist_id = models.ForeignKey(TaskList, on_delete= models.CASCADE)
    class Meta:
        db_table = 'task'


class SubTask(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=25)
    task_id = models.ForeignKey(Task, on_delete= models.CASCADE)
    class Meta:
        db_table = 'subtask'

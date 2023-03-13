from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class WorkFlowData(models.Model):
    # id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200)
    start_time = models.DateTimeField('date published')
    end_time = models.DateTimeField('date published')
    completed = models.CharField(max_length=200)

    def set_task_name(self, task_name):
        self.task_name = task_name

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_completed(self, completed):
        self.completed = completed

    def __str__(self):
        return self.task_name
    
class ConfigurationForm(models.Model):
    github_link = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    data_location = models.CharField(max_length=200)
    python_script = models.CharField(max_length=200)
    output_file = models.CharField(max_length=200)
    previous_performance = models.FloatField()

    
    
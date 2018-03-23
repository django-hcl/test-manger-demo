from django.db import models


class QuestionType(models.Model):
    questiontype_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.questiontype_id


class Complexity(models.Model):
    complexity_id = models.AutoField(primary_key=True)
    complexity = models.CharField(max_length=60)

    def __str__(self):
        return self.complexity_id


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=60)
    complexity = models.ForeignKey(Complexity, on_delete=models.CASCADE)
    questiontype_id = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    section_id = models.IntegerField(null=True)
    created_by = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_id


class QuestionChoices(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    options = models.IntegerField(null=True)
    is_correctanwser = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_id



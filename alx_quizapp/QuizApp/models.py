from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=225)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizzes"


class Question(models.Model):
    text = models.CharField(max_length=225)
    quiz = models.ForeignKey(
        Quiz, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=225)
    quiz = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.text

from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
    text = models.TextField(null=False, blank=False)
    answer = models.BooleanField(default=False,
                                 verbose_name='Is the answer Yes?')  # this stores the proper answer to the quiz

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('%s - %s' % (self.text, self.answer))


class Quiz(models.Model):
    name = models.TextField(null=False, blank=False)  # name of the quiz
    description = models.TextField(null=False, blank=False)  # a quick description
    content = models.TextField(null=False, blank=False)  # the full content of the quiz

    questions = models.ManyToManyField(Question)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)





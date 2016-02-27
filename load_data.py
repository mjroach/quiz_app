import django

django.setup()

from quiz.models import Quiz, Question

print("loading quiz 1 data")
quiz1, quiz1_created = Quiz.objects.get_or_create(name='Animal Memory Quiz',
                                                  description='A list of animals',
                                                  content='Cat, Dog, Fish, Bird')

quiz1_question1, quiz1_question1_created = Question.objects.get_or_create(text='Does the text mention rat?',
                                                                          answer=False)
quiz1_question2, quiz1_question2_created = Question.objects.get_or_create(text='Does the text mention bird?',
                                                                          answer=True)
quiz1_question3, quiz1_question3_created = Question.objects.get_or_create(text='Does the text mention monkey?',
                                                                          answer=False)

quiz1.questions.add(quiz1_question1)
quiz1.questions.add(quiz1_question2)
quiz1.questions.add(quiz1_question3)

quiz1.save()

print('loading quiz 2 data')
quiz2, created = Quiz.objects.get_or_create(name='Weather Memory Quiz',
                                            description='Does the text contain any mention about weather',
                                            content='Rain, Snow, Hail')

quiz2_question1, quiz2_question1_created = Question.objects.get_or_create(text='Does the text mention Hurricane?',
                                                                          answer=False)
quiz2_question2, quiz2_question2_created = Question.objects.get_or_create(text='Does the text mention Snow?',
                                                                          answer=True)
quiz2_question3, quiz2_question3_created = Question.objects.get_or_create(text='Does the text mention Rain?',
                                                                          answer=True)
quiz2_question4, quiz2_question4_created = Question.objects.get_or_create(text='Does the text mention Hail?',
                                                                          answer=True)

quiz2.questions.add(quiz2_question1)
quiz2.questions.add(quiz2_question2)
quiz2.questions.add(quiz2_question3)
quiz2.questions.add(quiz2_question4)

quiz2.save()


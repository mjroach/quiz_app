from __future__ import division

from django.template import RequestContext

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.forms import formset_factory

from quiz.models import Quiz
from quiz.forms import QuestionForm


def bool_to_string(input):
    if input:
        return 'Yes'
    return 'No'


def home(request):
    '''
    a basic landing page that will show all available quizes
    :param request: django request input
    :return: a response with a template and a context
    '''
    context = {'all_quizes': Quiz.objects.all()}
    return render_to_response('quiz/home.html', context, context_instance=RequestContext(request))


def take_quiz(request, quiz_id=None):
    '''
    This is the main page that will render the quiz content and grade it
    :param request:  Django request input
    :param quiz_id: the quiz number input
    :return: a template with either the questions and content or a graded sheet
    '''
    cur_quiz = get_object_or_404(Quiz, pk=quiz_id)
    context = {'quiz': cur_quiz}
    form_questions = formset_factory(QuestionForm, extra=0)

    if request.method == 'POST':
        formset = form_questions(request.POST)
        if formset.is_valid():
            graded = []
            correct = 0
            # the form is valid, and has all required fields.
            for question in formset.forms:
                #time for grading
                db_answer = cur_quiz.questions.get(text=question.instance.text)

                if db_answer.answer == question.cleaned_data['boolfield']:
                    correct += 1

                graded.append({'text': db_answer.text,
                               'input_answer': bool_to_string(question.cleaned_data['boolfield']),
                               'correct_answer': bool_to_string(db_answer.answer),
                               'correct': db_answer.answer == question.cleaned_data['boolfield']})

            context['grade'] = correct / len(formset.forms) * 100  #calculates the grade
            context['graded'] = graded

        return render_to_response('quiz/take_quiz.html', context, context_instance=RequestContext(request))

    else:
        formset = form_questions(initial=cur_quiz.questions.all().order_by('?').values())
    context['questions'] = formset
    return render_to_response('quiz/take_quiz.html', context, context_instance=RequestContext(request))

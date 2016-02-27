from django.conf.urls import url

from quiz.views import home, take_quiz


urlpatterns = [
    url(r'^take_quiz/([0-9]+)/$', take_quiz),
    url(r'^$', home),
]

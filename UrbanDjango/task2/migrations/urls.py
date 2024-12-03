from django.urls import path
from UrbanDjango.task2.views import functional_view, ClassBasedView

urlpatterns = [
    path('functional/', functional_view, name='functional_view'),
    path('class/', ClassBasedView.as_view(), name='class_based_view'),
]

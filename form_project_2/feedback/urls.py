from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('<int:id_feedback>', views.UpdateFeedbackView.as_view(), name='update_feed'),
    path('detail/<int:pk>', views.DetailFeedBack.as_view(),name='feedback_details'),
    path('update/<int:pk>', views.FeedBackViewUpdate.as_view(),name='feedback_details'),
]
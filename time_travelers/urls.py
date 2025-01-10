from django.urls import path

from . import views

urlpatterns = [
    path('traveler/',views.timetraveler_list,name='traveler'),
    path('travelerform/',views.add_timetraveler_form, name='timetravelerform'),
    path('traveleredit/<int:id>/',views.traveler_edit,name='traveler_edit'),
    path('travelerdelete/<int:id>/', views.traveler_delete, name='traveler_delete'),
    path('travelerdetail/<int:id>/',views.traveler_detail,name='traveler_detail'),

]
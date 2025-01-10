from django.urls import path
from . import views

urlpatterns =[
    path('destinations/',views.timedestinations_list,name='destinations'),
    path('destinationsform/',views.add_timedestination_form, name='timedestinationform'),
    path('destinationsedit/<int:id>/',views.destination_edit,name='destination_edit'),
    path('destinationdelete/<int:id>/',views.destination_delete,name='destination_delete'),
    path('destinationdetail/<int:id>/',views.destination_detail,name='detail'),

]
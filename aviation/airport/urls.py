from . import views
from django.urls import path

app_name = 'airport'

urlpatterns = [
    path('',views.index,name='index'),
    path('airport/',views.airport,name='airport'),
    path('airport/<int:airport_id>/',views.detail,name='detail'),

    #add airport
    path('add',views.create_airport,name='create_airport'),

    #edit
    path('update/<int:airport_id>/',views.update_airport,name="update_airport"),

    #delete
    path('delete/<int:airport_id>/',views.delete_airport,name='delete_airport'),

    #asia
    path('airport/asia',views.asia,name='asia'),

    #africa
    path('airport/africa',views.africa,name='africa'),

    #oceania
    path('airport/oceania',views.oceania,name='oceania'),

    #south and central america
    path('airport/southamerica',views.southandcentralamerica,name='southamerica'),

    #antartica
    path('airport/antartica',views.antartica,name='antartica'),

    #north america
    path('airport/northamerica',views.northamerica,name='northamerica'),
]
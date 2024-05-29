from account import views
from django.urls import path

urlpatterns = [
    path('showAc/',views.show_account,name='account'),
    path('add/',views.add_credit_debit,name='add'),
    path('delete/<int:id>',views.delete_data,name='delete'),
    path('update/<int:id>',views.update_data,name='update'),
]

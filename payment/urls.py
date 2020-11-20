from django.urls import path, include
from . import views

payment_urlpatterns = ([
                           path('process/<int:id>/', views.payment_process, name='process'),
                           path('process/<int:id>/<str:flag>', views.payment_process, name='process'),
                           path('admin_process/<int:id>/', views.admin_payment_process,
                                name='admin_process'),
                           path('admin_done/<int:id>/', views.admin_payment_done, name='admin_done'),
                           path('done/<int:id>/', views.payment_done, name='done'),

                           path('cancel/', views.payment_canceled, name='cancel'),

                       ], 'payment')

urlpatterns = [

    path('', include(payment_urlpatterns))
]

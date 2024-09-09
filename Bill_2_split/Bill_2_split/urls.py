from django.urls import path
from Bill_2_split import views
from django.views.generic import TemplateView

app_name = 'Bill_2_pay'

placeholder_view = TemplateView.as_view(template_name='Bill_2_split/placeholder.html')

urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='IndexView'),

    path('user/',
         views.UserView.as_view(),
         name='UserView'),

    path('list_of_ledgers/<int:user_pk>/',
         views.ListOfLedgersView.as_view(),
         name='ListOfLedgersView'),

    path('list_of_ledgers/<int:user_pk>/add/',
         views.LedgerAdd.as_view(),
         name='LedgerAdd'),

    path('ledger_detail/<int:ledger_pk>/<int:user_pk>/',
         views.LedgerDetailView.as_view(),
         name='LedgerDetailView'),

    path('ledger_detail/<int:ledger_pk>/<int:user_pk>/add/',
         views.PaymentAddView.as_view(),
         name='PaymentAddView'),

    path('payment_detail/<int:payment_pk>/<int:ledger_pk>/<int:user_pk>/add/',
         views.RelationsAddView.as_view(),
         name='RelationsAddView'),

    path('payment_detail/<int:payment_pk>/<int:ledger_pk>/<int:user_pk>/',
         views.PaymentDetailView.as_view(),
         name='PaymentDetailView'),
]
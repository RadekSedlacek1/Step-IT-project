from django.urls import path
from Bill_2_split import views
from django.views.generic import TemplateView

app_name = 'Bill_2_pay'

'''
index / - login page

list_of_ledgers / user_id / user_slug/      - overview of ledgers + balance

ledger_detail / ledger_id / ledger_slug/    - overview of expenses + participants balance graph

payment_detail / payment_id / payment_slug/ - overview of relations in the payment
'''

placeholder_view = TemplateView.as_view(template_name='Bill_2_split/placeholder.html')

urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='IndexView'),

    path('list_of_ledgers/',
         # path('list_of_ledgers/<int:pk_user>/<slug:slug>',
         views.ListOfLedgersView.as_view(),
         name='ListOfLedgersView'),

    path('ledger_detail/',
         # path('ledger_detail/<int:pk_ledger>/<slug:slug>/',
         views.LedgerDetailView.as_view(),
         name='LedgerDetailView'),

    path('payment_detail/',
         # path('payment_detail/<int:pk_payment>/<slug:slug>/',
         views.PaymentDetailView.as_view(),
         name='PaymentDetailView'),
]
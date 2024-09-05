from django.shortcuts import render
from django.views import generic
from Bill_2_split.models import User, Ledger, Payment, Relation

class IndexView(generic.TemplateView):
    template_name = 'Bill_2_split/index.html'
    title = 'Welcome page'

    def get_users(self):
        return User.objects.all()

class ListOfLedgersView(generic.DetailView):
    model = Ledger
    template_name = 'Bill_2_split/list_of_ledgers.html'
    title = 'List of ledgers'

    def get_ledgers(self):
        return Ledger.objects.all()


class LedgerDetailView(generic.DetailView):
    model = Payment
    template_name = 'Bill_2_split/ledger_detail.html'
    title = 'Ledger detail'

    def get_payments(self):
        return Payment.objects.all()


class PaymentDetailView(generic.DetailView):
    model = Relation
    template_name = 'Bill_2_split/payment_detail.html'
    title = 'Payment detail'

    def get_relations(self):
        return Relation.objects.all()
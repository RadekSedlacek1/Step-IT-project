
from django.views import generic
from Bill_2_split.models import User, Ledger, Payment, Relation
from .functions import calculate_relation_costs
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

class IndexView(generic.TemplateView):
    template_name = 'Bill_2_split/index.html'
    title = 'Welcome page'

class UserView(generic.TemplateView):
    template_name = 'Bill_2_split/user.html'
    title = 'User page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ListOfLedgersView(generic.DetailView):
    model = User
    template_name = 'Bill_2_split/list_of_ledgers.html'
    title = 'List of ledgers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()  # získej uživatele podle pk
        context['ledgers'] = Ledger.objects.filter(payment__relation__user=user).distinct()  # vyfiltruj ledgery pro daného uživatele
        return context

class LedgerAdd(generic.CreateView):
    model = Ledger
    template_name = 'Bill_2_split/LedgerAdd.html'
    fields = ['name', 'desc']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_pk')  # Získání ID uživatele z URL
        context['user'] = User.objects.get(pk=user_id)  # Přidání uživatele do kontextu
        return context

    def form_valid(self, form):
        # Získej ID uživatele z URL
        user_id = self.kwargs.get('user_pk')
        user = User.objects.get(pk=user_id)

        #ulož prázdný ledger
        form.instance.user = user
        response = super().form_valid(form)
        ledger = form.instance

        # Uložení prázdného ledgeru
        form.instance.save()

        # Zkontroluj, zda již payment neexistuje
        payment, created = Payment.objects.get_or_create(
            ledger=ledger,
            cost=0,
            user=user,
            defaults={
                'name': 'ledger_created',
                'desc': 'dummy_payment',
                'entry_time': datetime.now(),
                'payment_time': datetime.now(),
            }
        )

        # Vytvoř dummy relation pro uživatele
        Relation.objects.get_or_create(
            user=user,
            payment=payment,
            defaults={
                'relation': 1
            }
        )

        return HttpResponseRedirect(reverse('Bill_2_split:ListOfLedgersView', kwargs={'pk': user.pk}))

class LedgerDetailView(generic.DetailView):
    model = Ledger
    template_name = 'Bill_2_split/ledger_detail.html'
    title = 'Ledger detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ledger = self.get_object()

        user_id = self.kwargs.get('user_pk')
        user = User.objects.get(pk=user_id)

        context['ledger'] = ledger
        context['user'] = user
        context['payments'] = Payment.objects.filter(ledger=ledger)

        return context


class PaymentDetailView(generic.DetailView):
    model = Payment
    template_name = 'Bill_2_split/payment_detail.html'
    title = 'Payment detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        payment = self.get_object()

        user_id = self.kwargs.get('user_pk')
        user = User.objects.get(pk=user_id)

        ledger_id = self.kwargs.get('ledger_pk')
        ledger = Ledger.objects.get(pk=ledger_id)

        relations = Relation.objects.filter(payment=payment)

        balance_change = calculate_relation_costs(relations, payment.cost)

        context['ledger'] = ledger
        context['user'] = user
        context['payment'] = payment
        context['relations'] = relations
        context['balance_change'] = balance_change

        return context
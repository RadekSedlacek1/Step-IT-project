from django.urls import path
from first_app.views import welcome_view, user_view, ledger_view, expense_view

urlpatterns = [
    path('', welcome_view, name='welcome_page'),                            # welcome page
    path('<int:user_id>/', user_view, name='user_page'),                    # users overview - ledgers and balance
    path('<int:user_id>/<int:ledger_id>', ledger_view, name='ledger_view')  # ledger overview - expenses, participants, balance

]
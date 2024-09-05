from django.contrib import admin
from Bill_2_split.models import User, Ledger, Payment, Relation

admin.site.register(User)
admin.site.register(Ledger)
admin.site.register(Payment)
admin.site.register(Relation)

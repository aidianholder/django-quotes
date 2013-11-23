from django.core.management.base import NoArgsCommand
from quotes.models import Quote
from random import randint

class Command(NoArgsCommand):



	def handle_noargs(self, **options):
		fresh_quotes = Quote.objects.filter(active=False)
		active_quote = Quote.objects.get(active=True)
		count = fresh_quotes.count()
		random_index = randint(0, count-1)
		new_quote = fresh_quotes[random_index]
		new_quote.active=True
		new_quote.save()
		active_quote.active=False
		active_quote.save()






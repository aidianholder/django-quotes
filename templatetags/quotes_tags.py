from django import template
from quotes.models import Quote
from random import randint

def grab_quote(parser, token):
	return QuoteNode()

class QuoteNode(template.Node):
	def render(self, context):
		context['active_quote'] = Quote.objects.get(active=True)
		return ''


#@register.inclusion_tag('quote.html')
#def get_quote():
#	active_quote = Quote.objects.get(active=True)
#	return {'quote':active_quote}

def random_quote(parser, token):
	return RandomQuoteNode()

class RandomQuoteNode(template.Node):
	def render(self, context):
		fresh_quotes = Quote.objects.filter(active=False)
		random_index = randint(0, fresh_quotes.count()-1)
		new_quote = fresh_quotes[random_index]
		if Quote.objects.filter(active=True).exists():
			active_quote = Quote.objects.get(active=True)
			active_quote.active=False
			active_quote.save()
		new_quote.active=True
		new_quote.save()
		context['active_quote'] = new_quote
		return ''

"""@register.simple_tag
def random_quote():
	fresh_quotes = Quote.objects.filter(active=False)
	active_quote = Quote.objects.get(active=True)
	random_index = randint(0, fresh_quotes.count()-1)
	new_quote = fresh_quotes[random_index]
	new_quote.save()
	active_quote.active=False
	active_quote.save()
	return 
	<blockquote class='pull-right'>
	<p>%s</p>
	<small>%s</small>
	</blockquote>
	 % (string(active_quote.quote), string(active_quote.author))
"""

register = template.Library()
register.tag('get_quote', grab_quote)
register.tag('get_random_quote', random_quote)

from django.template import Library
from . import my_filters

register = Library()

register.filter('prix_total', my_filters.total_price)
register.filter('nbr_articles', my_filters.total_articles)
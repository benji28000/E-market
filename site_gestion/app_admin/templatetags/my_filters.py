from django import template

register = template.Library()

@register.filter
def total_price(achats):
    total = 0
    for achat in achats:
        total += achat.quantité_achat * achat.article.prix
    return total


@register.filter
def total_articles(achats):
    total = 0
    for achat in achats:
        total += achat.quantité_achat
    return total

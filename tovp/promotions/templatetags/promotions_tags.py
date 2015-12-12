from django import template

from ananta.helpers import format_with_commas, format_for_india


register = template.Library()


@register.filter()
def promo_ballance(promotion, pledge, ballance):
    custom_format_functions = {
        'INR': format_for_india,
    }

    output = []
    currency = pledge.currency
    if currency in custom_format_functions:
        format_function = custom_format_functions[currency]
    else:
        format_function = format_with_commas

    missing_amount = promotion.get_amount(currency) - (
        ballance[currency]['pledged'] - ballance[currency]['used'])
    output.append('{amount} {currency} more required'.format(
        amount=format_function(missing_amount),
        currency=currency))
    return ' / '.join(output)

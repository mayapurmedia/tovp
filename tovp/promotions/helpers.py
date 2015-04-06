from jingo import register

from ananta.helpers import format_with_commas, format_for_india


@register.filter
def promo_ballance(promotion, ballance):
    format_functions = {
        'INR': format_for_india,
        'USD': format_with_commas,
        'GBP': format_with_commas,
        'EUR': format_with_commas,
    }
    output = []
    for currency in ballance:
        missing_amount = promotion.get_amount(currency) - (
            ballance[currency]['pledged'] - ballance[currency]['used'])
        output.append('{amount} {currency}'.format(
            amount=format_functions[currency](missing_amount),
            currency=currency))
    return ' / '.join(output)

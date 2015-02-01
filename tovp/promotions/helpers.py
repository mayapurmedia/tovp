from jingo import register

from ananta.helpers import format_with_commas, format_for_india


@register.filter
def promo_ballance(promotion, ballance):
    format_functions = {
        'INR': format_for_india,
        'USD': format_with_commas,
    }
    # ballance = {
    #     'INR': {'pledged': 0,
    #             'paid': 0,
    #             'used': 0},
    #     'USD': {'pledged': 0,
    #             'paid': 0,
    #             'used': 0},
    # }
    # currencies = {'INR': '₹', 'USD': '$'}
    output = []
    for currency in ballance:
        missing_amount = promotion.get_amount(currency) - (
            ballance[currency]['pledged'] - ballance[currency]['used'])
        output.append('{amount} {currency}'.format(
            amount=format_functions[currency](missing_amount),
            currency=currency))
    return ' / '.join(output)

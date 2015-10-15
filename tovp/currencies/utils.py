from django.conf import settings


def get_currency_choices():
    choices = []
    for currency in settings.ENABLED_CURRENCIES:
        choices.append((currency,
                        settings.ENABLED_CURRENCIES[currency]['symbol']))
    return choices


def get_currency_words(currency):
    if currency in settings.ENABLED_CURRENCIES:
        return settings.ENABLED_CURRENCIES[currency]['word']
    raise

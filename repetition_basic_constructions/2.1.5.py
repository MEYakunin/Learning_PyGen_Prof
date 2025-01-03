def hide_card(card_number):
    card_number = '*' * 12 + card_number.replace(' ', '')[-4:]
    return card_number

card = '1234567890123456'

print(hide_card(card))
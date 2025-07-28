def build_line_items(items, tax_rates=None):
    line_items = []
    for item in items:
        line_item = {
                'price_data': {
                    'currency': item.currency.lower(),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }
        if tax_rates:
            line_item['tax_rates'] = [tax_rates.id]
        line_items.append(line_item)
    return line_items

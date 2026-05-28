def process_item(items_t: tuple[int,int,str],items_s: set[bytes]):
    return items_t,items_s

def process_items(prices: dict[str,float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

    
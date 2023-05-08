from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.get_total_cost())  # 200000
    print(item2.get_total_cost())  # 100000

    # устанавливаем новый уровень цен
    Item.discount_level = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all_items)

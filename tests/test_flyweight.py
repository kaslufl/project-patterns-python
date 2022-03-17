from project_patterns.structural_patterns import ItemFamilies


def test_item_families():
    item_data = (('Wand of Orkus', 1, 'Wands'), ('Axe of Mortius', 2, 'Axes'), ('Deathbringer', 1, 'Wands'))
    item_family_objects = []
    for item in item_data:
        obj = ItemFamilies(item[0], item[1])
        obj.set_item_info(item[2])
        item_family_objects.append(obj)

    assert id(item_family_objects[0]) == id(item_family_objects[2])
    assert id(item_family_objects[1]) != id(item_family_objects[2])
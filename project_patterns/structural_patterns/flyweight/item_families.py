from project_patterns.structural_patterns.flyweight.item import Item


class ItemFamilies:
    "A dict to store item data"

    item_families = {}

    def  __new__(cls, name: str, item_family_id: int) -> None:
        try:
            id = cls.item_families[item_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.item_families[item_family_id] = id
        return id

    def set_item_info(self, item_info):
        item = Item()
        self.item_info = item.get_name(item_info)

    def get_item_info(self):
        return self.item_info

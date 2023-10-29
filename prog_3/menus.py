import utility
from typing import List, Dict
import copy

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, dish):
        self.menu_items.append(dish)

    def __str__(self):
        result = "Menu:" + "\n"
        for item in self.menu_items:
            result += item.get_description() + "\n"
        return result


def main():
    ...

if __name__ == "__main__":
    main()

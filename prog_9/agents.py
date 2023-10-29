from info import Info
from properties import Property
from typing import List
from clients import Agent_p, Client
import copy
import utility

class Agent(Agent_p):
    def __init__(self, name: str, contact_info: Info) -> None:
        self.name = name
        self.contact_info = contact_info
        self._property_listings = []
        self._clients = []

    @utility.type_checking(Property)
    def add_property_listing(self, property: Property) -> None:
        self._property_listings.append(property)

    @utility.container_type_checking(list, Client)
    def manage_clients(self, clients: List['Client']) -> None:
        self._clients.extend(clients)

    def __str__(self):
        return f"Agent: {self.name}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str) -> None:
        self._name = value

    @property
    def contact_info(self) -> 'Info':
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(Info)
    def contact_info(self, value: 'Info') -> None:
        self._contact_info = value

    @property
    def property_listings(self) -> List['Property']:
        return copy.deepcopy(self._property_listings)

    @property
    def clients(self) -> List['Client']:
        return copy.deepcopy(self._clients)

def main():
    ...

if __name__ == "__main__":
    main()

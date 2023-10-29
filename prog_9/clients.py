from properties import Property
from info import Info
import utility

class Agent_p:
    pass

class Client:
    def __init__(self, name: str, contact_info: Info):
        self.name = name
        self.contact_info = contact_info

    @utility.type_checking(Agent_p)
    def search_properties(self, agent: Agent_p) -> str:
        available_properties = agent.property_listings
        return utility.display_array(available_properties)

    @utility.type_checking(Agent_p, Property)
    def purchase_property(self, agent: Agent_p, property: Property) -> None:
        if property in agent.property_listings:
            print(f"{self.name} purchased the property at {property.address}")
            agent.property_listings.remove(property)
        else:
            print(f"{self.name} cannot purchase this property as it's not available.")

    def __str__(self) -> str:
        return f"Client: {self.name}"

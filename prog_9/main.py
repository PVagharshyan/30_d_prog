from properties import ResidentialProperty, CommercialProperty
from clients import Client
from agents import Agent
from info import Info

def main():
    residential_property = ResidentialProperty("123 Main St", 250000, "3 bedrooms, 2 bathrooms")
    commercial_property = CommercialProperty("456 Oak Ave", 500000, "Office space, parking")

    i = Info("095899903", "dadas", "paylak.vagharshyan@gamil.com")
    agent1 = Agent("Agent Smith", i)
    agent1.add_property_listing(residential_property)
    agent1.add_property_listing(commercial_property)

    i1 = Info("078885878", "dasda", "paylak.vagharshyan@gamil.com")
    i2 = Info("098484484", "dadas", "paylak.vagharshyan@gamil.com")
    client1 = Client("John Doe", i1)
    client2 = Client("Jane Smith", i2)

    agent1.manage_clients([client1, client2])

    print("Available Properties:")
    client1.search_properties(agent1)

    client2.purchase_property(agent1, residential_property)
    client1.purchase_property(agent1, commercial_property)

if __name__ == "__main__":
    ...
    main()

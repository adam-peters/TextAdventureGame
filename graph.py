import string
import networkx as nx


class Place:
    def __init__(self, name: string, description: string):
        self.name = name
        self.description = description


class Story:
    places = [
        Place("Road", "You are by a road"),
        Place("Forest", "You are in a forest"),
    ]

    def add_place(self, place):
        self.places.append(self, place)

    def __str__(self):
        for p in self.places:
            print(p.name + " | " + p.description)


# class Player:
#     def __init__(self, inventory: list, money: float):
#         self.money = money
#         self.inventory = inventory

campaign = Story()


# Create a new graph
G = nx.Graph()

G.add_node(campaign.places[0])
G.add_node(campaign.places[1])
G.add_edge(campaign.places[0], campaign.places[1])

# Add some nodes
# for i in range(len(campaign.places) + 1):
#     G.add_node(campaign.places[i - 1])
#     G.add
# Add some edges
G.add_edge(1, 2)


# Print the graph
print(G.nodes())
# Output: [1, 2, 3]

print(G.edges())
# Output: [(1, 2), (1, 3), (2, 3)]

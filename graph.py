# Author: Adam Peters
# Date Started

import string
import networkx as nx
import csv


# A Place Object that is used as node in the story graph
# currently stores the name and description
#----------------------------------------------------------------
# In the future it will store information about the items
# that can be found there and more
class Place:
    def __init__(self, name: string, description: string):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.description}"

# A Story object holds the graph for each seperate text adventure story
# where the nodes are Place Objects
class Story:
    # Graph to hold each place that you can travel to in the game
    places = nx.Graph()

    # Takes a normal (not UTF8), properly formatted (see top) file
    def load_csv(self):
        with open("./story.csv", 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                self.places.add_node(Place(row['Places'], row['Description']))

    def add_edges(self, edges):
        with open("./story.csv", 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                turd = row['Connections'].split(', ')
                for t in turd:
                    if t != '':
                        print("OK")
    # def print_list(list):
    #     for i in list:
    #         print(i)

    def __str__(self):
        for p in self.places:
            print(p.description)


campaign = Story()

current_node = 0

subject = "forest"

# populates the
campaign.load_csv()
for node in campaign.places.nodes:
    print(node)

# user_input = input("What would you like to do? ").lower()
#
# while user_input != "exit":
#     if user_input == "goto":
#         subject = int(input("Where would you like to go? "))
#         if G.has_edge(nodes[current_node], subject):
#             current_node = nodes.index(subject)
#             print(f"you are now at {current_node}, {nodes[current_node]}")
#         else:
#             print("that place does not exist")

# for node in G.nodes:
#     print(node)
#     user_input = input("Where would you like to go?")
#     if G.has_edge(node, ):
#         print(node)

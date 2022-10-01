from rdflib.extras.external_graph_libs import *
from rdflib import Graph
from pyvis.network import Network
import subprocess
import webbrowser

# to run jar file that produce the ontology in Turtle

subprocess.call(['java', '-jar', 'r2rml/target/r2rml.jar',  
                '--connectionURL=jdbc:mysql://127.0.0.1:3306/test?serverTimezone=UTC',
                '--user=root', '--password=100824*bigli@',
                '--mappingFile=mapping.ttl', '--outputFile=output.ttl',
                '--format=TURTLE' ])

##################################################################################

g = Graph()
result = g.parse("output.ttl", format="turtle")
G = rdflib_to_networkx_multidigraph(result)

net=Network(width="1300px",
            bgcolor="#ffffff",
            notebook=True,
            layout="hierarchical",
            heading="Ontology visualization")

net.from_nx(G)

net.show_buttons(filter_=['physics', 'layout'])
net.show("ontology.html")
webbrowser.open_new_tab('ontology.html') # -> it opens html on browser
# in "layout" to visualize the classes in the bottom part and the instances in the upper part of the schema, change:
#               sort Method -> directed
# in "physics" increase the
#                nodeDistance -> to make them more readable

##################################################################################

#it works but not nice graphic
import networkx as nx
import matplotlib.pyplot as plt

#g = Graph()
#result = g.parse("output.ttl", format="turtle")
#G = rdflib_to_networkx_multidigraph(result)

#pos= nx.spring_layout(G, scale=2)
#edges_lables = nx.get_edge_attributes(G, 'r')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_lables, label_pos=1)
#nx.draw(G, with_labels=True)

#plt.show()
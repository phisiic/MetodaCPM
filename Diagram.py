import os
from diagrams import Diagram, Edge
from diagrams.custom import Custom


def create_diagram(zdarzenia_poprzedzajace_lista, zdarzenia, sciezka_krytyczna, diagram_name):
    # Specify the file path and format directly in the Diagram constructor
    with Diagram(diagram_name, show=False, filename="CPM_diagram",
                 graph_attr={'size': '20,20', 'pad': '0.1'}, ) as diag:
        # Dictionary to store nodes
        nodes = {}

        # Create nodes
        for zdarzenie in zdarzenia:
            if zdarzenie.id != "0":
                node_name = f"Node {zdarzenie.id}"
                node_image_path = os.path.join("nodes", f"node_{zdarzenie.id}.png")
                node = Custom(node_name, node_image_path)
                nodes[zdarzenie.id] = node

        # Define relationships between nodes
        for zdarzenie in zdarzenia:
            if zdarzenie.id != "0":
                node = nodes[zdarzenie.id]
                predecessors = zdarzenia_poprzedzajace_lista.get(zdarzenie.id, [])
                for predecessor in predecessors:
                    predecessor_id = predecessor.id
                    predecessor_node = nodes[predecessor_id]

                    # Check if the edge belongs to the critical path
                    if zdarzenie in sciezka_krytyczna and predecessor in sciezka_krytyczna:
                        edge = Edge(color="red", style="bold", arrowhead="vee")
                        predecessor_node >> edge >> node
                    else:
                        predecessor_node >> node

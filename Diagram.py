from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.database import Mysql

def create_diagram():
    # Specify the file path and format directly in the Diagram constructor
    with Diagram("Custom Node Diagram", show=False, filename="./custom_node_diagram.png") as diag:
        with Cluster("Nodes"):
            # Add custom nodes with images
            node_1 = Custom("Node 1", "./nodes/node_1.png")
            node_2 = Custom("Node 2", "./nodes/node_2.png")
            node_3 = Custom("Node 3", "./nodes/node_3.png")

            # Define the relationships between nodes
            node_1 >> node_2
            node_1 >> node_3

            # Add regular nodes if needed
            db = Mysql("Database")
            node_2 >> db

# Call the function to create the diagram
create_diagram()

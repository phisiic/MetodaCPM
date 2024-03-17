import networkx as nx
import matplotlib.pyplot as plt

# Tworzenie grafu
G = nx.DiGraph()

# Dodawanie zadań
tasks = {
    "A": {"duration": 3},
    "B": {"duration": 4},
    "C": {"duration": 6},
    "D": {"duration": 7},
    "E": {"duration": 1},
    "F": {"duration": 2},
    "G": {"duration": 3},
    "H": {"duration": 4},
    "I": {"duration": 1},
    "J": {"duration": 2}
}

# Dodawanie krawędzi między zadaniami
G.add_edges_from([
    ("0", "A"),
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"),
    ("D", "G"), ("E", "H"), ("F", "H"), ("G", "I"), ("H", "I"), ("I", "J")
])

# Ustalanie pozycji węzłów
pos = nx.spring_layout(G)

# Przygotowanie etykiet węzłów (numery ID zadań)
node_labels = {node: i+1 for i, node in enumerate(G.nodes)}

# Przygotowanie etykiet krawędzi (nazwy zadań i ich czas trwania)
edge_labels = {edge: f"{edge[1]} ({tasks[edge[1]]['duration']})" for edge in G.edges}

# Rysowanie węzłów z etykietami numerów ID zadań
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="skyblue")
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight="bold")

# Rysowanie krawędzi z etykietami nazw zadań i ich czasami trwania
nx.draw_networkx_edges(G, pos, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.axis('off')  # Wyłączenie osi
plt.show()

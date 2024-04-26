import matplotlib.pyplot as plt
import os


class Czynnosc:
    def __init__(self, name, duration, before=None, after=None):
        if after is None:
            after = Zdarzenie()
        if before is None:
            before = Zdarzenie()
        self.name = name
        self.duration = duration
        self.before = before
        self.after = after

    def __str__(self):
        before_name = self.before.id
        after_name = self.after.id
        return f"Czynnosc: {self.name}, Duration: {self.duration}, Before: {before_name}, After: {after_name}"

class Zdarzenie:  # kolka
    def __init__(self, id, ti=0, tj=0):
        self.id = id
        self.ti = ti
        self.tj = tj
        self.float = self.tj - self.ti

    def __str__(self):
        return f"Zdarzenie ID: {self.id}, Ti: {self.ti}, Tj: {self.tj}, Float: {self.float}"

    def set_ti(self, ti):
        self.ti = ti

    def set_tj(self, tj):
        self.tj = tj

    def set_float(self):
        self.float = self.tj - self.ti

    def draw(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        filename = f"node_{self.id}.png"
        os.makedirs("nodes", exist_ok=True)
        filepath = os.path.join("nodes", filename)

        circle = plt.Circle((0.5, 0.5), 0.4, color='lightblue', ec='black')
        ax.add_artist(circle)

        # Draw X
        ax.plot([0.3, 0.7], [0.3, 0.7], color='black', linewidth=2)
        ax.plot([0.3, 0.7], [0.7, 0.3], color='black', linewidth=2)

        # Text labels
        ax.text(0.5, 0.70, f'Node ID: {self.id}', ha='center', va='center', size='large')
        ax.text(0.25, 0.5, f'Early Start: {self.ti}', ha='center', va='center', size='large')
        ax.text(0.75, 0.5, f'Late Start: {self.tj}', ha='center', va='center', size='large')
        ax.text(0.5, 0.30, f'Float: {self.float}', ha='center', va='center', size='large')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.savefig(filepath, bbox_inches='tight', pad_inches=-0.33)
        plt.close()


def clear_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file and delete it
    for file in files:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
from functions import combination
from PyQt5.QtWidgets import QWidget


class Graph(QWidget):
    def __init__(self, data, number, letter):
        super().__init__()
        chart = Canvas(self, data, number, letter)


class Canvas(FigureCanvas):

    def __init__(self, parent, data, number, letter):
        fig, self.ax = plt.subplots(figsize=(4, 3), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        # Graph different combinations
        comb = combination(data, number, letter)
        if len(comb) == 2:
            self.ax.plot(comb[0], comb[1])
            if number == 1:
                red_patch = mpatches.Patch(label='L1')
            elif number ==2:
                red_patch = mpatches.Patch(label='L2')
            else:
                red_patch = mpatches.Patch(label='L3')
            self.ax.legend(handles=[red_patch], prop={'size': 6})
        if len(comb) == 3:
            self.ax.plot(comb[0], comb[1])
            self.ax.plot(comb[0], comb[2])
            if number == 12:
                red_patch = mpatches.Patch(label='L1')
                red_patch2 = mpatches.Patch(label='L2', color='orange')
            elif number == 13:
                red_patch = mpatches.Patch(label='L1')
                red_patch2 = mpatches.Patch(label='L3', color='orange')
            else:
                red_patch = mpatches.Patch(label='L2')
                red_patch2 = mpatches.Patch(label='L3', color='orange')
            self.ax.legend(handles=[red_patch, red_patch2], prop={'size': 6})

        if len(comb) == 4:
            self.ax.plot(comb[0], comb[1])
            self.ax.plot(comb[0], comb[2])
            self.ax.plot(comb[0], comb[3])
            red_patch = mpatches.Patch(label='L1')
            red_patch2 = mpatches.Patch(label='L2', color='orange')
            red_patch3 = mpatches.Patch(label='L3', color='green')
            self.ax.legend(handles=[red_patch, red_patch2, red_patch3], prop={'size': 6})

        self.myLocator = mticker.MultipleLocator(5)
        self.ax.xaxis.set_major_locator(self.myLocator)

        if letter == "p":
            self.ax.set(title='Wirkleistung vs. Zeit')
            self.ax.set_ylabel('Watt (W)', fontsize=8)
        if letter == "q":
            self.ax.set(title='Blindleistung vs. Zeit')
            self.ax.set_ylabel('Voltampere (VA)', fontsize=8)
        if letter == "i":
            self.ax.set(title='Strom vs. Zeit')
            self.ax.set_ylabel('Ampere (A)', fontsize=8)
        if letter == "v":
            self.ax.set(title='Spannung vs. Zeit')
            self.ax.set_ylabel('Volt (V)', fontsize=8)

        self.ax.set_xlabel('x-label', fontsize=8)

        plt.xticks(fontsize=5)
        plt.yticks(fontsize=6)
        self.ax.grid()
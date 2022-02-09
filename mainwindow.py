from graphs import Graph
from PyQt5 import uic
import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout
from functions import extreme_outlier
qt_name, QtClass = uic.loadUiType('mainwindow.ui')


class MainWindow(qt_name, QtClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        "Set Outliers out"
        self.data = pd.read_csv('output.csv', parse_dates=True)
        self.data["time"] = self.data["time"].str.slice(start=7, stop=-13)
        self.data_outliers = self.data.copy()
        self.data_outliers["l2_p"] = extreme_outlier(self.data_outliers["l2_p"], 500)
        self.data_outliers["l2_i"] = extreme_outlier(self.data_outliers["l2_i"], 4)
        self.data_ram = self.data.copy()

        "Init Graph"
        self.graph = Graph(self.data_ram, 1, 'p')
        self.layout_graph = QVBoxLayout()
        self.parameter = "p"

        "Hide labels"
        self.x_axis.hide()
        self.y_axis.hide()

        "Outliers Button"
        self.checkBox_out.toggled.connect(self.switch_outliers)

        "Phase Buttons"
        self.checkBox_l1.toggled.connect(lambda: self.l1_checked(self.parameter))
        self.checkBox_l2.toggled.connect(lambda: self.l2_checked(self.parameter))
        self.checkBox_l3.toggled.connect(lambda: self.l3_checked(self.parameter))

        "Parameter Buttons"
        self.checkBox_p.toggled.connect(self.p_checked)
        self.checkBox_q.toggled.connect(self.q_checked)
        self.checkBox_i.toggled.connect(self.i_checked)
        self.checkBox_v.toggled.connect(self.v_checked)

        self.graphicsView.setLayout(self.layout_graph)
        #self.graphicsView.hide()

        "Boolean for outliers switch"
        self.bool = True

    "Changes database with outliers or without"
    def switch_outliers(self):
        if self.bool:
            self.data_ram = self.data_outliers.copy()
            self.bool = False
        else:
            self.data_ram = self.data.copy()
            self.bool = True
        self.tik(self.parameter)

    "Checks if p is checked"
    def p_checked(self):
        if self.checkBox_p.isChecked():
            self.checkBox_q.setChecked(False)
            self.checkBox_i.setChecked(False)
            self.checkBox_v.setChecked(False)
            self.parameter = "p"
            self.tik(self.parameter)
        elif not self.checkBox_p.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    def q_checked(self):
        if self.checkBox_q.isChecked():
            self.checkBox_p.setChecked(False)
            self.checkBox_i.setChecked(False)
            self.checkBox_v.setChecked(False)
            self.parameter = "q"
            self.tik(self.parameter)

        elif not self.checkBox_q.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    def i_checked(self):
        if self.checkBox_i.isChecked():
            self.checkBox_p.setChecked(False)
            self.checkBox_q.setChecked(False)
            self.checkBox_v.setChecked(False)
            self.parameter = "i"
            self.tik(self.parameter)

        elif not self.checkBox_i.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    "Checks if p,q,i,v are all checked"
    def all_checked(self):
        if not self.checkBox_p.isChecked() and not self.checkBox_q.isChecked():
            if not self.checkBox_v.isChecked() and not self.checkBox_i.isChecked():
                return True
            else:
                return False
        else:
            return False

    def v_checked(self):
        if self.checkBox_v.isChecked():
            self.checkBox_p.setChecked(False)
            self.checkBox_q.setChecked(False)
            self.checkBox_i.setChecked(False)
            self.parameter = "v"
            self.tik(self.parameter)

        elif not self.checkBox_v.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    "Ticks on all the checks"
    def tik(self, parameter):
        self.l1_checked(parameter)
        self.l2_checked(parameter)
        self.l3_checked(parameter)

    "If L1 gets checked"
    def l1_checked(self, parameter):

        if self.checkBox_l1.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 1, parameter)
            self.table(1, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()

        self.checked1_2(parameter)
        self.checked1_3(parameter)
        self.checked1_2_3(parameter)

        if not self.checkBox_l1.isChecked() and not self.checkBox_l2.isChecked() and not self.checkBox_l3.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()
        if not self.checkBox_l1.isChecked() and not self.checkBox_l2.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 3, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.table(3, parameter)
            self.x_axis.show()
        if not self.checkBox_l1.isChecked() and not self.checkBox_l3.isChecked() and self.checkBox_l2.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 2, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.table(2, parameter)
            self.x_axis.show()
        if not self.checkBox_l1.isChecked() and self.checkBox_l2.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 23, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.table(23, parameter)
            self.x_axis.show()

        if self.all_checked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    "If L2 gets checked"
    def l2_checked(self, parameter):
        if self.checkBox_l2.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 2, parameter)
            self.table(2, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        self.checked1_2(parameter)
        self.checked2_3(parameter)
        self.checked1_2_3(parameter)
        if not self.checkBox_l1.isChecked() and not self.checkBox_l2.isChecked() and not self.checkBox_l3.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()
        if not self.checkBox_l3.isChecked() and not self.checkBox_l2.isChecked() and self.checkBox_l1.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 1, parameter)
            self.table(1, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if not self.checkBox_l1.isChecked() and not self.checkBox_l2.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 3, parameter)
            self.table(3, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if not self.checkBox_l2.isChecked() and self.checkBox_l1.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 13, parameter)
            self.table(13, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if self.all_checked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    "If L3 gets checked"
    def l3_checked(self, parameter):
        if self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 3, parameter)
            self.table(3, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        self.checked1_3(parameter)
        self.checked2_3(parameter)
        self.checked1_2_3(parameter)
        if not self.checkBox_l1.isChecked() and not self.checkBox_l2.isChecked() and not self.checkBox_l3.isChecked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()
        if not self.checkBox_l3.isChecked() and not self.checkBox_l2.isChecked() and self.checkBox_l1.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 1, parameter)
            self.table(1, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if not self.checkBox_l3.isChecked() and self.checkBox_l1.isChecked() and self.checkBox_l2.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 12, parameter)
            self.table(12, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if not self.checkBox_l3.isChecked() and not self.checkBox_l1.isChecked() and self.checkBox_l2.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 2, parameter)
            self.table(2, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()
        if self.all_checked():
            self.graph.close()
            self.hide_labels()
            self.x_axis.hide()

    def checked1_2(self, parameter):
        if self.checkBox_l1.isChecked() and self.checkBox_l2.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 12, parameter)
            self.table(12, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()

    def checked1_3(self, parameter):
        if self.checkBox_l1.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 13, parameter)
            self.table(13, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()

    def checked2_3(self, parameter):
        if self.checkBox_l2.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 23, parameter)
            self.table(23, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()

    def checked1_2_3(self, parameter):
        if self.checkBox_l1.isChecked() and self.checkBox_l2.isChecked() and self.checkBox_l3.isChecked():
            self.graph.close()
            self.graph = Graph(self.data_ram, 123, parameter)
            self.table(123, parameter)
            self.layout_graph.addWidget(self.graph)
            self.graph.show()
            self.x_axis.show()

    "Hides all labels from the table"
    def hide_labels(self):
        self.min_l1.hide()
        self.min_l2.hide()
        self.min_l3.hide()
        self.max_l1.hide()
        self.max_l2.hide()
        self.max_l3.hide()
        self.med_l1.hide()
        self.med_l2.hide()
        self.med_l3.hide()
        self.avg_l1.hide()
        self.avg_l2.hide()
        self.avg_l3.hide()

    "Helper functions for table"
    def l1_functions(self, x):
        self.min_l1.setText(str(self.data_ram[x].min()))
        self.min_l1.show()
        self.max_l1.setText(str(self.data_ram[x].max()))
        self.max_l1.show()
        self.med_l1.setText(str(round(self.data_ram[x].median(), 3)))
        self.med_l1.show()
        self.avg_l1.setText(str(round(self.data_ram[x].mean(), 3)))
        self.avg_l1.show()

    def l2_functions(self, x):
        self.min_l2.setText(str(self.data_ram[x].min()))
        self.min_l2.show()
        self.max_l2.setText(str(self.data_ram[x].max()))
        self.max_l2.show()
        self.med_l2.setText(str(round(self.data_ram[x].median(), 3)))
        self.med_l2.show()
        self.avg_l2.setText(str(round(self.data_ram[x].mean(), 3)))
        self.avg_l2.show()

    def l3_functions(self, x):
        self.min_l3.setText(str(self.data_ram[x].min()))
        self.min_l3.show()
        self.max_l3.setText(str(self.data_ram[x].max()))
        self.max_l3.show()
        self.med_l3.setText(str(round(self.data_ram[x].median(), 3)))
        self.med_l3.show()
        self.avg_l3.setText(str(round(self.data_ram[x].mean(), 3)))
        self.avg_l3.show()

    "Sets combinations of min, max, avg, med values"
    def table(self, num, param):
        self.hide_labels()
        if param == "p":
            if num == 1:
                self.l1_functions("l1_p")
            if num == 2:
                self.l2_functions("l2_p")
            if num == 3:
                self.l3_functions("l3_p")
            if num == 12:
                self.l1_functions("l1_p")
                self.l2_functions("l2_p")
            if num == 123:
                self.l1_functions("l1_p")
                self.l2_functions("l2_p")
                self.l3_functions("l3_p")
            if num == 23:
                self.l2_functions("l2_p")
                self.l3_functions("l3_p")
            if num == 13:
                self.l1_functions("l1_p")
                self.l3_functions("l3_p")
        if param == "q":
            if num == 1:
                self.l1_functions("l1_q")
            if num == 2:
                self.l2_functions("l2_q")
            if num == 3:
                self.l3_functions("l3_q")
            if num == 12:
                self.l1_functions("l1_q")
                self.l2_functions("l2_q")
            if num == 123:
                self.l1_functions("l1_q")
                self.l2_functions("l2_q")
                self.l3_functions("l3_q")
            if num == 23:
                self.l2_functions("l2_q")
                self.l3_functions("l3_q")
            if num == 13:
                self.l1_functions("l1_q")
                self.l3_functions("l3_q")
        if param == "v":
            if num == 1:
                self.l1_functions("l1_v")
            if num == 2:
                self.l2_functions("l2_v")
            if num == 3:
                self.l3_functions("l3_v")
            if num == 12:
                self.l1_functions("l1_v")
                self.l2_functions("l2_v")
            if num == 123:
                self.l1_functions("l1_v")
                self.l2_functions("l2_v")
                self.l3_functions("l3_v")
            if num == 23:
                self.l2_functions("l2_v")
                self.l3_functions("l3_v")
            if num == 13:
                self.l1_functions("l1_v")
                self.l3_functions("l3_v")
        if param == "i":
            if num == 1:
                self.l1_functions("l1_i")
            if num == 2:
                self.l2_functions("l2_i")
            if num == 3:
                self.l3_functions("l3_i")
            if num == 12:
                self.l1_functions("l1_i")
                self.l2_functions("l2_i")
            if num == 123:
                self.l1_functions("l1_i")
                self.l2_functions("l2_i")
                self.l3_functions("l3_i")
            if num == 23:
                self.l2_functions("l2_i")
                self.l3_functions("l3_i")
            if num == 13:
                self.l1_functions("l1_i")
                self.l3_functions("l3_i")
        pass

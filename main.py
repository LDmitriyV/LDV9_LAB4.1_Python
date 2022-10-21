#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        row = 0
        col = 0
        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(-5, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        self.label_max_el.setText('Максимальный элемент: ')
        self.label_min_el.setText('Минимальный элемент: ')




    def solve(self):
        list_information_max_num = find_max(self.tableWidget)
        if list_information_max_num == None:
            self.label_error.setText('Введены некорректные данные!')
            self.label_task_done.setText("")
            self.label_task_error.setText("")
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')
            self.label_error.setText('')
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_max_num[3]) + ' [' +
                str(list_information_max_num[4]) + ';' + str(list_information_max_num[5]) + ']')
            self.label_error.setText('')
            # -*- решение задания -*-
            row = 0
            col = 0
            min_num = list_information_max_num[3]
            max_num = list_information_max_num[0]
            try:
                if (max_num / abs(min_num) < 10):
                    self.label_task_error.setText('Задание не будет выполнено.')
            except ZeroDivisionError:
                while row < self.tableWidget.rowCount():
                    while col < self.tableWidget.columnCount():
                        item = int(self.tableWidget.item(row, col).text())
                        if item == 0:
                            self.tableWidget.setItem(row, col, QTableWidgetItem(str(1)))
                        if item < 0:
                            number = str(abs(item))
                            self.tableWidget.setItem(row, col, QTableWidgetItem(number))
                        col += 1
                    row += 1
                    col = 0
            else:
                while row < self.tableWidget.rowCount():
                    while col < self.tableWidget.columnCount():
                        item = int(self.tableWidget.item(row, col).text())
                        if item == 0:
                            self.tableWidget.setItem(row, col, QTableWidgetItem(str(1)))
                        if item < 0:
                            number = str(abs(item))
                            self.tableWidget.setItem(row, col, QTableWidgetItem(number))
                        col += 1
                    row += 1
                    col = 0
            self.label_task_done.setText('Задание выполнено.')



def find_max(table_widget):

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    row_min_number = 0  # номер строки, в котором находится максимальне число
    col_min_number = 0
    try:
        max_num = float(table_widget.item(row_max_number, col_max_number).text())
        min_num = float(table_widget.item(row_min_number, col_min_number).text())# Максимальное значение
        row = 0
        col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number >= max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                if number <= min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number, min_num, row_min_number, col_min_number]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

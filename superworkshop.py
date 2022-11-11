# -*- coding: utf-8 -*-

# Импорт всех библиотек
import csv
import sqlite3
import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtChart
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, \
    QStackedBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


# Конвертированный ui-файл в класс Python
class Interface(object):
    def setupUi(self, Form):
        Form.setObjectName("Interface")
        # Разрешение окна
        Form.resize(720, 480)

        # Размещение Layout-а
        self.vertical_Layout = QtWidgets.QWidget(Form)
        self.vertical_Layout.setGeometry(QtCore.QRect(0, 0, 190, 160))
        self.vertical_Layout.setObjectName("verticalLayoutWidget")
        self.buttons = QtWidgets.QVBoxLayout(self.vertical_Layout)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")

        # Наводим красоту линиями
        self.line1 = QtWidgets.QFrame(self.vertical_Layout)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        self.line2 = QtWidgets.QFrame(self.vertical_Layout)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")

        self.line3 = QtWidgets.QFrame(self.vertical_Layout)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")

        self.line4 = QtWidgets.QFrame(self.vertical_Layout)
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.buttons.addWidget(self.line4)

        self.bigline = QtWidgets.QFrame(Form)
        self.bigline.setGeometry(QtCore.QRect(175, 0, 30, 480))
        self.bigline.setFrameShape(QtWidgets.QFrame.VLine)
        self.bigline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bigline.setObjectName("bigline")

        # Общее количество
        self.total = QtWidgets.QPushButton(self.vertical_Layout)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.buttons.addWidget(self.total)

        # МГР
        self.mgr = QtWidgets.QPushButton(self.vertical_Layout)
        self.mgr.setObjectName("mgr")
        self.buttons.addWidget(self.mgr)
        self.buttons.addWidget(self.line2)

        # МП
        self.mp = QtWidgets.QPushButton(self.vertical_Layout)
        self.mp.setObjectName("mp")
        self.buttons.addWidget(self.mp)
        self.buttons.addWidget(self.line3)

        # МАЦП
        self.macp = QtWidgets.QPushButton(self.vertical_Layout)
        self.macp.setObjectName("macp")
        self.buttons.addWidget(self.macp)
        self.buttons.addWidget(self.line4)

        # Основная гистограмма
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 0, 530, 480))
        self.stackedWidget.setObjectName("stackedWidget")

        # Добавление модулей
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 345, 190, 140))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.adding_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.adding_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.adding_gridLayout.setObjectName("adding_gridLayout")

        # Ещё раз наводим красоту линиями
        self.line5 = QtWidgets.QFrame(Form)
        self.line5.setGeometry(QtCore.QRect(0, 300, 190, 15))
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line5.setObjectName("line5")

        self.line6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setObjectName("line6")
        self.adding_gridLayout.addWidget(self.line6, 0, 0, 1, 2)

        self.line7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line7.setObjectName("line7")
        self.adding_gridLayout.addWidget(self.line7, 4, 0, 1, 2)

        self.line8 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line8.setObjectName("line8")
        self.adding_gridLayout.addWidget(self.line8, 6, 0, 1, 2)

        # Операции которые проходит плата
        self.mounted = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.mounted.setObjectName("mounted")
        self.adding_gridLayout.addWidget(self.mounted, 1, 1, 1, 1)

        self.varnished = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.varnished.setObjectName("varnished")
        self.adding_gridLayout.addWidget(self.varnished, 2, 1, 1, 1)

        self.tested = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.tested.setObjectName("tested")
        self.adding_gridLayout.addWidget(self.tested, 3, 1, 1, 1)

        # Кнопка "Добавить"
        self.add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add.setObjectName("add")
        self.adding_gridLayout.addWidget(self.add, 5, 0, 1, 2)

        # Выбор типа платы
        self.choose = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.choose.setObjectName("chose")
        self.choose.addItem("")
        self.choose.addItem("")
        self.choose.addItem("")
        self.adding_gridLayout.addWidget(self.choose, 1, 0, 3, 1)

        # Надпись "Добавление платы"
        self.adding_label = QtWidgets.QLabel(Form)
        self.adding_label.setGeometry(QtCore.QRect(0, 310, 190, 30))
        self.adding_label.setObjectName("adding_label")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        # Задание названий
        Form.setWindowTitle(_translate("Form", "Суперцех"))
        self.total.setText(_translate("Form", "Общее количество"))
        self.mgr.setText(_translate("Form", "МГР"))
        self.mp.setText(_translate("Form", "МП"))
        self.macp.setText(_translate("Form", "МАЦП"))
        self.add.setText(_translate("Form", "Добавить"))
        self.choose.setItemText(0, _translate("Form", "МГР"))
        self.choose.setItemText(1, _translate("Form", "МП"))
        self.choose.setItemText(2, _translate("Form", "МАЦП"))
        self.mounted.setText(_translate("Form", "Монтаж"))
        self.varnished.setText(_translate("Form", "Лакирование"))
        self.tested.setText(_translate("Form", "Тестирование"))
        self.adding_label.setText(_translate("Form", "<html><head/><body><p \
        align=\"center\"><span style=\" font-size:10pt;\">Добавление модулей \
        </span></p></body></html>"))


# Основной класс программы
class SuperWorkshop(QMainWindow, Interface):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Иконка
        self.setWindowIcon(QtGui.QIcon('1111.png'))

        # Подключение базы данных
        self.con = sqlite3.connect('info_db.sqlite')
        self.cur = self.con.cursor()

        # Перенос данных из csv файла в БД
        self.csv_to_sqlite()

        # Функционал кнопок
        self.add.clicked.connect(self.adding)
        self.total.clicked.connect(self.main_chart)
        self.mgr.clicked.connect(self.secondary_chart)
        self.mp.clicked.connect(self.secondary_chart)
        self.macp.clicked.connect(self.secondary_chart)
        self.total.click()

    # Вносим информацию из csv файла в базу данных
    def csv_to_sqlite(self):
        # Данные вносятся, если БД пустая
        if sum([sum(self.values('МГР')), sum(self.values('МП')),
                sum(self.values('МАЦП'))]) == 0:
            for file in ['mgr.csv', 'mp.csv', 'macp.csv']:
                with open(file, encoding='utf8') as csv_file:
                    reader = csv.reader(csv_file, delimiter=';',
                                        quotechar='"')
                    operations = {'montage': 0,
                                  'varnishing': 0,
                                  'testing': 0}
                    for i in reader:
                        if i[1] == '+':
                            operations['montage'] += 1
                        if i[2] == '+':
                            operations['varnishing'] += 1
                        if i[3] == '+':
                            operations['testing'] += 1
                    for k, v in operations.items():
                        self.cur.execute(f"""UPDATE {file[:-4].upper()}
                                            SET {k} = {v}""")
                self.con.commit()

    # Показ гистограммы
    def show_chart(self, count, categories):
        # Создание гистограммы
        self.count = QtChart.QBarSet('')
        # Столбцы
        self.count.append(count)
        self.series = QStackedBarSeries()

        # Значения столбцов
        self.series.setLabelsPosition(1)
        self.series.setLabelsVisible(True)
        self.series.append(self.count)
        self.chart = QChart()
        self.chart.addSeries(self.series)

        # Анимация появления столбцов
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = categories

        # Ось OX
        axisX = QBarCategoryAxis()
        axisX.append(self.categories)
        self.chart.addAxis(axisX, QtCore.Qt.AlignBottom)

        # Ось OY
        axisY = QValueAxis()
        # Следующие 3 строки нужны для того,
        # чтобы отметки на оси OY были целыми числами
        maxY = max(self.count)
        while maxY % 4 != 0:
            maxY += 1
        axisY.setRange(0, maxY)
        self.chart.addAxis(axisY, QtCore.Qt.AlignLeft)
        # Прикрепляем оси
        self.series.attachAxis(axisX)
        self.series.attachAxis(axisY)
        # Скрываем ненужную легенду
        self.chart.legend().setVisible(False)

        # Отображение гистограммы
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.stackedWidget.addWidget(self.chart_view)
        self.stackedWidget.setCurrentWidget(self.chart_view)

    def main_chart(self):
        # Информация основной гистограммы
        count = [sum(self.values('МГР')), sum(self.values('МП')),
                 sum(self.values('МАЦП'))]
        categories = ['МГР', 'МП', 'МАЦП']
        self.show_chart(count, categories)

    def secondary_chart(self):
        # Информация гистограммы об отдельном модуле
        count = self.values(self.sender().text())
        categories = ['Монтаж', 'Лакирование', 'Тестирование']
        self.show_chart(count, categories)

    # Достаём из БД информацию о модулях
    def values(self, module_type):
        if module_type == 'МГР':
            self.name = 'MGR'
        elif module_type == 'МП':
            self.name = 'MP'
        elif module_type == 'МАЦП':
            self.name = 'MACP'

        try:
            # Сколько плат прошли монтаж комнонентов
            montage = self.cur.execute(f"""SELECT montage
                               FROM {self.name}""").fetchall()[0][0]

            # Сколько плат прошли лакирование
            varnishing = self.cur.execute(f"""SELECT varnishing
                               FROM {self.name}""").fetchall()[0][0]

            # Сколько плат прошли тестирование
            testing = self.cur.execute(f"""SELECT testing
                               FROM {self.name}""").fetchall()[0][0]
            return [montage, varnishing, testing]
        except IndexError:
            # Изначально вносим нулевые значения
            self.cur.execute(f"""INSERT INTO {self.name} 
                (montage, varnishing, testing) VALUES (0, 0, 0)""")
            self.con.commit()
            return [0, 0, 0]

    # Добавление элементов в БД
    def adding(self):
        if self.choose.currentIndex() == 0:
            self.name = 'MGR'
        elif self.choose.currentIndex() == 1:
            self.name = 'MP'
        elif self.choose.currentIndex() == 2:
            self.name = 'MACP'

        # +1 если выбрана операция
        if self.mounted.checkState():
            self.cur.execute(f"""UPDATE {self.name}
                                SET montage = montage + 1""")
        if self.varnished.checkState():
            self.cur.execute(f"""UPDATE {self.name}
                                SET varnishing = varnishing + 1""")
        if self.tested.checkState():
            self.cur.execute(f"""UPDATE {self.name}
                                SET testing = testing + 1""")
        # Если не выбрана ни одна операция то выводится сообщение об ошибке
        if not self.mounted.checkState() and not self.varnished.checkState() \
                and not self.tested.checkState():
            QMessageBox.information(window, 'Ошибка',
                                    'Модуль должен проходить какую либо опера'
                                    'цию', QMessageBox.Ok)
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SuperWorkshop()
    # Задаём фиксированный размер окна
    window.setFixedSize(720, 480)
    window.show()
    sys.exit(app.exec())

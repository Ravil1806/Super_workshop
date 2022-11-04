# -*- coding: utf-8 -*-

# Импорт всех библиотек
import sys
import sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui, QtChart
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, \
    QStackedBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication


# Отконвертированный ui-файл в класс Python
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Название окна
        Form.setWindowTitle(_translate("Form", "Суперцех"))
        # Надписи на кнопках
        self.total.setText(_translate("Form", "Общее количество"))
        self.mgr.setText(_translate("Form", "МГР"))
        self.mp.setText(_translate("Form", "МП"))
        self.macp.setText(_translate("Form", "МАЦП"))


# Основной класс программы
class SuperWorkshop(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Иконка для приложения
        self.setWindowIcon(QtGui.QIcon('1111.png'))

        # Подключение базы данных
        self.con = sqlite3.connect('info_db.sqlite')
        self.cur = self.con.cursor()

        # Функционал кнопок
        self.total.clicked.connect(self.main_chart)
        self.mgr.clicked.connect(self.secodary_chart)
        self.mp.clicked.connect(self.secodary_chart)
        self.macp.clicked.connect(self.secodary_chart)
        self.total.click()

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
        self.series.attachAxis(axisX)
        self.series.attachAxis(axisY)

        self.chart.legend().setVisible(False)
        # Отображение основной гистограммы
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

    def secodary_chart(self):
        # Информация остальных гистограмм
        count = self.values(self.sender().text())
        categories = ['Монтаж', 'Лакирование', 'Тестирование']
        self.show_chart(count, categories)

    def values(self, who):
        if who == 'МГР':
            name = 'MGR'
        elif who == 'МП':
            name = 'MP'
        elif who == 'МАЦП':
            name = 'MACP'
        # Сколько плат прошли монтаж
        montage = self.cur.execute(f"""SELECT montage
                           FROM {name}""").fetchall()[0][0]
        # Сколько плат прошли лакирование
        varnishing = self.cur.execute(f"""SELECT varnishing
                           FROM {name}""").fetchall()[0][0]
        # Сколько плат прошли тестированиеё
        testing = self.cur.execute(f"""SELECT testing
                           FROM {name}""").fetchall()[0][0]
        return [montage, varnishing, testing]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SuperWorkshop()
    window.setFixedSize(720, 480)
    window.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kryds_og_bolle_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(332, 428)
        self.actionNyt_spil = QAction(MainWindow)
        self.actionNyt_spil.setObjectName(u"actionNyt_spil")
        self.actionLuk_spil = QAction(MainWindow)
        self.actionLuk_spil.setObjectName(u"actionLuk_spil")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.info_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.knap_4 = QPushButton(self.centralwidget)
        self.knap_4.setObjectName(u"knap_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knap_4.sizePolicy().hasHeightForWidth())
        self.knap_4.setSizePolicy(sizePolicy)
        self.knap_4.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_4, 1, 1, 1, 1)

        self.knap_1 = QPushButton(self.centralwidget)
        self.knap_1.setObjectName(u"knap_1")
        sizePolicy.setHeightForWidth(self.knap_1.sizePolicy().hasHeightForWidth())
        self.knap_1.setSizePolicy(sizePolicy)
        self.knap_1.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_1, 0, 1, 1, 1)

        self.knap_0 = QPushButton(self.centralwidget)
        self.knap_0.setObjectName(u"knap_0")
        sizePolicy.setHeightForWidth(self.knap_0.sizePolicy().hasHeightForWidth())
        self.knap_0.setSizePolicy(sizePolicy)
        self.knap_0.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_0, 0, 0, 1, 1)

        self.knap_3 = QPushButton(self.centralwidget)
        self.knap_3.setObjectName(u"knap_3")
        sizePolicy.setHeightForWidth(self.knap_3.sizePolicy().hasHeightForWidth())
        self.knap_3.setSizePolicy(sizePolicy)
        self.knap_3.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_3, 1, 0, 1, 1)

        self.knap_2 = QPushButton(self.centralwidget)
        self.knap_2.setObjectName(u"knap_2")
        sizePolicy.setHeightForWidth(self.knap_2.sizePolicy().hasHeightForWidth())
        self.knap_2.setSizePolicy(sizePolicy)
        self.knap_2.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_2, 0, 2, 1, 1)

        self.knap_5 = QPushButton(self.centralwidget)
        self.knap_5.setObjectName(u"knap_5")
        sizePolicy.setHeightForWidth(self.knap_5.sizePolicy().hasHeightForWidth())
        self.knap_5.setSizePolicy(sizePolicy)
        self.knap_5.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_5, 1, 2, 1, 1)

        self.knap_6 = QPushButton(self.centralwidget)
        self.knap_6.setObjectName(u"knap_6")
        sizePolicy.setHeightForWidth(self.knap_6.sizePolicy().hasHeightForWidth())
        self.knap_6.setSizePolicy(sizePolicy)
        self.knap_6.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_6, 2, 0, 1, 1)

        self.knap_8 = QPushButton(self.centralwidget)
        self.knap_8.setObjectName(u"knap_8")
        sizePolicy.setHeightForWidth(self.knap_8.sizePolicy().hasHeightForWidth())
        self.knap_8.setSizePolicy(sizePolicy)
        self.knap_8.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_8, 2, 2, 1, 1)

        self.knap_7 = QPushButton(self.centralwidget)
        self.knap_7.setObjectName(u"knap_7")
        sizePolicy.setHeightForWidth(self.knap_7.sizePolicy().hasHeightForWidth())
        self.knap_7.setSizePolicy(sizePolicy)
        self.knap_7.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.knap_7, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spiller_x_score = QLabel(self.centralwidget)
        self.spiller_x_score.setObjectName(u"spiller_x_score")

        self.horizontalLayout.addWidget(self.spiller_x_score)

        self.spiller_o_score = QLabel(self.centralwidget)
        self.spiller_o_score.setObjectName(u"spiller_o_score")
        self.spiller_o_score.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spiller_o_score)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 332, 23))
        self.menuFiler = QMenu(self.menubar)
        self.menuFiler.setObjectName(u"menuFiler")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFiler.menuAction())
        self.menuFiler.addAction(self.actionNyt_spil)
        self.menuFiler.addSeparator()
        self.menuFiler.addAction(self.actionLuk_spil)

        self.retranslateUi(MainWindow)
        self.actionLuk_spil.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kryds og bolle", None))
        self.actionNyt_spil.setText(QCoreApplication.translate("MainWindow", u"Nyt spil", None))
        self.actionLuk_spil.setText(QCoreApplication.translate("MainWindow", u"Luk spil", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Infolabel", None))
        self.knap_4.setText("")
        self.knap_1.setText("")
        self.knap_0.setText("")
        self.knap_3.setText("")
        self.knap_2.setText("")
        self.knap_5.setText("")
        self.knap_6.setText("")
        self.knap_8.setText("")
        self.knap_7.setText("")
        self.spiller_x_score.setText(QCoreApplication.translate("MainWindow", u"Spiller X: 0", None))
        self.spiller_o_score.setText(QCoreApplication.translate("MainWindow", u"Spiller O: 0", None))
        self.menuFiler.setTitle(QCoreApplication.translate("MainWindow", u"Filer", None))
    # retranslateUi


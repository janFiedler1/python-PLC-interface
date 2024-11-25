/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QTabWidget *tabWidget;
    QWidget *tab_3;
    QGridLayout *gridLayout;
    QProgressBar *progressBar;
    QLabel *label_2;
    QLabel *label;
    QLCDNumber *lcdNumber;
    QPushButton *pushButton_2;
    QSpacerItem *verticalSpacer;
    QPushButton *pushButton;
    QSlider *horizontalSlider;
    QSpacerItem *horizontalSpacer;
    QWidget *tab_4;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(898, 542);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setObjectName("gridLayout_2");
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName("tabWidget");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        tab_3 = new QWidget();
        tab_3->setObjectName("tab_3");
        gridLayout = new QGridLayout(tab_3);
        gridLayout->setObjectName("gridLayout");
        progressBar = new QProgressBar(tab_3);
        progressBar->setObjectName("progressBar");
        progressBar->setValue(24);

        gridLayout->addWidget(progressBar, 0, 4, 1, 1);

        label_2 = new QLabel(tab_3);
        label_2->setObjectName("label_2");

        gridLayout->addWidget(label_2, 3, 3, 1, 1);

        label = new QLabel(tab_3);
        label->setObjectName("label");
        label->setWordWrap(true);

        gridLayout->addWidget(label, 1, 4, 1, 1);

        lcdNumber = new QLCDNumber(tab_3);
        lcdNumber->setObjectName("lcdNumber");

        gridLayout->addWidget(lcdNumber, 3, 2, 1, 1);

        pushButton_2 = new QPushButton(tab_3);
        pushButton_2->setObjectName("pushButton_2");

        gridLayout->addWidget(pushButton_2, 1, 1, 1, 3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        gridLayout->addItem(verticalSpacer, 2, 4, 2, 1);

        pushButton = new QPushButton(tab_3);
        pushButton->setObjectName("pushButton");

        gridLayout->addWidget(pushButton, 0, 1, 1, 3);

        horizontalSlider = new QSlider(tab_3);
        horizontalSlider->setObjectName("horizontalSlider");
        horizontalSlider->setMinimum(1);
        horizontalSlider->setMaximum(8);
        horizontalSlider->setValue(4);
        horizontalSlider->setSliderPosition(4);
        horizontalSlider->setTracking(true);
        horizontalSlider->setOrientation(Qt::Orientation::Horizontal);

        gridLayout->addWidget(horizontalSlider, 2, 1, 1, 3);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 5, 2, 1);

        tabWidget->addTab(tab_3, QString());
        tab_4 = new QWidget();
        tab_4->setObjectName("tab_4");
        tabWidget->addTab(tab_4, QString());

        gridLayout_2->addWidget(tabWidget, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName("statusBar");
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Cups", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "The coffee will be ready in __ minutes/seconds", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "Cancel Brew", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Brew Coffee", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QCoreApplication::translate("MainWindow", "Coffee Controls", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_4), QCoreApplication::translate("MainWindow", "Settings", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

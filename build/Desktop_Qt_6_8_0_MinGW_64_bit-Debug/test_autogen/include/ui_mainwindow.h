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
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QTabWidget *tabWidget;
    QWidget *controls_tab;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_2;
    QLineEdit *text_input_1;
    QPushButton *enter_button;
    QPushButton *start_button;
    QPushButton *stop_button;
    QGraphicsView *graphics_view;
    QWidget *settings_tab;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(898, 542);
        MainWindow->setTabShape(QTabWidget::TabShape::Rounded);
        MainWindow->setDockOptions(QMainWindow::DockOption::AllowTabbedDocks|QMainWindow::DockOption::AnimatedDocks);
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
        controls_tab = new QWidget();
        controls_tab->setObjectName("controls_tab");
        gridLayout = new QGridLayout(controls_tab);
        gridLayout->setObjectName("gridLayout");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        text_input_1 = new QLineEdit(controls_tab);
        text_input_1->setObjectName("text_input_1");

        verticalLayout_2->addWidget(text_input_1);

        enter_button = new QPushButton(controls_tab);
        enter_button->setObjectName("enter_button");

        verticalLayout_2->addWidget(enter_button);

        start_button = new QPushButton(controls_tab);
        start_button->setObjectName("start_button");

        verticalLayout_2->addWidget(start_button);

        stop_button = new QPushButton(controls_tab);
        stop_button->setObjectName("stop_button");

        verticalLayout_2->addWidget(stop_button);


        horizontalLayout->addLayout(verticalLayout_2);

        graphics_view = new QGraphicsView(controls_tab);
        graphics_view->setObjectName("graphics_view");

        horizontalLayout->addWidget(graphics_view);


        gridLayout->addLayout(horizontalLayout, 0, 1, 1, 1);

        tabWidget->addTab(controls_tab, QString());
        settings_tab = new QWidget();
        settings_tab->setObjectName("settings_tab");
        tabWidget->addTab(settings_tab, QString());

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
        enter_button->setText(QCoreApplication::translate("MainWindow", "Enter", nullptr));
        start_button->setText(QCoreApplication::translate("MainWindow", "Start", nullptr));
        stop_button->setText(QCoreApplication::translate("MainWindow", "Stop", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(controls_tab), QCoreApplication::translate("MainWindow", "Controls", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(settings_tab), QCoreApplication::translate("MainWindow", "Settings", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

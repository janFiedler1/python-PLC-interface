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
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout_5;
    QTabWidget *tabWidget;
    QWidget *controls_tab;
    QWidget *verticalLayoutWidget_3;
    QVBoxLayout *verticalLayout_4;
    QWidget *widget_3;
    QWidget *widget_2;
    QPushButton *start_button;
    QPushButton *stop_button;
    QLineEdit *text_input_1;
    QPushButton *enter_button;
    QWidget *settings_tab;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QComboBox *comboBox;
    QSpacerItem *verticalSpacer_2;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QSpacerItem *verticalSpacer_3;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer_2;
    QWidget *widget;
    QSpacerItem *verticalSpacer;
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
        horizontalLayout_5 = new QHBoxLayout(centralwidget);
        horizontalLayout_5->setObjectName("horizontalLayout_5");
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName("tabWidget");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        controls_tab = new QWidget();
        controls_tab->setObjectName("controls_tab");
        verticalLayoutWidget_3 = new QWidget(controls_tab);
        verticalLayoutWidget_3->setObjectName("verticalLayoutWidget_3");
        verticalLayoutWidget_3->setGeometry(QRect(400, 10, 202, 408));
        verticalLayout_4 = new QVBoxLayout(verticalLayoutWidget_3);
        verticalLayout_4->setObjectName("verticalLayout_4");
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        widget_3 = new QWidget(verticalLayoutWidget_3);
        widget_3->setObjectName("widget_3");
        widget_3->setMinimumSize(QSize(200, 200));

        verticalLayout_4->addWidget(widget_3);

        widget_2 = new QWidget(verticalLayoutWidget_3);
        widget_2->setObjectName("widget_2");
        widget_2->setMinimumSize(QSize(200, 200));
        widget_2->setBaseSize(QSize(30, 30));

        verticalLayout_4->addWidget(widget_2);

        start_button = new QPushButton(controls_tab);
        start_button->setObjectName("start_button");
        start_button->setGeometry(QRect(11, 71, 80, 24));
        stop_button = new QPushButton(controls_tab);
        stop_button->setObjectName("stop_button");
        stop_button->setGeometry(QRect(11, 101, 80, 24));
        text_input_1 = new QLineEdit(controls_tab);
        text_input_1->setObjectName("text_input_1");
        text_input_1->setGeometry(QRect(11, 11, 108, 24));
        enter_button = new QPushButton(controls_tab);
        enter_button->setObjectName("enter_button");
        enter_button->setGeometry(QRect(11, 41, 80, 24));
        tabWidget->addTab(controls_tab, QString());
        settings_tab = new QWidget();
        settings_tab->setObjectName("settings_tab");
        verticalLayout_5 = new QVBoxLayout(settings_tab);
        verticalLayout_5->setObjectName("verticalLayout_5");
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName("verticalLayout");
        label = new QLabel(settings_tab);
        label->setObjectName("label");
        label->setMaximumSize(QSize(16777215, 30));

        verticalLayout->addWidget(label);

        comboBox = new QComboBox(settings_tab);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName("comboBox");
        comboBox->setEditable(false);

        verticalLayout->addWidget(comboBox);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);

        radioButton = new QRadioButton(settings_tab);
        radioButton->setObjectName("radioButton");

        verticalLayout->addWidget(radioButton);

        radioButton_2 = new QRadioButton(settings_tab);
        radioButton_2->setObjectName("radioButton_2");

        verticalLayout->addWidget(radioButton_2);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        verticalLayout->addItem(verticalSpacer_3);


        horizontalLayout_2->addLayout(verticalLayout);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        label_2 = new QLabel(settings_tab);
        label_2->setObjectName("label_2");
        label_2->setMaximumSize(QSize(16777215, 30));

        horizontalLayout_3->addWidget(label_2);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_2);

        widget = new QWidget(settings_tab);
        widget->setObjectName("widget");

        horizontalLayout_3->addWidget(widget);


        verticalLayout_3->addLayout(horizontalLayout_3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        verticalLayout_3->addItem(verticalSpacer);


        horizontalLayout_2->addLayout(verticalLayout_3);


        verticalLayout_5->addLayout(horizontalLayout_2);

        tabWidget->addTab(settings_tab, QString());

        horizontalLayout_5->addWidget(tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName("statusBar");
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);
        comboBox->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        start_button->setText(QCoreApplication::translate("MainWindow", "Start", nullptr));
        stop_button->setText(QCoreApplication::translate("MainWindow", "Stop", nullptr));
        enter_button->setText(QCoreApplication::translate("MainWindow", "Enter", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(controls_tab), QCoreApplication::translate("MainWindow", "Controls", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Select PLC to connect to", nullptr));
        comboBox->setItemText(0, QCoreApplication::translate("MainWindow", "Local TwinCat XAE PLC", nullptr));
        comboBox->setItemText(1, QCoreApplication::translate("MainWindow", "Beckhoff PLC", nullptr));
        comboBox->setItemText(2, QCoreApplication::translate("MainWindow", "Allen Bradley PLC", nullptr));

        comboBox->setCurrentText(QCoreApplication::translate("MainWindow", "Local TwinCat XAE PLC", nullptr));
        comboBox->setPlaceholderText(QString());
        radioButton->setText(QCoreApplication::translate("MainWindow", "Default", nullptr));
        radioButton_2->setText(QCoreApplication::translate("MainWindow", "Custom", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Connection Status", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(settings_tab), QCoreApplication::translate("MainWindow", "Settings", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

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
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
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
    QGridLayout *gridLayout_2;
    QTabWidget *tabWidget;
    QWidget *controls_tab;
    QGridLayout *gridLayout_4;
    QLabel *label_10;
    QGroupBox *graph_box;
    QGridLayout *gridLayout;
    QWidget *empty_widget_1;
    QWidget *empty_widget_3;
    QWidget *empty_widget_2;
    QGroupBox *controls_box;
    QGridLayout *gridLayout_3;
    QPushButton *live_data_button;
    QPushButton *alarm_history_button;
    QPushButton *historical_data_button;
    QPushButton *data_settings_button;
    QPushButton *login_button;
    QLabel *label_2;
    QWidget *settings_tab;
    QHBoxLayout *horizontalLayout_2;
    QGroupBox *plc_settings_box;
    QVBoxLayout *verticalLayout_3;
    QComboBox *plc_select_dropdown;
    QRadioButton *default_plc_radio;
    QRadioButton *custom_plc_radio;
    QGroupBox *groupBox_5;
    QFormLayout *formLayout_2;
    QLineEdit *plc_ip_port;
    QLineEdit *plc_port_input;
    QLabel *label_5;
    QLabel *label_3;
    QPushButton *plc_connect_button;
    QSpacerItem *verticalSpacer_4;
    QGroupBox *groupBox_4;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_9;
    QLabel *plc_connection_status_label;
    QGroupBox *database_settings_box;
    QVBoxLayout *verticalLayout_2;
    QComboBox *db_select_dropdown;
    QGroupBox *db_settings_form;
    QFormLayout *formLayout;
    QLabel *label_8;
    QLineEdit *db_host_input;
    QLineEdit *db_db_input;
    QLabel *label_7;
    QLineEdit *db_login_input;
    QLabel *label_4;
    QLineEdit *db_password_input;
    QLabel *label_6;
    QPushButton *db_connect_button;
    QSpacerItem *verticalSpacer;
    QGroupBox *db_connection_status_box;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label;
    QLabel *db_connected_label;
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
        gridLayout_4 = new QGridLayout(controls_tab);
        gridLayout_4->setObjectName("gridLayout_4");
        label_10 = new QLabel(controls_tab);
        label_10->setObjectName("label_10");
        QSizePolicy sizePolicy1(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_10->sizePolicy().hasHeightForWidth());
        label_10->setSizePolicy(sizePolicy1);
        label_10->setStyleSheet(QString::fromUtf8("background-color: red;"));

        gridLayout_4->addWidget(label_10, 1, 2, 1, 1);

        graph_box = new QGroupBox(controls_tab);
        graph_box->setObjectName("graph_box");
        gridLayout = new QGridLayout(graph_box);
        gridLayout->setObjectName("gridLayout");
        empty_widget_1 = new QWidget(graph_box);
        empty_widget_1->setObjectName("empty_widget_1");

        gridLayout->addWidget(empty_widget_1, 0, 1, 1, 1);

        empty_widget_3 = new QWidget(graph_box);
        empty_widget_3->setObjectName("empty_widget_3");

        gridLayout->addWidget(empty_widget_3, 1, 1, 1, 1);

        empty_widget_2 = new QWidget(graph_box);
        empty_widget_2->setObjectName("empty_widget_2");

        gridLayout->addWidget(empty_widget_2, 0, 2, 1, 1);


        gridLayout_4->addWidget(graph_box, 2, 0, 1, 1);

        controls_box = new QGroupBox(controls_tab);
        controls_box->setObjectName("controls_box");
        QSizePolicy sizePolicy2(QSizePolicy::Policy::Fixed, QSizePolicy::Policy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(controls_box->sizePolicy().hasHeightForWidth());
        controls_box->setSizePolicy(sizePolicy2);
        controls_box->setMinimumSize(QSize(300, 0));
        controls_box->setMaximumSize(QSize(500, 16777215));
        gridLayout_3 = new QGridLayout(controls_box);
        gridLayout_3->setObjectName("gridLayout_3");
        live_data_button = new QPushButton(controls_box);
        live_data_button->setObjectName("live_data_button");
        QSizePolicy sizePolicy3(QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Ignored);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(live_data_button->sizePolicy().hasHeightForWidth());
        live_data_button->setSizePolicy(sizePolicy3);

        gridLayout_3->addWidget(live_data_button, 0, 0, 1, 1);

        alarm_history_button = new QPushButton(controls_box);
        alarm_history_button->setObjectName("alarm_history_button");
        sizePolicy3.setHeightForWidth(alarm_history_button->sizePolicy().hasHeightForWidth());
        alarm_history_button->setSizePolicy(sizePolicy3);

        gridLayout_3->addWidget(alarm_history_button, 1, 1, 1, 1);

        historical_data_button = new QPushButton(controls_box);
        historical_data_button->setObjectName("historical_data_button");
        sizePolicy3.setHeightForWidth(historical_data_button->sizePolicy().hasHeightForWidth());
        historical_data_button->setSizePolicy(sizePolicy3);

        gridLayout_3->addWidget(historical_data_button, 0, 1, 1, 1);

        data_settings_button = new QPushButton(controls_box);
        data_settings_button->setObjectName("data_settings_button");
        sizePolicy3.setHeightForWidth(data_settings_button->sizePolicy().hasHeightForWidth());
        data_settings_button->setSizePolicy(sizePolicy3);

        gridLayout_3->addWidget(data_settings_button, 1, 0, 1, 1);

        login_button = new QPushButton(controls_box);
        login_button->setObjectName("login_button");
        sizePolicy3.setHeightForWidth(login_button->sizePolicy().hasHeightForWidth());
        login_button->setSizePolicy(sizePolicy3);

        gridLayout_3->addWidget(login_button, 2, 0, 1, 2);


        gridLayout_4->addWidget(controls_box, 2, 2, 1, 1);

        label_2 = new QLabel(controls_tab);
        label_2->setObjectName("label_2");
        sizePolicy1.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy1);
        label_2->setStyleSheet(QString::fromUtf8("background-color: red;"));

        gridLayout_4->addWidget(label_2, 1, 0, 1, 1);

        tabWidget->addTab(controls_tab, QString());
        settings_tab = new QWidget();
        settings_tab->setObjectName("settings_tab");
        horizontalLayout_2 = new QHBoxLayout(settings_tab);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        plc_settings_box = new QGroupBox(settings_tab);
        plc_settings_box->setObjectName("plc_settings_box");
        verticalLayout_3 = new QVBoxLayout(plc_settings_box);
        verticalLayout_3->setObjectName("verticalLayout_3");
        plc_select_dropdown = new QComboBox(plc_settings_box);
        plc_select_dropdown->addItem(QString());
        plc_select_dropdown->addItem(QString());
        plc_select_dropdown->addItem(QString());
        plc_select_dropdown->setObjectName("plc_select_dropdown");
        plc_select_dropdown->setEditable(false);

        verticalLayout_3->addWidget(plc_select_dropdown);

        default_plc_radio = new QRadioButton(plc_settings_box);
        default_plc_radio->setObjectName("default_plc_radio");

        verticalLayout_3->addWidget(default_plc_radio);

        custom_plc_radio = new QRadioButton(plc_settings_box);
        custom_plc_radio->setObjectName("custom_plc_radio");

        verticalLayout_3->addWidget(custom_plc_radio);

        groupBox_5 = new QGroupBox(plc_settings_box);
        groupBox_5->setObjectName("groupBox_5");
        formLayout_2 = new QFormLayout(groupBox_5);
        formLayout_2->setObjectName("formLayout_2");
        plc_ip_port = new QLineEdit(groupBox_5);
        plc_ip_port->setObjectName("plc_ip_port");

        formLayout_2->setWidget(1, QFormLayout::FieldRole, plc_ip_port);

        plc_port_input = new QLineEdit(groupBox_5);
        plc_port_input->setObjectName("plc_port_input");

        formLayout_2->setWidget(3, QFormLayout::FieldRole, plc_port_input);

        label_5 = new QLabel(groupBox_5);
        label_5->setObjectName("label_5");

        formLayout_2->setWidget(3, QFormLayout::LabelRole, label_5);

        label_3 = new QLabel(groupBox_5);
        label_3->setObjectName("label_3");

        formLayout_2->setWidget(1, QFormLayout::LabelRole, label_3);


        verticalLayout_3->addWidget(groupBox_5);

        plc_connect_button = new QPushButton(plc_settings_box);
        plc_connect_button->setObjectName("plc_connect_button");

        verticalLayout_3->addWidget(plc_connect_button);

        verticalSpacer_4 = new QSpacerItem(20, 144, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        verticalLayout_3->addItem(verticalSpacer_4);

        groupBox_4 = new QGroupBox(plc_settings_box);
        groupBox_4->setObjectName("groupBox_4");
        groupBox_4->setStyleSheet(QString::fromUtf8("background-color: red;"));
        horizontalLayout_4 = new QHBoxLayout(groupBox_4);
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        label_9 = new QLabel(groupBox_4);
        label_9->setObjectName("label_9");

        horizontalLayout_4->addWidget(label_9);

        plc_connection_status_label = new QLabel(groupBox_4);
        plc_connection_status_label->setObjectName("plc_connection_status_label");
        plc_connection_status_label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        horizontalLayout_4->addWidget(plc_connection_status_label);


        verticalLayout_3->addWidget(groupBox_4);


        horizontalLayout_2->addWidget(plc_settings_box);

        database_settings_box = new QGroupBox(settings_tab);
        database_settings_box->setObjectName("database_settings_box");
        verticalLayout_2 = new QVBoxLayout(database_settings_box);
        verticalLayout_2->setObjectName("verticalLayout_2");
        db_select_dropdown = new QComboBox(database_settings_box);
        db_select_dropdown->addItem(QString());
        db_select_dropdown->setObjectName("db_select_dropdown");
        db_select_dropdown->setEditable(false);

        verticalLayout_2->addWidget(db_select_dropdown);

        db_settings_form = new QGroupBox(database_settings_box);
        db_settings_form->setObjectName("db_settings_form");
        formLayout = new QFormLayout(db_settings_form);
        formLayout->setObjectName("formLayout");
        label_8 = new QLabel(db_settings_form);
        label_8->setObjectName("label_8");

        formLayout->setWidget(4, QFormLayout::LabelRole, label_8);

        db_host_input = new QLineEdit(db_settings_form);
        db_host_input->setObjectName("db_host_input");

        formLayout->setWidget(4, QFormLayout::FieldRole, db_host_input);

        db_db_input = new QLineEdit(db_settings_form);
        db_db_input->setObjectName("db_db_input");

        formLayout->setWidget(7, QFormLayout::FieldRole, db_db_input);

        label_7 = new QLabel(db_settings_form);
        label_7->setObjectName("label_7");

        formLayout->setWidget(7, QFormLayout::LabelRole, label_7);

        db_login_input = new QLineEdit(db_settings_form);
        db_login_input->setObjectName("db_login_input");

        formLayout->setWidget(0, QFormLayout::FieldRole, db_login_input);

        label_4 = new QLabel(db_settings_form);
        label_4->setObjectName("label_4");

        formLayout->setWidget(0, QFormLayout::LabelRole, label_4);

        db_password_input = new QLineEdit(db_settings_form);
        db_password_input->setObjectName("db_password_input");

        formLayout->setWidget(2, QFormLayout::FieldRole, db_password_input);

        label_6 = new QLabel(db_settings_form);
        label_6->setObjectName("label_6");

        formLayout->setWidget(2, QFormLayout::LabelRole, label_6);


        verticalLayout_2->addWidget(db_settings_form);

        db_connect_button = new QPushButton(database_settings_box);
        db_connect_button->setObjectName("db_connect_button");

        verticalLayout_2->addWidget(db_connect_button);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        db_connection_status_box = new QGroupBox(database_settings_box);
        db_connection_status_box->setObjectName("db_connection_status_box");
        db_connection_status_box->setStyleSheet(QString::fromUtf8("background-color: red;"));
        horizontalLayout_3 = new QHBoxLayout(db_connection_status_box);
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        label = new QLabel(db_connection_status_box);
        label->setObjectName("label");

        horizontalLayout_3->addWidget(label);

        db_connected_label = new QLabel(db_connection_status_box);
        db_connected_label->setObjectName("db_connected_label");
        db_connected_label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        horizontalLayout_3->addWidget(db_connected_label);


        verticalLayout_2->addWidget(db_connection_status_box);


        horizontalLayout_2->addWidget(database_settings_box);

        tabWidget->addTab(settings_tab, QString());

        gridLayout_2->addWidget(tabWidget, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName("statusBar");
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(1);
        plc_select_dropdown->setCurrentIndex(0);
        db_select_dropdown->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "Database: Connected", nullptr));
        graph_box->setTitle(QCoreApplication::translate("MainWindow", "Graphs", nullptr));
        controls_box->setTitle(QCoreApplication::translate("MainWindow", "Controls", nullptr));
        live_data_button->setText(QCoreApplication::translate("MainWindow", "Live Data", nullptr));
        alarm_history_button->setText(QCoreApplication::translate("MainWindow", "Alarm History", nullptr));
        historical_data_button->setText(QCoreApplication::translate("MainWindow", "Historical Data", nullptr));
        data_settings_button->setText(QCoreApplication::translate("MainWindow", "Alarms/Graphs", nullptr));
        login_button->setText(QCoreApplication::translate("MainWindow", "Login", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "PLC: Disconnected", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(controls_tab), QCoreApplication::translate("MainWindow", "Controls", nullptr));
        plc_settings_box->setTitle(QCoreApplication::translate("MainWindow", "Connect PLC", nullptr));
        plc_select_dropdown->setItemText(0, QCoreApplication::translate("MainWindow", "Local TwinCat XAE PLC", nullptr));
        plc_select_dropdown->setItemText(1, QCoreApplication::translate("MainWindow", "Beckhoff PLC", nullptr));
        plc_select_dropdown->setItemText(2, QCoreApplication::translate("MainWindow", "Allen Bradley PLC", nullptr));

        plc_select_dropdown->setCurrentText(QCoreApplication::translate("MainWindow", "Local TwinCat XAE PLC", nullptr));
        plc_select_dropdown->setPlaceholderText(QString());
        default_plc_radio->setText(QCoreApplication::translate("MainWindow", "Default", nullptr));
        custom_plc_radio->setText(QCoreApplication::translate("MainWindow", "Custom", nullptr));
        groupBox_5->setTitle(QString());
        label_5->setText(QCoreApplication::translate("MainWindow", "Port", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "IP Address", nullptr));
        plc_connect_button->setText(QCoreApplication::translate("MainWindow", "Connect", nullptr));
        groupBox_4->setTitle(QString());
        label_9->setText(QCoreApplication::translate("MainWindow", "Connection Status:", nullptr));
        plc_connection_status_label->setText(QCoreApplication::translate("MainWindow", "Disconnected", nullptr));
        database_settings_box->setTitle(QCoreApplication::translate("MainWindow", "Connect Database", nullptr));
        db_select_dropdown->setItemText(0, QCoreApplication::translate("MainWindow", "Local DB", nullptr));

        db_select_dropdown->setCurrentText(QCoreApplication::translate("MainWindow", "Local DB", nullptr));
        db_select_dropdown->setPlaceholderText(QString());
        db_settings_form->setTitle(QString());
        label_8->setText(QCoreApplication::translate("MainWindow", "Host", nullptr));
        db_host_input->setText(QCoreApplication::translate("MainWindow", "localhost", nullptr));
        db_db_input->setText(QCoreApplication::translate("MainWindow", "plc_data_1", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Database", nullptr));
        db_login_input->setText(QCoreApplication::translate("MainWindow", "plc_login", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "User", nullptr));
        db_password_input->setText(QCoreApplication::translate("MainWindow", "test123", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Password", nullptr));
        db_connect_button->setText(QCoreApplication::translate("MainWindow", "Connect", nullptr));
        db_connection_status_box->setTitle(QString());
        label->setText(QCoreApplication::translate("MainWindow", "Connection Status:", nullptr));
        db_connected_label->setText(QCoreApplication::translate("MainWindow", "Disconnected", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(settings_tab), QCoreApplication::translate("MainWindow", "Settings", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

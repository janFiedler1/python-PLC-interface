#!/bin/bash
pyuic5 mainwindow.ui -o python-interface/app.py
pyuic5 alarms_graphs.ui -o python-interface/alarms.py


#sed -i -e 's/abc/XYZ/g' /tmp/file.txt
# MainWindow.setTabShape(QtCore.Qt.QTabWidget::TabShape::Rounded)
# self.plc_connection_status_label.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)
# self.db_connected_label.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignRight|QtCore.Qt.Qt::AlignmentFlag::AlignTrailing|QtCore.Qt.Qt::AlignmentFlag::AlignVCenter)


# self.scrollArea.setLayoutDirection(QtCore.Qt.Qt::LayoutDirection::LeftToRight)
# self.scrollArea.setAlignment(QtCore.Qt.Qt::AlignmentFlag::AlignLeading|QtCore.Qt.Qt::AlignmentFlag::AlignLeft|QtCore.Qt.Qt::AlignmentFlag::AlignTop)
# self.buttonBox.setOrientation(QtCore.Qt.Qt::Orientation::Horizontal)
# self.buttonBox.setStandardButtons(QtCore.Qt.QDialogButtonBox::StandardButton::Cancel|QtCore.Qt.QDialogButtonBox::StandardButton::Ok)

# replace
# self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOffQtCore.Qt.Qt::ScrollBarPolicy::ScrollBarAlwaysOff)
# self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
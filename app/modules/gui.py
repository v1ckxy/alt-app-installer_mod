import os

from PyQt6 import QtCore, QtGui, QtWidgets

# parent directory for absloute path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Ui_MainProgram(object):
    def setupUi(self, MainProgram):
        MainProgram.setObjectName("MainProgram")
        MainProgram.setEnabled(True)
        MainProgram.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainProgram.sizePolicy().hasHeightForWidth())
        MainProgram.setSizePolicy(sizePolicy)
        MainProgram.setMinimumSize(QtCore.QSize(0, 0))
        MainProgram.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainProgram)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.imagetitle = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagetitle.sizePolicy().hasHeightForWidth())
        self.imagetitle.setSizePolicy(sizePolicy)
        self.imagetitle.setMinimumSize(QtCore.QSize(51, 51))
        self.imagetitle.setMaximumSize(QtCore.QSize(51, 51))
        self.imagetitle.setText("")
        self.imagetitle.setPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/installer_icon.png")
        )
        self.imagetitle.setScaledContents(True)
        self.imagetitle.setObjectName("imagetitle")
        self.horizontalLayout_3.addWidget(self.imagetitle)
        self.Title_2 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_2.sizePolicy().hasHeightForWidth())
        self.Title_2.setSizePolicy(sizePolicy)
        self.Title_2.setMaximumSize(QtCore.QSize(319, 42))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Title_2.setFont(font)
        self.Title_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Title_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.Title_2.setObjectName("Title_2")
        self.horizontalLayout_3.addWidget(self.Title_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            0,
            25,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Select_app_label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Select_app_label.sizePolicy().hasHeightForWidth()
        )
        self.Select_app_label.setSizePolicy(sizePolicy)
        self.Select_app_label.setMaximumSize(QtCore.QSize(225, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Select_app_label.setFont(font)
        self.Select_app_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.Select_app_label.setObjectName("Select_app_label")
        self.horizontalLayout_4.addWidget(self.Select_app_label)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(114, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.stop_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setMaximumSize(QtCore.QSize(114, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_4.addWidget(self.stop_btn)
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(
            400,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(
            18,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem8)
        self.Main_bar = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_bar.sizePolicy().hasHeightForWidth())
        self.Main_bar.setSizePolicy(sizePolicy)
        self.Main_bar.setMinimumSize(QtCore.QSize(0, 25))
        self.Main_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Main_bar.setFont(font)
        self.Main_bar.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.Main_bar.setObjectName("Main_bar")
        self.horizontalLayout.addWidget(self.Main_bar)
        self.mainprogressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainprogressBar.sizePolicy().hasHeightForWidth()
        )
        self.mainprogressBar.setSizePolicy(sizePolicy)
        self.mainprogressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.mainprogressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mainprogressBar.setFont(font)
        self.mainprogressBar.setProperty("value", 30)
        self.mainprogressBar.setTextVisible(False)
        self.mainprogressBar.setObjectName("mainprogressBar")
        self.horizontalLayout.addWidget(self.mainprogressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(
            40,
            10,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Current_bar = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Current_bar.sizePolicy().hasHeightForWidth())
        self.Current_bar.setSizePolicy(sizePolicy)
        self.Current_bar.setMinimumSize(QtCore.QSize(5, 25))
        self.Current_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Current_bar.setBaseSize(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Current_bar.setFont(font)
        self.Current_bar.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.Current_bar.setObjectName("Current_bar")
        self.horizontalLayout_2.addWidget(self.Current_bar)
        self.currentprogressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.currentprogressBar.sizePolicy().hasHeightForWidth()
        )
        self.currentprogressBar.setSizePolicy(sizePolicy)
        self.currentprogressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.currentprogressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.currentprogressBar.setBaseSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.currentprogressBar.setFont(font)
        self.currentprogressBar.setAutoFillBackground(False)
        self.currentprogressBar.setProperty("value", 50)
        self.currentprogressBar.setTextVisible(False)
        self.currentprogressBar.setObjectName("currentprogressBar")
        self.horizontalLayout_2.addWidget(self.currentprogressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainProgram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainProgram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.advancedmenu = QtWidgets.QMenu(parent=self.menuOptions)
        self.advancedmenu.setEnabled(True)
        self.advancedmenu.setTearOffEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/advanced.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.advancedmenu.setIcon(icon)
        self.advancedmenu.setToolTipsVisible(False)
        self.advancedmenu.setObjectName("advancedmenu")
        self.Dependencymenu = QtWidgets.QMenu(parent=self.advancedmenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/dependency.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.Dependencymenu.setIcon(icon1)
        self.Dependencymenu.setObjectName("Dependencymenu")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainProgram.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainProgram)
        self.statusbar.setObjectName("statusbar")
        MainProgram.setStatusBar(self.statusbar)
        self.actionInstall_From_File = QtGui.QAction(parent=MainProgram)
        self.actionInstall_From_File.setObjectName("actionInstall_From_File")
        self.actionDownload_From_Url = QtGui.QAction(parent=MainProgram)
        self.actionDownload_From_Url.setObjectName("actionDownload_From_Url")
        self.actionclear_cache = QtGui.QAction(parent=MainProgram)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/clear.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionclear_cache.setIcon(icon2)
        self.actionclear_cache.setObjectName("actionclear_cache")
        self.actionInstall_Driver_Chrome = QtGui.QAction(parent=MainProgram)
        self.actionInstall_Driver_Chrome.setObjectName("actionInstall_Driver_Chrome")
        self.actionInstall_Chrome_Driver = QtGui.QAction(parent=MainProgram)
        self.actionInstall_Chrome_Driver.setObjectName("actionInstall_Chrome_Driver")
        self.actionCheck_For_Updates = QtGui.QAction(parent=MainProgram)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/update.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionCheck_For_Updates.setIcon(icon3)
        self.actionCheck_For_Updates.setObjectName("actionCheck_For_Updates")
        self.actionAbout = QtGui.QAction(parent=MainProgram)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/about.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setStatusTip("")
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(parent=MainProgram)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/help.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOpen_Logs = QtGui.QAction(parent=MainProgram)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/log.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionOpen_Logs.setIcon(icon6)
        self.actionOpen_Logs.setObjectName("actionOpen_Logs")
        self.actionDownload_From_Url_2 = QtGui.QAction(parent=MainProgram)
        self.actionDownload_From_Url_2.setObjectName("actionDownload_From_Url_2")
        self.actioninstall_From_File = QtGui.QAction(parent=MainProgram)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/file.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actioninstall_From_File.setIcon(icon7)
        self.actioninstall_From_File.setObjectName("actioninstall_From_File")
        self.actionSet_Wait_Time = QtGui.QAction(parent=MainProgram)
        self.actionSet_Wait_Time.setObjectName("actionSet_Wait_Time")
        self.actionDownloads = QtGui.QAction(parent=MainProgram)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/downloads.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionDownloads.setIcon(icon8)
        self.actionDownloads.setObjectName("actionDownloads")
        self.actionAll_Dependencies = QtGui.QAction(parent=MainProgram)
        self.actionAll_Dependencies.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/unchecked.png"),
            QtGui.QIcon.Mode.Selected,
            QtGui.QIcon.State.Off,
        )
        icon9.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/checked.png"),
            QtGui.QIcon.Mode.Selected,
            QtGui.QIcon.State.On,
        )
        self.actionAll_Dependencies.setIcon(icon9)
        self.actionAll_Dependencies.setObjectName("actionAll_Dependencies")
        self.actionIgnore_Latest_Version = QtGui.QAction(parent=MainProgram)
        self.actionIgnore_Latest_Version.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/unchecked.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon10.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/checked.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        self.actionIgnore_Latest_Version.setIcon(icon10)
        self.actionIgnore_Latest_Version.setObjectName("actionIgnore_Latest_Version")
        self.actionIgnore_All_filters = QtGui.QAction(parent=MainProgram)
        self.actionIgnore_All_filters.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/unchecked.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        icon11.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/checked.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon11.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/unchecked.png"),
            QtGui.QIcon.Mode.Selected,
            QtGui.QIcon.State.Off,
        )
        icon11.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/checked.png"),
            QtGui.QIcon.Mode.Selected,
            QtGui.QIcon.State.On,
        )
        self.actionIgnore_All_filters.setIcon(icon11)
        self.actionIgnore_All_filters.setObjectName("actionIgnore_All_filters")
        self.actionget_using_url = QtGui.QAction(parent=MainProgram)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(f"{parent_dir}/data/images/link.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.actionget_using_url.setIcon(icon12)
        self.actionget_using_url.setObjectName("actionget_using_url")
        self.actionDownload_Mode = QtGui.QAction(parent=MainProgram)
        self.actionDownload_Mode.setCheckable(True)
        self.actionDownload_Mode.setChecked(True)
        self.actionDownload_Mode.setIcon(icon10)
        self.actionDownload_Mode.setObjectName("actionDownload_Mode")
        self.actionDedicated_Folder = QtGui.QAction(parent=MainProgram)
        self.actionDedicated_Folder.setCheckable(True)
        self.actionDedicated_Folder.setChecked(True)
        self.actionDedicated_Folder.setIcon(icon10)
        self.actionDedicated_Folder.setObjectName("actionDedicated_Folder")
        self.Dependencymenu.addAction(self.actionIgnore_Latest_Version)
        self.Dependencymenu.addAction(self.actionIgnore_All_filters)
        self.advancedmenu.addAction(self.actionDownload_Mode)
        self.advancedmenu.addAction(self.actionDedicated_Folder)
        self.advancedmenu.addAction(self.actionclear_cache)
        self.advancedmenu.addAction(self.Dependencymenu.menuAction())
        self.menuOptions.addAction(self.actionDownloads)
        self.menuOptions.addAction(self.actionget_using_url)
        self.menuOptions.addAction(self.actioninstall_From_File)
        self.menuOptions.addAction(self.advancedmenu.menuAction())
        self.menuAbout.addAction(self.actionCheck_For_Updates)
        self.menuAbout.addAction(self.actionOpen_Logs)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainProgram)
        QtCore.QMetaObject.connectSlotsByName(MainProgram)

    def retranslateUi(self, MainProgram):
        _translate = QtCore.QCoreApplication.translate
        MainProgram.setWindowTitle(_translate("MainProgram", "Alt App Installer"))
        self.Title_2.setText(_translate("MainProgram", "Alt App Installer"))
        self.Select_app_label.setText(
            _translate("MainProgram", "Select App To Install:")
        )
        self.pushButton.setText(_translate("MainProgram", "Choose App"))
        self.stop_btn.setText(_translate("MainProgram", "Stop"))
        self.Main_bar.setText(_translate("MainProgram", "Main Progress: "))
        self.Current_bar.setText(_translate("MainProgram", "Current Progress: "))
        self.menuOptions.setTitle(_translate("MainProgram", "Options"))
        self.advancedmenu.setStatusTip(_translate("MainProgram", "Advanced Settings"))
        self.advancedmenu.setTitle(_translate("MainProgram", "Advanced"))
        self.Dependencymenu.setStatusTip(
            _translate("MainProgram", "Dependency Download Option")
        )
        self.Dependencymenu.setTitle(_translate("MainProgram", "Dependencies"))
        self.menuAbout.setTitle(_translate("MainProgram", "Help"))
        self.actionInstall_From_File.setText(
            _translate("MainProgram", "Install From File")
        )
        self.actionInstall_From_File.setStatusTip(
            _translate("MainProgram", "Install App (appx,Msix) From Local File")
        )
        self.actionDownload_From_Url.setText(
            _translate("MainProgram", "Install From Url")
        )
        self.actionDownload_From_Url.setStatusTip(
            _translate(
                "MainProgram",
                "Install from link given by user (link of the app from microsoft.com)",
            )
        )
        self.actionclear_cache.setText(_translate("MainProgram", "Clear Cache"))
        self.actionclear_cache.setStatusTip(
            _translate("MainProgram", "Clear all files like [downloads,logs.. etc]")
        )
        self.actionInstall_Driver_Chrome.setText(
            _translate("MainProgram", "Install Driver + Chrome")
        )
        self.actionInstall_Chrome_Driver.setText(
            _translate("MainProgram", "Install Chrome Driver")
        )
        self.actionInstall_Chrome_Driver.setStatusTip(
            _translate("MainProgram", "Download and install chrome driver")
        )
        self.actionCheck_For_Updates.setText(
            _translate("MainProgram", "Check For Updates")
        )
        self.actionCheck_For_Updates.setStatusTip(
            _translate("MainProgram", "Check for updates")
        )
        self.actionAbout.setText(_translate("MainProgram", "About"))
        self.actionHelp.setText(_translate("MainProgram", "Help"))
        self.actionHelp.setStatusTip(_translate("MainProgram", "Get Help"))
        self.actionOpen_Logs.setText(_translate("MainProgram", "Open Logs"))
        self.actionOpen_Logs.setStatusTip(_translate("MainProgram", "Open log file"))
        self.actionDownload_From_Url_2.setText(
            _translate("MainProgram", "Download From Url")
        )
        self.actionDownload_From_Url_2.setStatusTip(
            _translate(
                "MainProgram",
                "Download from link given by user (link of the app from microsoft.com)",
            )
        )
        self.actioninstall_From_File.setText(
            _translate("MainProgram", "Install UWP App")
        )
        self.actioninstall_From_File.setStatusTip(
            _translate("MainProgram", "Install app (Appx,Msix..etc) from local file ")
        )
        self.actionSet_Wait_Time.setText(_translate("MainProgram", "Set Wait Time"))
        self.actionSet_Wait_Time.setStatusTip(
            _translate(
                "MainProgram", "Set Wait Time ( Use If Slow Internet Speed,Default: 5)"
            )
        )
        self.actionDownloads.setText(_translate("MainProgram", "Downloads"))
        self.actionDownloads.setStatusTip(
            _translate("MainProgram", "Open downloads folder")
        )
        self.actionAll_Dependencies.setText(
            _translate("MainProgram", "All Dependencies")
        )
        self.actionIgnore_Latest_Version.setText(
            _translate("MainProgram", "Ignore  Version")
        )
        self.actionIgnore_Latest_Version.setStatusTip(
            _translate("MainProgram", "Download all versions of the dependencies")
        )
        self.actionIgnore_All_filters.setText(
            _translate("MainProgram", "Ignore All  Filters")
        )
        self.actionIgnore_All_filters.setStatusTip(
            _translate(
                "MainProgram",
                "Download all dependencies regardless of system arch (x64,x32,Arm), type (Appx,Msix..etc), latest version",
            )
        )
        self.actionget_using_url.setText(_translate("MainProgram", "Get From Link"))
        self.actionget_using_url.setStatusTip(
            _translate("MainProgram", "Get the app from the link (app url)")
        )
        self.actionDownload_Mode.setText(_translate("MainProgram", "Download Mode"))
        self.actionDownload_Mode.setStatusTip(
            _translate("MainProgram", "Enable download only mode")
        )
        self.actionDedicated_Folder.setText(
            _translate("MainProgram", "Dedicated Folder")
        )
        self.actionDedicated_Folder.setStatusTip(
            _translate(
                "MainProgram",
                "Download the apps to separate folder [causes increase in bandwith and storage space]",
            )
        )

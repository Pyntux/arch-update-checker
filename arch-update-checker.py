#!/bin/env python

import sys
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

default_icon = '/usr/bin/arch-update-checker/icon.png'
update_icon = '/usr/bin/arch-update-checker/update.png'

class UpdateChecker:
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_updates)
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon(default_icon))
        self.tray_icon.setToolTip("Arch Update Checker")
        self.tray_icon.show()
        self.menu = QMenu()
        self.action_check_updates = QAction('Check for updates')
        self.action_check_updates.triggered.connect(self.check_updates)
        self.action_update = QAction('Update')
        self.action_update.setVisible(False)
        self.action_update.triggered.connect(self.update_system)
        self.action_quit = QAction('Quit')
        self.action_quit.triggered.connect(QApplication.quit)
        self.menu.addAction(self.action_check_updates)
        self.menu.addAction(self.action_update)
        self.menu.addAction(self.action_quit)
        self.tray_icon.setContextMenu(self.menu)

        # Check for updates immediately on startup with a delay of 20 seconds
        QTimer.singleShot(20000, self.check_updates_startup)

        # Check for updates every hour
        self.timer.start(3600000)

    def check_updates_startup(self):
        process = subprocess.run(['checkupdates'], capture_output=True, text=True)
        updates = process.stdout.strip().split('\n')
        if updates and updates[0].strip() != '':
            message = f'There are {len(updates)} updates available!'
            self.tray_icon.setIcon(QIcon(update_icon))
            self.action_update.setVisible(True)
            self.tray_icon.showMessage('Arch Update Checker', message)
        else:
            self.tray_icon.setIcon(QIcon(default_icon))

    def check_updates(self):
        process = subprocess.run(['checkupdates'], capture_output=True, text=True)
        updates = process.stdout.strip().split('\n')
        if updates and updates[0].strip() != '':
            message = f'There are {len(updates)} updates available!'
            self.tray_icon.setIcon(QIcon(update_icon))
            self.action_update.setVisible(True)
        else:
            message = 'Your system is up to date.'
            self.tray_icon.setIcon(QIcon(default_icon))
            self.action_update.setVisible(False)
        self.tray_icon.showMessage('Arch Update Checker', message)

    def check_updates_after_click_on_update(self):
        process = subprocess.run(['checkupdates'], capture_output=True, text=True)
        updates = process.stdout.strip().split('\n')
        if updates and updates[0].strip() != '':
            message = f'There are {len(updates)} updates available!'
            self.tray_icon.setIcon(QIcon(update_icon))
            self.action_update.setVisible(True)
        else:
            self.tray_icon.setIcon(QIcon(default_icon))
            self.action_update.setVisible(False)

    def update_system(self):
        subprocess.Popen(['konsole', '-e', 'sudo', 'pacman', '-Syu'])
        QTimer.singleShot(20000, self.check_updates_after_click_on_update)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('Arch Update Checker')
    update_checker = UpdateChecker()
    sys.exit(app.exec_())

# arch-update-checker
Simple tray icon which will check for Arch Linux updates.

This APP is WORK in PROGRESS!

1. For this app to work you need to have installed:
  - python
  - python-pyqt5
  - pacman-contrib
  
2. The application assumes that you are using "konsole" terminal emulator. You can change that in code...


MANUAL INSTALL:


Copy "arch-update-checker", "icon.png" and "update.png" in to a "PATH" directory of yours.

For example, you can add "~/.local/bin" to your path by adding:

export PATH="$HOME/.local/bin:$PATH"

in to your .bashrc (if you are using bash)

than copy files in to ~/.local/bin. Now you can start app from terminal just by typing "arch-update-checker"

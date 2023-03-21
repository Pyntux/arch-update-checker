install:
	install -d '$(DESTDIR)'/usr/bin/
	install -m755 arch-update-checker '$(DESTDIR)'/usr/bin/arch-update-checker-tray
	install -d '$(DESTDIR)'/usr/share/arch-update-checker-tray/
	cp -r icon.png '$(DESTDIR)'/usr/share/arch-update-checker-tray/
	cp -r update.png '$(DESTDIR)'/usr/share/arch-update-checker-tray/
	install -d '$(DESTDIR)'/usr/share/applications/
	cp arch-update-checker-tray.desktop '$(DESTDIR)'/usr/share/applications/arch-update-checker-tray.desktop


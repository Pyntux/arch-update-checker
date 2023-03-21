pkgname=arch-update-checker
pkgver=1.0.0
pkgrel=1
pkgdesc="A system tray application for checking and updating Arch Linux packages"
arch=('any')
url="https://github.com/Pyntux/arch-update-checker/"
license=('MIT')
depends=('python' 'python-pyqt5' 'pacman-contrib')
makedepends=('git')
source=("git+${url}.git")
sha256sums=('SKIP')

package() {
    install -d '$(DESTDIR)'/usr/bin/
	install -m755 arch-update-checker '$(DESTDIR)'/usr/bin/arch-update-checker
	install -d '$(DESTDIR)'/usr/share/arch-update-checker/
	cp -r icon.png '$(DESTDIR)'/usr/share/arch-update-checker/
	cp -r update.png '$(DESTDIR)'/usr/share/arch-update-checker/
	install -d '$(DESTDIR)'/usr/share/applications/
	cp arch-update-checker.desktop '$(DESTDIR)'/usr/share/applications/arch-update-checker.desktop
}

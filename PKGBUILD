pkgname=arch-update-checker
pkgver=1.0.0
pkgrel=1
pkgdesc="A system tray application for checking and updating Arch Linux packages"
arch=('any')
url="https://github.com/Pyntux/arch-update-checker/"
license=('GPL3')
depends=('python' 'python-pyqt5' 'pacman-contrib')
makedepends=('git')
source=("git+${url}.git")
sha256sums=('SKIP')

package() {
    cd "$srcdir"
    mkdir -p "$pkgdir/usr/bin"
    cp -r yourrepository/* "$pkgdir/usr/bin/arch-update-checker"
    chmod +x "$pkgdir/usr/bin/arch-update-checker/main.py"
    install -Dm644 "$pkgdir/usr/bin/arch-update-checker/icon.png" "$pkgdir/usr/share/icons/hicolor/48x48/apps/arch-update-checker.png"
    install -Dm644 "$pkgdir/usr/bin/arch-update-checker/update.png" "$pkgdir/usr/share/icons/hicolor/48x48/apps/arch-update-checker-update.png"
    install -Dm644 "$pkgdir/usr/bin/arch-update-checker/arch-update-checker.desktop" "$pkgdir/usr/share/applications/arch-update-checker.desktop"
}

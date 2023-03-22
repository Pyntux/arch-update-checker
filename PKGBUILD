pkgname=arch-update-checker
pkgver=1.0
pkgrel=1
pkgdesc="A system tray tool for checking for updates on Arch Linux."
arch=('any')
url="https://github.com/Pyntux/arch-update-checker"
license=('MIT')
depends=('python' 'python-pyqt5' 'pacman-contrib')
makedepends=('git')
source=("git+$url")
md5sums=('SKIP')

package() {
    cd "$srcdir/$pkgname"
    install -Dm755 arch-update-checker.py "$pkgdir/usr/bin/arch-update-checker"
    install -Dm644 icon.png "$pkgdir/usr/bin/arch-update-checker/icon.png"
    install -Dm644 update.png "$pkgdir/usr/bin/arch-update-checker/update.png"
    install -Dm644 arch-update-checker.desktop "$pkgdir/usr/share/applications/arch-update-checker.desktop"
}

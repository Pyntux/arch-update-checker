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
#    cd "${pkgname%-*}"
    make install DESTDIR="$pkgdir"
}

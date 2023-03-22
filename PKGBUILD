pkgname=arch-update-checker
pkgver=1.0
pkgrel=1
pkgdesc="A system tray application for Arch Linux that checks for updates"
arch=('any')
url="https://github.com/Pyntux/arch-update-checker"
license=('MIT')
depends=('python' 'python-pyqt5' 'pacman-contrib')
makedepends=('git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  # No build needed
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm644 icon.png "${pkgdir}/usr/bin/arch-update-checker/icon.png"
  install -Dm644 update.png "${pkgdir}/usr/bin/arch-update-checker/update.png"
  install -Dm644 arch-update-checker.py "${pkgdir}/usr/bin/arch-update-checker/arch-update-checker.py"
  install -Dm644 arch-update-checker.desktop "${pkgdir}/usr/share/applications/arch-update-checker.desktop"
}

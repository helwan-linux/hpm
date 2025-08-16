# Maintainer: Saeed Badreldeen <your-email@example.com>
pkgname=hpm
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Package Manager - a simple package manager frontend for Arch Linux."
arch=('x86_64')
url="https://github.com/helwan-linux/helwan-pkg-manager"
license=('MIT')
depends=('python-rich' 'python-typer' 'python' 'sudo' 'pacman')
makedepends=('git')
provides=('hpm')
source=("git+https://github.com/helwan-linux/helwan-pkg-manager.git")
md5sums=('SKIP')

build() {
    cd "$srcdir/helwan-pkg-manager"
    # لا حاجة لعملية build حقيقية
    :
}

package() {
    cd "$srcdir/helwan-pkg-manager"

    # نسخ الحزمة إلى /usr/lib/hpm
    mkdir -p "$pkgdir/usr/lib/hpm"
    cp -r hpm/* "$pkgdir/usr/lib/hpm/"
    cp -r hpm/assets "$pkgdir/usr/lib/hpm/assets"

    # إنشاء wrapper script في /usr/bin
    mkdir -p "$pkgdir/usr/bin"
    cat > "$pkgdir/usr/bin/hpm" <<'EOF'
#!/usr/bin/env bash
PYTHONPATH=/usr/lib/hpm python3 /usr/lib/hpm/main.py "$@"
EOF
    chmod +x "$pkgdir/usr/bin/hpm"
}


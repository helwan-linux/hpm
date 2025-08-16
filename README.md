# hpm – A Friendly Frontend for Pacman

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Arch%20Linux-blue.svg)](https://archlinux.org)

`hpm` is a user-friendly and minimal CLI frontend for `pacman`, designed for Arch Linux users and derivatives. It simplifies common package management tasks through readable and intuitive commands.

---

## 🚀 Features

* 📦 Simple commands: `install`, `remove`, `upgrade`, etc.
* 🧹 System maintenance tools: cache cleaning and orphan management
* 🔍 Package search and info display
* 📜 Command history tracking
* 🌐 AUR support via `yay`
* 🩺 Full system health check (`doctor` command)
* 🧪 Dry-run mode (`--dry-run`) for safe testing
* 📁 Written in Python using `Typer` and `Rich`

---

## 🛠️ Installation

### From Source

```bash
sudo pacman -S hpm
```

This will make the `hpm` command globally available in your terminal.

---

## 📚 Usage

### 📦 Install & Remove

```bash
hpm instalar firefox
hpm remove nano
```

### 🔄 Upgrade & Refresh

```bash
hpm upgrade         # Upgrade all installed packages
hpm refresh         # Sync databases + upgrade packages
```

### 🔍 Search & Info

```bash
hpm search terminal      # Search packages
hpm info htop            # Show detailed info
hpm list                 # List all installed packages
```

### 🧹 System Maintenance

```bash
hpm clean
hpm orphans list
hpm orphans remove
```

### 🌐 AUR Management

```bash
hpm aur install visual-studio-code-bin
```

### 🩺 System Health Check

```bash
hpm doctor
```

---

## 🧩 Global Options

* `--dry-run`, `-d`: Simulate actions without applying changes
* `--force`, `-f`: Skip confirmation prompts (for install/remove/upgrade)

---

## 📖 Command Table (Multi-language)

| Command (English) | Shortcut | Command (Arabic) | Command (Spanish) | Command (Chinese) |
| ----------------- | -------- | ---------------- | ----------------- | ----------------- |
| install           | i        | تثبيت            | instalar          | 安装                |
| remove            | r        | إزالة            | eliminar          | 卸载                |
| upgrade           | u        | ترقية            | actualizar        | 升级                |
| refresh           | s        | تحديث            | sincronizar       | 刷新                |
| search            | q        | بحث              | buscar            | 搜索                |
| info              | I        | معلومات          | informacion       | 信息                |
| list              | l        | قائمة            | lista             | 列表                |
| clean             | c        | تنظيف            | limpiar           | 清理                |
| orphans           | o        | يتيم             | huerfanos         | 孤儿                |
| aur               | a        | aur              | aur               | AUR               |
| doctor            | d        | فحص              | diagnostico       | 诊断                |
| history           | h        | سجل              | historial         | 历史                |
| --help            | —        | --مساعدة         | --ayuda           | --帮助              |

---

## 🧪 Development

To run the app locally:

```bash
hpm --help

hpm --帮助

hpm eliminar [pkg-name]

hpm سجل
```

To build a `.zst` package for Arch:

* Add a valid `PKGBUILD`
* Use `makepkg`

---

## 📄 License

MIT © Helwan Linux Team





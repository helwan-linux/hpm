# 📦 Helwan Package Manager (HPM)

### HPM is a human-friendly package manager for Helwan Linux, built on top of pacman with natural-language command chaining.

> **Note:** Each language supports its native **"then"** keyword for command chaining.

### 📥 Installation

# On Helwan Linux
sudo pacman -S hpm

# On other Arch-based distros
yay -S hpm


---

#### 🌐 اختر اللغة / Choose Language

* [العربية](#arabic)
* [English](#english)
* [中文 (Chinese)](#chinese)
* [Español (Spanish)](#spanish)
* [हिन्दी (Hindi)](#hindi)
* [اردو (Urdu)](#urdu)
* [🚀 Contributing](#contributing)

---

<a name="arabic"></a>

## 🇪🇬 النسخة العربية (Arabic)

هذا هو مدير الحزم الرسمي لتوزيعة "حلوان لينكس"، يدعم تنفيذ أوامر متعددة في سطر واحد.

| المهمة           | الأمر      | الاختصار | مثال                    |
| :--------------- | :--------- | :------- | :---------------------- |
| تثبيت حزمة       | `تثبيت`    | -        | `hpm تثبيت firefox`     |
| إزالة حزمة       | `إزالة`    | -        | `hpm إزالة vlc`         |
| ترقية النظام     | `ترقية`    | -        | `hpm ترقية`             |
| تحديث المستودعات | `تحديث`    | -        | `hpm تحديث`             |
| بحث عن حزمة      | `بحث`      | -        | `hpm بحث chrome`        |
| معلومات الحزمة   | `معلومات`  | -        | `hpm معلومات vlc`       |
| قائمة المثبت     | `قائمة`    | -        | `hpm قائمة`             |
| تنظيف النظام     | `تنظيف`    | -        | `hpm تنظيف`             |
| حزم يتيمة        | `يتيم`     | -        | `hpm يتيم`              |
| مستودع AUR       | `aur`      | -        | `hpm aur google-chrome` |
| فحص النظام       | `فحص`      | -        | `hpm فحص`               |
| سجل الأوامر      | `سجل`      | -        | `hpm سجل`               |
| المساعدة         | `--مساعدة` | -        | `hpm --مساعدة`          |

**💡 أمثلة التشغيل:**

* **أمر عادي:** `hpm تثبيت vlc`
* **أمر مجمع:** `hpm تحديث ثم ترقية ثم تنظيف ثم فحص`

---

<a name="english"></a>

## 🇺🇸 English Version

| Function    | Command   | Shortcut | Example               |
| :---------- | :-------- | :------- | :-------------------- |
| Install     | `install` | `i`      | `hpm i firefox`       |
| Remove      | `remove`  | `r`      | `hpm r vlc`           |
| Upgrade     | `upgrade` | `u`      | `hpm u`               |
| Refresh     | `refresh` | `s`      | `hpm s`               |
| Search      | `search`  | `q`      | `hpm q chrome`        |
| Info        | `info`    | `I`      | `hpm I vlc`           |
| List        | `list`    | `l`      | `hpm l`               |
| Clean       | `clean`   | `c`      | `hpm c`               |
| Orphans     | `orphans` | `o`      | `hpm o`               |
| AUR Support | `aur`     | `a`      | `hpm a google-chrome` |
| Doctor      | `doctor`  | `d`      | `hpm d`               |
| History     | `history` | `h`      | `hpm h`               |
| Help        | `--help`  | -        | `hpm --help`          |

**💡 Examples:**

* **Basic Command:** `hpm i vlc`
* **Chained Command:** `hpm s then u then c then d`

---

<a name="chinese"></a>

## 🇨🇳 中文版 (Chinese)

| 任务     | 命令     | 例子                      |
| :----- | :----- | :---------------------- |
| 安装     | `安装`   | `hpm 安装 firefox`        |
| 卸载     | `卸载`   | `hpm 卸载 vlc`            |
| 升级     | `升级`   | `hpm 升级`                |
| 刷新     | `刷新`   | `hpm 刷新`                |
| 搜索     | `搜索`   | `hpm 搜索 chrome`         |
| 信息     | `信息`   | `hpm 信息 vlc`            |
| 列表     | `列表`   | `hpm 列表`                |
| 清理     | `清理`   | `hpm 清理`                |
| 孤儿包    | `孤儿`   | `hpm 孤儿`                |
| AUR 支持 | `aur`  | `hpm aur google-chrome` |
| 诊断     | `诊断`   | `hpm 诊断`                |
| 历史     | `历史`   | `hpm 历史`                |
| 帮助     | `--帮助` | `hpm --帮助`              |

**💡 例子:**

* **基本命令:** `hpm 安装 vlc`
* **链式命令:** `hpm 刷新 然后 升级 然后 清理`

---

<a name="spanish"></a>

## 🇪🇸 Versión Española (Spanish)

| Función     | Comando       | Ejemplo                 |
| :---------- | :------------ | :---------------------- |
| Instalar    | `instalar`    | `hpm instalar firefox`  |
| Eliminar    | `eliminar`    | `hpm eliminar vlc`      |
| Actualizar  | `actualizar`  | `hpm actualizar`        |
| Sincronizar | `sincronizar` | `hpm sincronizar`       |
| Buscar      | `buscar`      | `hpm buscar chrome`     |
| Información | `informacion` | `hpm informacion vlc`   |
| Lista       | `lista`       | `hpm lista`             |
| Limpiar     | `limpiar`     | `hpm limpiar`           |
| Huérfanos   | `huerfanos`   | `hpm huerfanos`         |
| Soporte AUR | `aur`         | `hpm aur google-chrome` |
| Diagnóstico | `diagnostico` | `hpm diagnostico`       |
| Historial   | `historial`   | `hpm historial`         |
| Ayuda       | `--ayuda`     | `hpm --ayuda`           |

**💡 Ejemplos:**

* **Comando Básico:** `hpm instalar vlc`
* **Comando Combinado:** `hpm sincronizar luego actualizar luego limpiar`

---
<a name="hindi"></a>

## 🇮🇳 हिन्दी संस्करण (Hindi)

यह हेलवान لिनक्स का आधिकारिक पैकेज प्रबंधक है।

| कार्य | कमांड | उदाहरण |
| :--- | :--- | :--- |
| पैकेज स्थापित करें | `स्थापित` | `hpm स्थापित firefox` |
| पैकेज निकालें | `हटाएं` | `hpm हटाएं vlc` |
| सिस्टम अपग्रेड करें | `अपग्रेड` | `hpm अपग्रेड` |
| रिपॉजिटरी अपडेट करें | `अपडेट` | `hpm अपडेट` |
| पैकेज खोजें | `खोजें` | `hpm खोजें vlc` |
| जानकारी | `जानकारी` | `hpm जानकारी vlc` |
| सूची | `सूची` | `hpm सूची` |
| साफ़ करें | `साफ़` | `hpm साफ़` |
| अनाथ पैकेज | `अनाथ` | `hpm अनाथ` |
| एयूआर समर्थन | `aur` | `hpm aur google-chrome` |
| सिस्टम जांच | `जांच` | `hpm जांच` |
| इतिहास | `इतिहास` | `hpm इतिहास` |
| सहायता | `--सहायता` | `hpm --सहायता` |

**💡 उदाहरण (Chaining):**
`hpm अपडेट फिर अपग्रेड फिर साफ़`

---

<a name="urdu"></a>

## 🇵🇰 اردو ورژن (Urdu)

یہ حلوان لینکس کا آفیشل پیکیج مینیجر ہے۔

| ٹاسک | کمانڈ | مثال |
| :--- | :--- | :--- |
| پیکیج انسٹال کریں | `انسٹال` | `hpm انسٹال firefox` |
| پیکیج ختم کریں | `ختم` | `hpm ختم vlc` |
| سسٹم اپ گریڈ کریں | `اپ گریڈ` | `hpm اپ گریڈ` |
| ریپوزٹری تازہ کریں | `تازہ` | `hpm تازہ` |
| پیکیج تلاش کریں | `تلاش` | `hpm تلاش vlc` |
| معلومات | `معلومات` | `hpm معلومات vlc` |
| فہرست | `فہرست` | `hpm فہرست` |
| صفائی | `صفائی` | `hpm صفائی` |
| یتیم پیکیجز | `یتیم` | `hpm یتیم` |
| اے یو آر سپورٹ | `aur` | `hpm aur google-chrome` |
| ڈاکٹر (جانچ) | `ڈاکٹر` | `hpm ڈاکٹر` |
| تاریخ | `تاریخ` | `hpm تاریخ` |
| مدد | `--مدد` | `hpm --مدد` |

**💡 مثال (Chaining):**
`hpm تازہ پھر اپ گریڈ پھر صفائی`
---
<a name="contributing"></a>

## 🚀 Contributing to Helwan Linux

We welcome contributions from developers worldwide! Whether you want to add a new language, optimize the code, or fix a bug, here is how you can help:

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Branch**: `git checkout -b feature/NewFeature`.
3. **Commit Changes**: Use descriptive messages like `Add French language support`.
4. **Submit a Pull Request**: Explain your changes and wait for review.

### 🌐 Internationalization (i18n)

If you wish to add a new language to **HPM**, please check the `constants.py` file and add the corresponding translations for all commands.

---








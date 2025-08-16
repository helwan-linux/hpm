# hpm/i18n.py

LANGUAGES = {
    "en": {
        "description": "hpm: A simple and powerful package manager for Arch Linux.",
        "usage": "Usage",
        "dry_run_warning": "Running in dry-run mode. No changes will be made to the system.",
        "commands_title": "[bold blue]Available Commands[/bold blue]",
        "command_header": "Command",
        "description_header": "Description",
        "global_options_title": "Options",
        "dry_run_help": "Show what would be done without making any changes.",
        "lang_help": "Set the interface language.",
        "help_help": "Show this message and exit.",
        "command_aur_searching_helper": "Searching for AUR helper...",
        "command_aur_error_no_helper_found": "No AUR helper (yay or paru) found.",
        "command_aur_helper_install_info": "Please install an AUR helper to use this command.",
        "command_aur_using_helper": "Using AUR helper: {helper}",
        "command_aur_error_no_action_provided": "Please provide an action (e.g., install, remove, etc.).",
        "command_aur_installing_packages": "Installing AUR package(s): {packages}",
        "command_aur_removing_packages": "Removing AUR package(s): {packages}",
        "command_aur_searching_for_packages": "Searching for package(s): {packages}",
        "command_aur_upgrading_packages": "Upgrading packages...",
        "command_aur_error_unknown_action": "Error: Unknown action '{action}'.",
        "command_aur_error_no_package_provided": "Please provide a package name to install.",
        "command_aur_error_no_package_provided_remove": "Please provide a package name to remove.",
        "command_aur_error_no_search_term_provided": "Please provide a search term.",
        "dry_run_command_info": "The command that would be executed is: {command}",
        "operation_completed": "Operation completed successfully.",
        "command_aur_error_helper_not_found": "AUR helper not found. This error should not happen.",
        "command_aur_error_unexpected_error": "An unexpected error occurred: {error}",
        "commands": {
            "install": {"name": "install", "desc": "Installs one or more packages.", "aliases": ["i", "install"]},
            "remove": {"name": "remove", "desc": "Removes a package.", "aliases": ["r", "remove"]},
            "upgrade": {"name": "upgrade", "desc": "Upgrades all installed packages.", "aliases": ["u", "upgrade"]},
            "refresh": {"name": "refresh", "desc": "Synchronizes databases and upgrades packages.", "aliases": ["s", "refresh"]},
            "search": {"name": "search", "desc": "Searches for packages.", "aliases": ["q", "search"]},
            "info": {"name": "info", "desc": "Displays detailed package info.", "aliases": ["I", "info"]},
            "list": {"name": "list", "desc": "Lists all installed packages.", "aliases": ["l", "list"]},
            "clean": {"name": "clean", "desc": "Cleans the package cache.", "aliases": ["c", "clean"]},
            "orphans": {"name": "orphans", "desc": "Manages orphan packages.", "aliases": ["o", "orphans"]},
            "aur": {"name": "aur", "desc": "Manages packages from the AUR.", "aliases": ["a", "aur"]},
            "doctor": {"name": "doctor", "desc": "Performs a system health check.", "aliases": ["d", "doctor"]},
            "history": {"name": "history", "desc": "Displays command history.", "aliases": ["h", "history"]}
        }
    },
    "ar": {
        "description": "hpm: مدير حزم بسيط وقوي لـ Arch Linux.",
        "usage": "الاستخدام",
        "dry_run_warning": "يعمل في وضع التجربة. لن يتم إجراء أي تغييرات على النظام.",
        "commands_title": "[bold blue]الأوامر المتاحة[/bold blue]",
        "command_header": "الأمر",
        "description_header": "الوصف",
        "global_options_title": "الخيارات",
        "dry_run_help": "يعرض ما سيتم تنفيذه دون إجراء أي تغييرات.",
        "lang_help": "يضبط لغة الواجهة.",
        "help_help": "يعرض هذه الرسالة ويخرج.",
        "command_aur_searching_helper": "جارٍ البحث عن مساعد AUR...",
        "command_aur_error_no_helper_found": "لم يتم العثور على مساعد AUR (yay أو paru).",
        "command_aur_helper_install_info": "يرجى تثبيت مساعد AUR لاستخدام هذا الأمر.",
        "command_aur_using_helper": "يتم استخدام مساعد AUR: {helper}",
        "command_aur_error_no_action_provided": "يرجى تقديم إجراء (مثل تثبيت، إزالة، إلخ).",
        "command_aur_installing_packages": "جارٍ تثبيت حزمة(حزم) AUR: {packages}",
        "command_aur_removing_packages": "جارٍ إزالة حزمة(حزم) AUR: {packages}",
        "command_aur_searching_for_packages": "جارٍ البحث عن حزمة(حزم): {packages}",
        "command_aur_upgrading_packages": "جارٍ ترقية الحزم...",
        "command_aur_error_unknown_action": "خطأ: إجراء غير معروف '{action}'.",
        "command_aur_error_no_package_provided": "يرجى تقديم اسم حزمة للتثبيت.",
        "command_aur_error_no_package_provided_remove": "يرجى تقديم اسم حزمة للإزالة.",
        "command_aur_error_no_search_term_provided": "يرجى تقديم مصطلح للبحث.",
        "dry_run_command_info": "الأمر الذي سيتم تنفيذه: {command}",
        "operation_completed": "اكتملت العملية بنجاح.",
        "command_aur_error_helper_not_found": "لم يتم العثور على مساعد AUR. يجب ألا يحدث هذا الخطأ.",
        "command_aur_error_unexpected_error": "حدث خطأ غير متوقع: {error}",
        "commands": {
            "install": {"name": "تثبيت", "desc": "يثبت حزمة واحدة أو أكثر.", "aliases": ["i", "تثبيت", "install"]},
            "remove": {"name": "إزالة", "desc": "يزيل حزمة.", "aliases": ["r", "إزالة", "remove"]},
            "upgrade": {"name": "ترقية", "desc": "يرقي جميع الحزم المثبتة.", "aliases": ["u", "ترقية", "upgrade"]},
            "refresh": {"name": "تحديث", "desc": "يزامن قواعد البيانات ويرقي الحزم.", "aliases": ["s", "تحديث", "refresh"]},
            "search": {"name": "بحث", "desc": "يبحث عن حزم.", "aliases": ["q", "بحث", "search"]},
            "info": {"name": "معلومات", "desc": "يعرض معلومات مفصلة عن الحزمة.", "aliases": ["I", "معلومات", "info"]},
            "list": {"name": "قائمة", "desc": "يسرد جميع الحزم المثبتة.", "aliases": ["l", "قائمة", "list"]},
            "clean": {"name": "تنظيف", "desc": "ينظف ذاكرة التخزين المؤقت للحزم.", "aliases": ["c", "تنظيف", "clean"]},
            "orphans": {"name": "يتيم", "desc": "يدير الحزم اليتيمة.", "aliases": ["o", "يتيم", "orphans"]},
            "aur": {"name": "aur", "desc": "يدير حزم من Arch User Repository (AUR).", "aliases": ["a", "aur"]},
            "doctor": {"name": "فحص", "desc": "يقوم بفحص كامل لصحة النظام.", "aliases": ["d", "فحص", "doctor"]},
            "history": {"name": "سجل", "desc": "يعرض سجل الأوامر.", "aliases": ["h", "سجل", "history"]}
        }
    }
    ,    "es": {
        "description": "hpm: Un gestor de paquetes simple y potente para Arch Linux.",
        "usage": "Uso",
        "dry_run_warning": "Modo de prueba. No se realizarán cambios en el sistema.",
        "commands_title": "[bold blue]Comandos Disponibles[/bold blue]",
        "command_header": "Comando",
        "description_header": "Descripción",
        "global_options_title": "Opciones",
        "dry_run_help": "Muestra lo que se haría sin realizar cambios.",
        "lang_help": "Configura el idioma de la interfaz.",
        "help_help": "Muestra este mensaje y sale.",
        "command_aur_searching_helper": "Buscando asistente AUR...",
        "command_aur_error_no_helper_found": "No se encontró un asistente AUR (yay o paru).",
        "command_aur_helper_install_info": "Por favor, instala un asistente AUR para usar este comando.",
        "command_aur_using_helper": "Usando asistente AUR: {helper}",
        "command_aur_error_no_action_provided": "Por favor, proporciona una acción (por ejemplo: install, remove, etc.).",
        "command_aur_installing_packages": "Instalando paquete(s) AUR: {packages}",
        "command_aur_removing_packages": "Eliminando paquete(s) AUR: {packages}",
        "command_aur_searching_for_packages": "Buscando paquete(s): {packages}",
        "command_aur_upgrading_packages": "Actualizando paquetes...",
        "command_aur_error_unknown_action": "Error: Acción desconocida '{action}'.",
        "command_aur_error_no_package_provided": "Por favor, proporciona el nombre del paquete a instalar.",
        "command_aur_error_no_package_provided_remove": "Por favor, proporciona el nombre del paquete a eliminar.",
        "command_aur_error_no_search_term_provided": "Por favor, proporciona un término de búsqueda.",
        "dry_run_command_info": "El comando que se ejecutaría es: {command}",
        "operation_completed": "Operación completada con éxito.",
        "command_aur_error_helper_not_found": "Asistente AUR no encontrado. Este error no debería ocurrir.",
        "command_aur_error_unexpected_error": "Ocurrió un error inesperado: {error}",
        "commands": {
            "install": {"name": "instalar", "desc": "Instala uno o más paquetes.", "aliases": ["i", "instalar", "install"]},
            "remove": {"name": "eliminar", "desc": "Elimina un paquete.", "aliases": ["r", "eliminar", "remove"]},
            "upgrade": {"name": "actualizar", "desc": "Actualiza todos los paquetes instalados.", "aliases": ["u", "actualizar", "upgrade"]},
            "refresh": {"name": "sincronizar", "desc": "Sincroniza bases de datos y actualiza paquetes.", "aliases": ["s", "sincronizar", "refresh"]},
            "search": {"name": "buscar", "desc": "Busca paquetes.", "aliases": ["q", "buscar", "search"]},
            "info": {"name": "informacion", "desc": "Muestra información detallada del paquete.", "aliases": ["I", "informacion", "info"]},
            "list": {"name": "lista", "desc": "Lista todos los paquetes instalados.", "aliases": ["l", "lista", "list"]},
            "clean": {"name": "limpiar", "desc": "Limpia la caché de paquetes.", "aliases": ["c", "limpiar", "clean"]},
            "orphans": {"name": "huerfanos", "desc": "Gestiona paquetes huérfanos.", "aliases": ["o", "huerfanos", "orphans"]},
            "aur": {"name": "aur", "desc": "Gestiona paquetes del Arch User Repository (AUR).", "aliases": ["a", "aur"]},
            "doctor": {"name": "diagnostico", "desc": "Realiza una revisión completa del sistema.", "aliases": ["d", "diagnostico", "doctor"]},
            "history": {"name": "historial", "desc": "Muestra el historial de comandos.", "aliases": ["h", "historial", "history"]}
        }
    },
    "zh": {
        "description": "hpm: 一个简单且强大的 Arch Linux 软件包管理器。",
        "usage": "用法",
        "dry_run_warning": "模拟运行模式。系统不会进行任何更改。",
        "commands_title": "[bold blue]可用命令[/bold blue]",
        "command_header": "命令",
        "description_header": "描述",
        "global_options_title": "选项",
        "dry_run_help": "显示将要执行的操作，但不进行任何更改。",
        "lang_help": "设置界面语言。",
        "help_help": "显示此信息并退出。",
        "command_aur_searching_helper": "正在搜索 AUR 助手...",
        "command_aur_error_no_helper_found": "未找到 AUR 助手 (yay 或 paru)。",
        "command_aur_helper_install_info": "请安装 AUR 助手以使用此命令。",
        "command_aur_using_helper": "使用 AUR 助手: {helper}",
        "command_aur_error_no_action_provided": "请提供一个操作（例如: install, remove 等）。",
        "command_aur_installing_packages": "正在安装 AUR 包: {packages}",
        "command_aur_removing_packages": "正在移除 AUR 包: {packages}",
        "command_aur_searching_for_packages": "正在搜索包: {packages}",
        "command_aur_upgrading_packages": "正在升级软件包...",
        "command_aur_error_unknown_action": "错误: 未知操作 '{action}'。",
        "command_aur_error_no_package_provided": "请提供要安装的软件包名称。",
        "command_aur_error_no_package_provided_remove": "请提供要删除的软件包名称。",
        "command_aur_error_no_search_term_provided": "请提供搜索关键字。",
        "dry_run_command_info": "将执行的命令是: {command}",
        "operation_completed": "操作成功完成。",
        "command_aur_error_helper_not_found": "未找到 AUR 助手。此错误不应发生。",
        "command_aur_error_unexpected_error": "发生意外错误: {error}",
        "commands": {
            "install": {"name": "安装", "desc": "安装一个或多个软件包。", "aliases": ["i", "安装", "install"]},
            "remove": {"name": "卸载", "desc": "卸载软件包。", "aliases": ["r", "卸载", "remove"]},
            "upgrade": {"name": "升级", "desc": "升级所有已安装的软件包。", "aliases": ["u", "升级", "upgrade"]},
            "refresh": {"name": "刷新", "desc": "同步数据库并升级软件包。", "aliases": ["s", "刷新", "refresh"]},
            "search": {"name": "搜索", "desc": "搜索软件包。", "aliases": ["q", "搜索", "search"]},
            "info": {"name": "信息", "desc": "显示软件包的详细信息。", "aliases": ["I", "信息", "info"]},
            "list": {"name": "列表", "desc": "列出所有已安装的软件包。", "aliases": ["l", "列表", "list"]},
            "clean": {"name": "清理", "desc": "清理软件包缓存。", "aliases": ["c", "清理", "clean"]},
            "orphans": {"name": "孤儿", "desc": "管理孤立的软件包。", "aliases": ["o", "孤儿", "orphans"]},
            "aur": {"name": "aur", "desc": "管理 Arch User Repository (AUR) 的软件包。", "aliases": ["a", "aur"]},
            "doctor": {"name": "诊断", "desc": "执行系统健康检查。", "aliases": ["d", "诊断", "doctor"]},
            "history": {"name": "历史", "desc": "显示命令历史。", "aliases": ["h", "历史", "history"]}
        }
    }

}

def get_translation(lang: str):
    """Retrieves a translation getter function for a given language."""
    if lang not in LANGUAGES:
        lang = "en"
    
    translations = LANGUAGES[lang]
    def translate(key: str):
        if key in translations:
            return translations[key]
        return LANGUAGES["en"][key]
    
    return translate

def get_full_translation_dict(lang: str):
    """Retrieves the full translation dictionary for a given language."""
    return LANGUAGES.get(lang, LANGUAGES["en"])

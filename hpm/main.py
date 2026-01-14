# main.py

import sys
import typer
from hpm.cli import app as cli_app, print_custom_help, current_lang
from hpm.utils.early_args_patch import patch_args, CHAIN_CONNECTORS

def main():
    # تعريف كلمات المساعدة بكل اللغات بما فيها الصينية
    HELP_KEYWORDS = ["--help", "-h", "--مساعدة", "--ayuda", "--帮助"]
    
    # 1. تجميع كل كلمات الربط (ثم، then، luego، إلخ)
    all_connectors = []
    for connectors in CHAIN_CONNECTORS.values():
        all_connectors.extend(connectors)

    raw_args = sys.argv[1:]
    
    # 2. فحص المساعدة العامة قبل تقسيم الأوامر
    for arg in raw_args:
        if arg in HELP_KEYWORDS:
            if arg == "--مساعدة":
                print_custom_help("ar")
            elif arg == "--帮助":
                print_custom_help("zh")
            elif arg == "--ayuda":
                print_custom_help("es")
            else:
                detected = patch_args()
                print_custom_help(detected or "en")
            return

    # 3. تقسيم المدخلات لسلسلة أوامر
    commands_to_run = []
    current_chunk = []

    for arg in raw_args:
        if arg in all_connectors:
            if current_chunk:
                commands_to_run.append(current_chunk)
                current_chunk = []
        else:
            current_chunk.append(arg)
    
    if current_chunk:
        commands_to_run.append(current_chunk)

    # 4. تشغيل المساعدة الافتراضية لو لم يتم إدخال أي شيء
    if not commands_to_run:
        patch_args()
        cli_app()
        return

    # 5. تنفيذ سلسلة الأوامر
    for cmd_args in commands_to_run:
        sys.argv = [sys.argv[0]] + cmd_args
        
        # ترجمة الأمر الحالي وتحديد لغته
        detected_lang = patch_args()

        # فحص المساعدة داخل السلسلة
        if any(h in sys.argv for h in HELP_KEYWORDS):
            if "--مساعدة" in sys.argv:
                print_custom_help("ar")
            elif "--帮助" in sys.argv:
                print_custom_help("zh")
            elif "--ayuda" in sys.argv:
                print_custom_help("es")
            else:
                print_custom_help(detected_lang or "en")
            continue

        try:
            cli_app()
        except SystemExit as e:
            if e.code is not None and e.code != 0:
                sys.exit(e.code)
            continue

if __name__ == "__main__":
    main()

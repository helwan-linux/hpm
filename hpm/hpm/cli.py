# hpm/cli.py

import typer
from rich.console import Console
from rich.table import Table
from typing import List, Optional
from typing_extensions import Annotated
from hpm.commands import (
    install as install_cmd, remove as remove_cmd, upgrade as upgrade_cmd,
    search as search_cmd, clean as clean_cmd, info as info_cmd,
    list_command as list_cmd, refresh as refresh_cmd, orphans as orphans_cmd,
    aur as aur_cmd, doctor as doctor_cmd, history_command as history_cmd
)
from hpm.utils import log
from hpm.constants import BANNER_FILE
from hpm.i18n import LANGUAGES, get_translation

app = typer.Typer(
    name="hpm",
    help="hpm: a simple package manager frontend for Arch Linux."
)
console = Console()
current_lang = "en"

def print_banner():
    """Prints the application banner."""
    try:
        with open(BANNER_FILE, 'r', encoding='utf-8') as f:
            console.print(f.read(), style="bold cyan")
    except FileNotFoundError:
        log.warning("Banner file not found.")

def print_custom_help(lang: str):
    """Prints a custom help message in the specified language."""
    translate = get_translation(lang)
    console.print(f"[bold green]{translate('description')}[/bold green]")
    console.print("[dim]Version: 1.1.0 (Chained Commands Support)[/dim]")
    console.print(f"\n[bold]{translate('usage')}:[/b] hpm [COMMAND] [OPTIONS] [ARGS]...")

    # قسم شرح ميزة الربط
    chain_title = translate('chaining_title')
    console.print(f"\n[bold magenta]🔗 {chain_title}:[/bold magenta]")
    
    if lang == "ar":
        console.print("  يمكنك تشغيل عدة أوامر معاً باستخدام الرابط [bold cyan]'ثم'[/bold cyan]")
        console.print("  [dim]مثال: hpm تحديث ثم فحص ثم تنظيف[/dim]")
    elif lang == "es":
        console.print("  Puedes ejecutar varios comandos usando [bold cyan]'luego'[/bold cyan]")
        console.print("  [dim]Ejemplo: hpm actualizar luego diagnostico[/dim]")
    elif lang == "zh":
        console.print("  你可以使用 [bold cyan]'然后'[/bold cyan] 同时运行多个命令")
        console.print("  [dim]例子: hpm 刷新 然后 诊断 然后 清理[/dim]")
    else:
        console.print("  You can run multiple commands using [bold cyan]'then'[/bold cyan]")
        console.print("  [dim]Example: hpm refresh then doctor then clean[/dim]")

    table = Table(
        title=f"\n{translate('commands_title')}",
        show_header=True,
        header_style="bold magenta",
        title_justify="left",
    )
    table.add_column(translate("command_header"), style="bold cyan", no_wrap=True)
    table.add_column(translate("description_header"), style="white", overflow="fold")
    table.add_column("Key Options", style="yellow", overflow="fold")

    commands = translate('commands')
    
    # صفوف الجدول كاملة كما في ملفك الأصلي
    table.add_row(f"{commands['install']['name']} ({'|'.join(commands['install']['aliases'])})", commands['install']['desc'], "**--local (-l) : Install from a local file.**\n--force (-f) : Bypass confirmations.")
    table.add_row(f"{commands['remove']['name']} ({'|'.join(commands['remove']['aliases'])})", commands['remove']['desc'], "--force (-f) : Bypass confirmations.")
    table.add_row(f"{commands['upgrade']['name']} ({'|'.join(commands['upgrade']['aliases'])})", commands['upgrade']['desc'], "--force (-f) : Bypass confirmations.")
    table.add_row(f"{commands['refresh']['name']} ({'|'.join(commands['refresh']['aliases'])})", commands['refresh']['desc'], "--force (-f) : Bypass confirmations.")
    table.add_row(f"{commands['search']['name']} ({'|'.join(commands['search']['aliases'])})", commands['search']['desc'], "")
    table.add_row(f"{commands['info']['name']} ({'|'.join(commands['info']['aliases'])})", commands['info']['desc'], "")
    table.add_row(f"{commands['list']['name']} ({'|'.join(commands['list']['aliases'])})", commands['list']['desc'], "")
    table.add_row(f"{commands['clean']['name']} ({'|'.join(commands['clean']['aliases'])})", commands['clean']['desc'], "--all (-a) : Remove all cache files.")
    table.add_row(f"{commands['orphans']['name']} ({'|'.join(commands['orphans']['aliases'])})", commands['orphans']['desc'], "remove : Removes all orphan packages.")
    table.add_row(f"{commands['aur']['name']} ({'|'.join(commands['aur']['aliases'])})", commands['aur']['desc'], "")
    table.add_row(f"{commands['doctor']['name']} ({'|'.join(commands['doctor']['aliases'])})", commands['doctor']['desc'], "")
    table.add_row(f"{commands['history']['name']} ({'|'.join(commands['history']['aliases'])})", commands['history']['desc'], "")

    console.print(table)
    
    # تحديد خيار المساعدة بناءً على اللغة لمنع التخلف
    help_option = "--help"
    if lang == "ar": help_option = "--مساعدة"
    elif lang == "zh": help_option = "--帮助"
    elif lang == "es": help_option = "--ayuda"

    console.print(f"\n[bold]{translate('global_options_title')}:[/b]")
    console.print(f"  [cyan]--dry-run, -d[/cyan] : {translate('dry_run_help')}")
    #console.print(f"  [cyan]--lang[/cyan] : {translate('lang_help')}")
    console.print(f"  [cyan]--version[/cyan] : Show version info")
    console.print(f"  [cyan]{help_option}[/cyan] : {translate('help_help')}")

@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    version: Annotated[bool, typer.Option("--version", help="Show version")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", "-d", help="Show what would be done")] = False,
    lang: Annotated[Optional[str], typer.Option("--lang", help="Set language")] = None,
):
    global current_lang
    if lang and lang in LANGUAGES:
        current_lang = lang
    
    if version:
        console.print("[bold cyan]HPM Version: 1.1.0[/bold cyan]")
        console.print("[dim]Chained Commands & Multi-language Support Enabled.[/dim]")
        raise typer.Exit()

    ctx.obj = {"dry_run": dry_run, "lang": current_lang}
    print_banner()

    translate = get_translation(current_lang)
    if dry_run:
        log.warning(translate("dry_run_warning"))

    if ctx.invoked_subcommand is None:
        print_custom_help(current_lang)
        raise typer.Exit()

@app.command(name="install", help="Installs one or more packages.")
@app.command(name="i", help="Installs one or more packages.")
def install_command(
    ctx: typer.Context,
    packages: Annotated[List[str], typer.Argument(..., help="The package(s) to install.")],
    force: bool = typer.Option(False, "--force", "-f", help="Bypass safety checks and confirmations."),
    local: bool = typer.Option(False, "--local", "-l", help="Installs a package from a local file.")
):
    dry_run = ctx.obj.get("dry_run", False)
    install_cmd.install_main(packages, force, local, dry_run)

@app.command(name="remove", help="Removes a package.")
@app.command(name="r", help="Removes a package.")
def remove_command(
    ctx: typer.Context,
    packages: Annotated[List[str], typer.Argument(..., help="The package(s) to remove.")],
    force: bool = typer.Option(False, "--force", "-f", help="Bypass safety checks and confirmations.")
):
    dry_run = ctx.obj.get("dry_run", False)
    remove_cmd.remove_main(packages, force, dry_run)
    
@app.command(name="search", help="Searches for packages.")
@app.command(name="q", help="Searches for packages.")
def search_command(
    ctx: typer.Context,
    packages: Annotated[List[str], typer.Argument(help="Name of the package to search.")]
):
    dry_run = ctx.obj.get("dry_run", False)
    search_cmd.search_main(packages, dry_run)

@app.command(name="info", help="Displays detailed information about a package.")
@app.command(name="I", help="Displays detailed information about a package.")
def info_command(
    ctx: typer.Context,
    packages: Annotated[List[str], typer.Argument(help="Name of the package(s) to show info.")]
):
    dry_run = ctx.obj.get("dry_run", False)
    info_cmd.info_main(packages, dry_run)
    
@app.command(name="refresh", help="Synchronizes databases and upgrades all installed packages.")
@app.command(name="s", help="Synchronizes databases and upgrades all installed packages.")
def refresh_command(
    ctx: typer.Context,
    force: Annotated[bool, typer.Option("--force", "-f", help="Bypass safety checks and confirmations.")] = False
):
    dry_run = ctx.obj.get("dry_run", False)
    refresh_cmd.refresh_main(force, dry_run)
    
@app.command(name="upgrade", help="Upgrades all installed packages.")
@app.command(name="u", help="Upgrades all installed packages.")
def upgrade_command(
    ctx: typer.Context,
    force: Annotated[bool, typer.Option("--force", "-f", help="Bypass safety checks and confirmations.")] = False
):
    dry_run = ctx.obj.get("dry_run", False)
    upgrade_cmd.upgrade_main(force, dry_run)
    
@app.command(name="clean", help="Cleans the package cache.")
@app.command(name="c", help="Cleans the package cache.")
def clean_command(
    ctx: typer.Context,
    all_cache: Annotated[bool, typer.Option("--all", "-a", help="Remove all cache files.")] = False
):
    dry_run = ctx.obj.get("dry_run", False)
    clean_cmd.clean_main(all_cache, dry_run)

@app.command(name="list", help="Lists all installed packages.")
@app.command(name="l", help="Lists all installed packages.")
def list_command(ctx: typer.Context):
    dry_run = ctx.obj.get("dry_run", False)
    list_cmd.list_main(dry_run)
    
@app.command(name="orphans", help="Manages orphan packages.")
@app.command(name="o", help="Manages orphan packages.")
def orphans_command(
    ctx: typer.Context,
    remove: Annotated[bool, typer.Option("--remove", "-r", help="Removes all orphan packages.")] = False
):
    dry_run = ctx.obj.get("dry_run", False)
    orphans_cmd.orphans_main(remove, dry_run)
    
@app.command(name="aur", help="Manages packages from the Arch User Repository (AUR).")
@app.command(name="a", help="Manages packages from the Arch User Repository (AUR).")
def aur_command(
    ctx: typer.Context,
    packages: Annotated[List[str], typer.Argument(help="The package(s) to manage.")]
):
    dry_run = ctx.obj.get("dry_run", False)
    aur_cmd.aur_main(packages, dry_run)
    
@app.command(name="doctor", help="Performs a complete system health check.")
@app.command(name="d", help="Performs a complete system health check.")
def doctor_command(ctx: typer.Context):
    dry_run = ctx.obj.get("dry_run", False)
    doctor_cmd.doctor_main(dry_run)

@app.command(name="history", help="Displays command history.")
@app.command(name="h", help="Displays command history.")
def history_command(ctx: typer.Context):
    dry_run = ctx.obj.get("dry_run", False)
    history_cmd.history_main(dry_run)

if __name__ == "__main__":
    app()

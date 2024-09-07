"""Generate a report of dotfiles not reported by xdg-ninja."""

import os

from rich.console import Console
from rich.table import Table
from string_grab import grab_all


def get_dotfiles_list() -> list:
    """
    Get a list of dotfiles in the user's $HOME directory.

    Returns:
        list: A list containing the names of dotfiles in the $HOME directory.
    """
    home_directory = os.path.expanduser("~")
    dotfiles_list = [
        item for item in os.listdir(home_directory) if item.startswith(".")
    ]
    return dotfiles_list


def read_xdg_ninja_report(report_path: str) -> list:
    """
    Read the xdg-ninja report and extract the reported files.

    Args:
        report_path (str): The path to the xdg-ninja report file.

    Returns:
        list: A list containing the reported files from the xdg-ninja report.
    """
    with open(report_path, "r") as report_file:
        content = report_file.read()

        xdg_ninja_report_1 = list(grab_all(content, start="$HOME/", end="[0m\n"))
        xdg_ninja_report_2 = list(grab_all(content, start="${HOME}/", end="[0m\n"))

    return xdg_ninja_report_1 + xdg_ninja_report_2


def cross_match(list1: list, list2: list) -> list:
    """
    Perform a cross-match between two lists and return the elements present in list1 but not in list2.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: The elements present in list1 but not in list2.
    """
    return list(set(list1) - set(list2))


def compare_with_xdg_ninja(dotfiles_list: list, xdg_ninja_report: list) -> list:
    """
    Compare the list of dotfiles with the xdg-ninja report and find unreported files.

    Args:
        dotfiles_list (list): The list of dotfiles in the user's $HOME directory.
        xdg_ninja_report (list): The reported files from the xdg-ninja report.

    Returns:
        list: A list of dotfiles that are not reported by xdg-ninja.
    """
    accepted_dots = {".config", ".cache", ".local"}
    not_reported_files = list(
        set(dotfiles_list) - accepted_dots - set(xdg_ninja_report)
    )
    return not_reported_files


def get_type_format(file_path: str) -> str:
    """
    Return the type of file as a formatted string.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The type of file as a formatted string.
    """
    if os.path.islink(file_path):
        return "[bold yellow][Symlink][/]"
    elif os.path.isfile(file_path):
        return "[bold green][File][/]"
    elif os.path.isdir(file_path):
        return "[bold blue][Folder][/]"
    else:
        return "[bold red][Unknown][/]"


def print_not_reported_files(not_reported_files: list) -> None:
    """
    Print the list of files not reported by xdg-ninja in a formatted table.

    Args:
        not_reported_files (list): A list of dotfiles that are not reported by
            xdg-ninja.

    Returns:
        None
    """
    if not not_reported_files:
        print("[green]All dotfiles are reported by xdg-ninja.[/green]")
        return

    console = Console()
    table = Table(show_header=True, header_style="bold white on blue")
    table.add_column("File/Folder", style="dim", width=35)
    table.add_column("Type", style="dim", width=10)

    for file in sorted(not_reported_files):
        file_type = get_type_format(os.path.join(os.path.expanduser("~"), file))
        table.add_row(file, file_type)

    console.print("\n[yellow]Files/Folders not reported by xdg-ninja:[/yellow]")
    console.print(table)

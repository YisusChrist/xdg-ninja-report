"""Main module for xdg_ninja_report package."""

from rich import print

from xdg_ninja_report.cli import get_parsed_args, parser_error
from xdg_ninja_report.report import (compare_with_xdg_ninja, get_dotfiles_list,
                                     print_not_reported_files,
                                     read_xdg_ninja_report)


def main() -> None:
    global parser

    args = get_parsed_args()

    if not args.report_file:
        parser_error("No report file specified")
        return

    xdg_ninja_report_path = args.report_file
    print(f"Reading xdg-ninja report from '{xdg_ninja_report_path}'")

    dotfiles_list = get_dotfiles_list()
    xdg_ninja_report = read_xdg_ninja_report(xdg_ninja_report_path)
    not_reported_files = compare_with_xdg_ninja(dotfiles_list, xdg_ninja_report)

    print_not_reported_files(not_reported_files)


if __name__ == "__main__":
    main()

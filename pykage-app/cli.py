from os import getcwd
from .packaging import CreatePackage


try:
    import click
    import colorama as color
    from colorama import Fore
except ImportError as import_error:
    raise ImportError("There was an error during import process.")


color.init(autoreset=True)

@click.command()
@click.argument("name", type=click.STRING, required=True)
@click.option("-d", "--dir",
                is_flag=False,
                flag_value=getcwd(),
                default=getcwd(),
                help="The directory in wich the package should be created.",
                type=click.Path(exists=True))
def main(name, dir):
    new_package = CreatePackage(name, dir)
    new_package.create_package()
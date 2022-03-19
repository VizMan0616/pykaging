try:
    import click
    import colorama as color
    from colorama import Fore
except ImportError as import_error:
    print(f"There was a error during module import:\n {import_error}")

color.init(autoreset=True)

def main():
    pass
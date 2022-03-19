from datetime import date
from os import getcwd, mkdir, getenv
from os.path import (
                abspath, 
                relpath, 
                join
            )
from typing import Optional


class CreatePackage:
    """
    
    """
    
    def __init__(self, package_name:str, dir:Optional[str]) -> None:
        self.package_name = package_name
        self.created_date = date.today()
        self.abs_dir = getcwd() or abspath(dir)
        self.abs_init_dir = ""
        self._rel_dir = relpath(getcwd()) or dir
        self._rel_init_dir = ""

    def create_package(self):
        new_package_route = join(self._rel_dir, self.package_name)
        mkdir(new_package_route)
        self.abs_init_dir = join(abspath(new_package_route), "__init__.py")
        self._rel_init_dir = join(new_package_route, "__init__.py")

        self._create_init_file(True)

    def _create_init_file(self, is_package_created:bool) -> None:
        """Creates an init file if the package is creatd
        so python can recognize it as it.
        """
        
        template_str = f"""# {self.package_name.upper()} package created at {self.created_date.strftime("%m/%d/%Y")}\n         
        # by {getenv("USER").upper()}.\n
        # \n
        # PYKAGE and all it's feature is a software under the MIT License.
        """

        if is_package_created:
            with open(self._rel_init_dir, "w+") as init_file:
                init_file.write(template_str)

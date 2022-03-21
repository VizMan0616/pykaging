from datetime import date
from os import getenv
from os.path import abspath
import sys
from pathlib import Path
from typing import Optional


class CreatePackage:
    """Package class designed for handling basic and common
    attributes associated with diretories and naming.
    -------------------------------------------------------
    Attrs:\n
    package_name[str] - The name used to create the package.\n
    dir [str] - Directory where the package should be created.
    """
    
    def __init__(self, package_name:str, dir:str) -> None:
        self.package_name = package_name
        self.created_date = date.today()
        self.abs_dir = Path(abspath(dir))
        self.abs_init_dir = None

    def create_package(self):
        """It creates a handly method to create python
            packages.
        """

        # npr stands for "new package route 
        # (Yeah i'm lazy with long names) don't bother me.
        npr = self.abs_dir / self.package_name
        
        try:
            npr.mkdir()
        except FileNotFoundError as dir_error:
            raise FileNotFoundError("There was an error during package creation process")
        
        self.abs_init_dir = npr / "__init__.py"
        self._create_init_file(True)

    def _create_init_file(self, is_package_created:bool) -> None:
        """Creates an init file if the package is creatd
        so python can recognize it as it.
        """
        if sys.platform == "linux":
            os_name = getenv("USER")
        elif sys.platform == "win32":
            os_name = getenv("USERNAME")

        template_str = f"""# '{self.package_name}' package created at {self.created_date.strftime("%m/%d/%Y")} by {os_name}.
# 
# Pykaging is created by José Vizcaya. This software is running
# under the MIT License.
# 
# To see more about please refer to https://github.com/VizMan0616/pykaging
"""

        if is_package_created:
            with self.abs_init_dir.open(mode="w") as init_file:
                init_file.write(template_str)    

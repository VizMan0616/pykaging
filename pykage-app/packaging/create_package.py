from datetime import date
from os import getcwd, getenv
from os.path import abspath
from pathlib import Path
from typing import Optional


class CreatePackage:
    """Package class designed for handling basic and common
    attributes associated with diretories and naming.
    -------------------------------------------------------
    Attrs:
        package_name[str] - The name used to create the package.
        dir [str] - Optional argument, if provided i will create
    """
    
    def __init__(self, package_name:str, dir:Optional[str]) -> None:
        self.package_name = package_name
        self.created_date = date.today()
        self.abs_dir = Path(getcwd() or abspath(dir))
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
        
        template_str = f"""# {self.package_name.upper()} package created at {self.created_date.strftime("%m/%d/%Y")}\n         
        # by {getenv("USER").upper()}.\n
        # \n
        # PYKAGE is created by Jos'e Vizcaya. All features is a software running under the MIT License.\n
        # To see more about please refer to [GitHub link]
        """

        if is_package_created:
            with self.abs_init_dir.open(mode="w") as init_file:
                init_file.write(template_str)    

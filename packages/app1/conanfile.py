from conan import ConanFile
from conan.tools.files import copy
from pathlib import Path

class myConanClass(ConanFile):
    name = "app1"
    python_requires = "conan2_base_recipes/2.5.0"
    python_requires_extend = "conan2_base_recipes.Conan2BaseClass"
    version = "0.2.0"

    def package(self):
        copy(self, "*.h", dst=Path(self.package_folder)/"include", src=Path(self.build_folder)/"src")


from conan import ConanFile

class myConanClass(ConanFile):
    name = "my_conan_package"
    python_requires = "conan2_base_recipes/2.4.1"
    python_requires_extend = "conan2_base_recipes.Conan2BaseClass"
    version = "0.1.1"
    settings = ["os"]

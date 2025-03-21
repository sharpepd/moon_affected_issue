from conan import ConanFile

class myConanClass(ConanFile):
    name = "my_conan_package"
    python_requires = "conan2_base_recipes/1.1.2"
    python_requires_extend = "conan2_base_recipes.Conan2BaseClass"

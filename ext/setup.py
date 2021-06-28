
from distutils.core import Extension, setup
from Cython.Build import cythonize
import os

if __name__ == '__main__':
    os.environ['CFLAGS'] = "-march='native' -ffast-math -flto"

    setup(
        ext_modules = cythonize(
            Extension(name="hello", sources=[f"{os.getcwd()}/hello.pyx"]),
            compiler_directives = {'language_level': 3, 'infer_types': True}
        )
    )

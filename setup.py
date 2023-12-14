"""Setup.py for Pypi.org"""
import os
from distutils.core import setup
from setuptools import find_packages


if os.environ.get("OBFUSCATE", "0") == "1":
    import package_obfuscator

    print("Obfuscating package...")
    package_obfuscator.obfuscate("src", output="foolproof", force_output_overwrite=True)


setup(
    name="foolproof",
    packages=find_packages(include=["foolproof", "foolproof.*"]),
    include_package_data=True,
    package_data={
        "": ["*.pyc"],
        "foolproof": ["__custom_pycache__/*.pyc"],
    },
    version="0.1.8",
    description="Find all exceptions that your code and its dependencies can raise, to make your work foolproof!",
    author="Nicolas Micaux",
    author_email="micaux.nicolas@gmail.com",
    url="https://github.com/NicolasMICAUX/foolproof",
    install_requires=[],
    keywords=["exception", "foolproof"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.5",
    # Set README.md as description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)

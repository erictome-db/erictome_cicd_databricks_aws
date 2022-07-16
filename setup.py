from setuptools import find_packages, setup
from erictome_cicd_databricks_aws import __version__

setup(
    name="erictome_cicd_databricks_aws",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in new_hrms/__init__.py
from new_hrms import __version__ as version

setup(
	name="new_hrms",
	version=version,
	description="Hr and Payroll",
	author="admin",
	author_email="admin@10decoders.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

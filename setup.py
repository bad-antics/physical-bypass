from setuptools import setup,find_packages
setup(name="physical-bypass",version="2.0.0",author="bad-antics",description="Physical security bypass research and testing",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")

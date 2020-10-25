
from rj_ml_utils.package import details as pkg
import setuptools

print(pkg.include_package_data[0])
setuptools.setup(
    name=pkg.name, # Replace with your own username
    version=pkg.version,
    author=pkg.author,
    author_email=pkg.author_email,
    description=pkg.description,
    long_description=pkg.long_description,
    long_description_content_type=pkg.long_description_content_type,
    url=pkg.url,
    packages=setuptools.find_packages(),
    classifiers=pkg.classifiers,
    python_requires=pkg.python_requires,
    include_package_data=pkg.include_package_data[0],
    install_requires=pkg.install_requires
)
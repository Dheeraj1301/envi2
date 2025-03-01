import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "COVID-19-Severity-Prediction"
AUTHOR_USER_NAME = "Dheeraj1301"  # Replace with your GitHub username
SRC_REPO = "covid_severity_classifier"
AUTHOR_EMAIL = "dheeraj130105@gmail.com"  # Replace with your email

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for COVID-19 severity classification using CNN",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Dheeraj1301/envi2.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Dheeraj1301/envi2.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

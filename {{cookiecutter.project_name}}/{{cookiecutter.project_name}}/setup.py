
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

TESTS_REQUIRE = ["selenium~=3.141", "pylint", "mock", "black", "bandit"]

setup(
    name="{{ cookiecutter.package_name }}",
    description="{{ cookiecutter.short_description }}",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.author_name }}",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "webviz_config_containers": [
            "SomeCustomContainer = {{cookiecutter.package_name}}.containers:SomeCustomContainer",
            "SomeOtherCustomContainer = {{cookiecutter.package_name}}.containers:SomeOtherCustomContainer",
        ]
    },
    install_requires=[
        "webviz-config>=0.0.24",
    ],
    tests_require=TESTS_REQUIRE,
    extras_require={"tests": TESTS_REQUIRE},
    setup_requires=["setuptools_scm~=3.2"],
    use_scm_version=True,
    zip_safe=False,
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)

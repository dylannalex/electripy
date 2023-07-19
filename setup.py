from distutils.core import setup


setup(
    name="electripy",
    packages=["electripy", "electripy.physics", "electripy.visualization"],
    version="0.1.0",
    license="MIT",
    description="Learn electrostatics by playing around with electrons and protons",
    author="Dylan Tintenfich",
    author_email="tintenfichdylan05@gmail.com",
    url="https://github.com/dylannalex/electripy",
    keywords=[
        "electrostatics", "simulation", "physics"
    ],
    install_requires=[
        "numpy>=1.0.0",
        "pygame>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    package_data={"electripy.visualization": ["sounds/add_charge.wav"]},
)

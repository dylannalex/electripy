from distutils.core import setup


setup(
    name="electripy",
    packages=["electripy", "electripy.physics", "electripy.visualization"],
    version="0.0.4.2",
    license="MIT",
    description="Learn electrostatics by playing around with electrons and protons",
    author="Dylan Tintenfich",
    author_email="tintenfichdylan05@gmail.com",
    url="https://github.com/dylannalex/electripy",
    keywords=[
        "electricity",
    ],
    install_requires=[
        "numpy==1.21.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    package_data={"electripy.visualization": ["sounds/add_charge.wav"]},
)

from setuptools import setup

setup(
    name="brutto_netto_rechner",
    version="1.0",
    py_modules=["main", "lst2025"],
    install_requires=[
        "PyQt6",
        "fpdf"
    ],
    entry_points={
        "console_scripts": [
            "brutto-netto = main:main"
        ]
    }
)

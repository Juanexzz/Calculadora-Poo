from setuptools import setup
setup(
    name="cli_calculator",
    version="0.1",
    packages=["calculadora", "tests"],
    install_requieres=[
        "click"
    ],
    entry_points='''
      [console_scripts]
      calc=calculadora.cli:calc
    '''

)

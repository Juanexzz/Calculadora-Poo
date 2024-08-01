from setuptools import setup
setup(
    name="cli_calculator",
    version="0.1",
    packages=["calculator", "tests"],
    install_requieres=[
        "click"
    ],
    entry_point='''
      [console_scripts]
      calc=calculator.cli:calc
    '''

)

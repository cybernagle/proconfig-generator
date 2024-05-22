from setuptools import setup, find_packages

setup(
    name='proconfig',
    version='0.1.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        "tabulate",
        "termcolor",
        "jsonschema",
        "click",
        "dash",
        "dash_cytoscape",
    ],
    entry_points='''
        [console_scripts]
        pcc=proconfig.cli:cli
    ''',
    author='cybernagle',
    author_email='zhang.nagle@gmail.com',
    description='A CLI tool for simplify MyShell PorConfig programming.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cybernagle/proconfig-generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

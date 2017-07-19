from setuptools import setup

setup(
    name='jkconnect_monitor',
    packages=['jkconnect_monitor'],
    version='0.0.1',
    description='A tshark wrapper to count the number of cellphones in the vicinity',
    author='krishnan',
    url='https://github.com/krishnanmuthaiahpillai/jkconnect_monitor',
    author_email='krishnanmuthaiahpillai@gmail.com',
    download_url='https://github.com/krishnanmuthaiahpillai/jkconnect_monitor/archive/v2.0.tar.gz',
    keywords=['tshark', 'wifi', 'location'],
    classifiers=[],
    install_requires=[
        "click",
        "netifaces",
        "pick",
    ],
    setup_requires=[],
    tests_require=[],
    entry_points={'console_scripts': [
        'jkconnect_monitor = jkconnect_monitor.__main__:main',
    ], },
)

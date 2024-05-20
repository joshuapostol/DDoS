from setuptools import setup, find_packages

setup(
    name="DDoS",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    entry_points={
        "console_scripts": [
            "ddos_test=ddos_attack:run",
        ],
    },
    python_requires='>=3.6',
    description="this is a powerfull ddos tools but do not attack any gov or edu website",
    author="joshua Apostol",
    author_email="joshuaapostol909@gmail.com",
    url="https://github.com/Justerw/DDoS",
)

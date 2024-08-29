from setuptools import setup, find_packages

setup(
    name='rehttp',  # Имя вашей библиотеки
    version='0.1.0',  # Версия
    packages=find_packages(),
    author='anoniszmuss',
    author_email='thisanot@example.com',
    description='Почини запор пистолетом',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/onenonelynonely/rehttp',  # URL репозитория
    install_requires=[
        'requests',  # Зависимость (requests)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
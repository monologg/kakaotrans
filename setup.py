from setuptools import setup, find_packages

setup(
    name='kakaotrans',
    version='0.1.2',
    url='https://github.com/monologg/kakaotrans',
    license='MIT',
    author='Jangwon Park',
    author_email='adieujw@gmail.com',
    description='[Unofficial] Kakaotrans: Kakao translate API for python',
    packages=find_packages(exclude=[]),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)

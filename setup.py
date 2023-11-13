from setuptools import setup, find_packages

setup(
    name='dsss_math_quiz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = dsss_math_quiz.module:main',
        ],
    },
)

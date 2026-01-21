from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='git-smart-commit',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Intelligent Git commit message generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/git-smart-commit',
    py_modules=['git_smart_commit'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'git-smart-commit=git_smart_commit:main',
            'gsc=git_smart_commit:main',
        ],
    },
    keywords='git commit conventional-commits automation developer-tools',
    project_urls={
        'Bug Reports': 'https://github.com/YOUR_USERNAME/git-smart-commit/issues',
        'Source': 'https://github.com/YOUR_USERNAME/git-smart-commit',
    },
)

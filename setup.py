from setuptools import setup, find_packages

with open('./readme.md') as f:
    long_description = f.read()

setup(
    name='django_doc_view',
    version='0.1.2',
    keywords=('django', 'api', 'view', 'document', 'doc'),
    description='The simplest way to document your Django APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',  # https://packaging.python.org/tutorials/distributing-packages/#description
    author='Ocavue',
    author_email='ocavue@gmail.conm',
    url='https://github.com/ocavue/django-doc-view',
    license='MIT License',
    packages=find_packages(),
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta', 'Programming Language :: Python :: 3'
    ],
)

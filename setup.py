from setuptools import setup
from setuptools.extension import Extension

setup(
    author="Taylor Jung",
    author_email="iam@nyanye.com",
    name='goorm',
    version='0.1.1',
    url='https://github.com/nyanye/Goorm',
    description='Python package for Korean wordcloud generation with morphological analysis',
    license='MIT',
    install_requires=['matplotlib', 'numpy', 'Pillow'],
    ext_modules=[Extension("goorm.query_integral_image",
                           ["goorm/query_integral_image.c"])],
    scripts=['goorm/wordcloud_cli.py'],
    packages=['goorm'],
    package_data={'goorm': [
        'fonts/*.ttf',
        'tag/*/*/*/*'
        ]}
)

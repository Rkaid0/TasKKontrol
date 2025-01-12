from distutils.core import setup

with open("README.md", 'r') as file:
    longDiscription = file.read() 

setup(
  name = 'TasKKontrol',
  packages = ['TasKKontrol'],
  version = '0.1.1-alpha',
  license='MIT',
  description = 'Task automation library',
  long_description_content_type = "text/markdown",
  long_description = longDiscription,
  author = 'Artyom Yesayan',
  author_email = 'yesart8@gmail.com',
  url = 'https://github.com/Rkaid0/TasKKontrol',
  keywords = ['Workflow', 'Automation', 'Task'],
  install_requires=[],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)

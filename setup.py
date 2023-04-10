from setuptools import setup, find_packages

setup(
    name='dougs_noti',
    version='0.3.6',
    description='notify the user thorough email or text message ',
    author='Doug Kim',
    author_email='slakingex@gmail.com',
    url='https://github.com/dougieduk/dougs_noti',
    packages=find_packages(),
    install_requires=[
        'twilio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

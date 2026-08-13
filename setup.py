from setuptools import setup, find_packages

setup(
    name='Sublist3r',
    version='1.0',
    python_requires='>=2.7',
    install_requires=['dnspython', 'requests', 'argparse; python_version==\'2.7\''],
    packages=find_packages()+['.'],
    include_package_data=True,
    url='https://github.com/reapersapprentice/Sublist3r-macOS',
    license='GPL-2.0',
    description='Fast subdomain enumeration tool for macOS — Apple Silicon & Intel native',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Security',
    ],
    keywords='subdomain dns enumeration macos apple-silicon osint reconnaissance penetration-testing cybersecurity bug-bounty',
    entry_points={
        'console_scripts': [
            'sublist3r = sublist3r:interactive',
        ],
    },
)

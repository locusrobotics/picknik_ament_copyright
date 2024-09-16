from setuptools import find_packages
from setuptools import setup

package_name = 'locus_ament_copyright'

setup(
    name=package_name,
    version='0.3.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    package_data={'': [
        'template/*',
    ]},
    zip_safe=False,
    url='https://github.com/locusrobotics/locus_ament_copyright',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Check source files for Locus Robotics-specific copyright reference.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'ament_copyright.copyright_name': [
            'locus = locus_ament_copyright.copyright_names:locus',
        ],
        'ament_copyright.license': [
            'locus_proprietary = locus_ament_copyright.licenses:locus_proprietary',
        ],
    },
)

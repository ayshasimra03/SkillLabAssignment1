from setuptools import find_packages, setup

package_name = 'assignment1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
     ('share/ament_index/resource_index/packages',
       ['resource/' + package_name]),

     ('share/' + package_name,
       ['package.xml']),

     ('share/' + package_name + '/launch',
       ['launch/display.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='shimaazssheikh14@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pub = assignment1.pub:main',
            'sub = assignment1.sub:main',
        ],
    },
)

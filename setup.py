from setuptools import setup

package_name = 'turtle_bot_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Raempest',
    maintainer_email='thehuman130410@gmail.com',
    description='Simple ROS2 node for turtle bot movement control',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_controller = turtle_bot_control.turtle_bot_control:main',
        ],
    },
)
   

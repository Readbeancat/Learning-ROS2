import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/admin/Documents/ROS2/C4.1/install/demo_python_service'

import os
from common import util

# path of path.py
path_dir = os.path.abspath(__file__)

# path of directory config
config_dir = os.path.dirname(path_dir)

# path of project
project_dir = os.path.dirname(config_dir)

# path of directory data
data_dir = os.path.join(project_dir, 'data')

# path of test_data.yaml
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
test_data_dir = os.path.join(data_dir, 'test_data.yaml')

# path of directory output
output_dir = os.path.join(project_dir, 'output')

# path of directory img
img_dir = os.path.join(output_dir, 'img')

# path of directory log
log_dir = os.path.join(output_dir, 'log')
log_name = "mylog_" + util.current_time() + ".log"
log_file = os.path.join(log_dir, log_name)

# path of directory report
report_path = os.path.join(output_dir, 'report')

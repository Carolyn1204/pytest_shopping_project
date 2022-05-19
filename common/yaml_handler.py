import yaml
from config.path import test_data_dir


def read_yaml(fpath):
    with open(fpath) as f:
        data = yaml.safe_load(f)
        return data


yaml_data = read_yaml(test_data_dir)

if __name__ == '__main__':
    print(yaml_data['gift_message'])

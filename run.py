import os
from time import sleep
from common.send_email import SendEmail

import pytest


def run():
    os.system('pytest -s ./testcases/  --alluredir=./output/report_jason')
    os.system('allure generate ./output/report_jason -o ./output/report --clean')
    # pytest.main(["./testcases/test_01place_order.py"])
    # os.system('pytest -s ./testcases/test_01place_order.py  --alluredir=./output/report_jason')
    # os.system('allure serve ./output/report_jason')
    sleep(3)
    sm = SendEmail()
    sm.send_report()


if __name__ == '__main__':
    run()

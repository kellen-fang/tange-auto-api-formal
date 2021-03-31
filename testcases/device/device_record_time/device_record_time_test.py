# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/device/device_record_time/device_record_time.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDeviceRecordTime(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters({"status_code-ok-status-code-data": [[200, 1, "ok", 200, 0]]}),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("获取当前服务器时间").base_url("${ENV(DV_test_url)}")

    teststeps = [
        Step(
            RunRequest("获取当前服务器时间")
            .post("device/record/time")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(None)
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data", "$data")
        ),
    ]


if __name__ == "__main__":
    TestCaseDeviceRecordTime().test_start()

# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/device/device_auth_active/device_auth_active.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDeviceAuthActive(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "uuid-actived": "${parameterize(test_data/normal_device_data.csv)}",
                "status_code-ok-status-code-data": [
                    [200, 1, "ok", 200, "active success"]
                ],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("tange-iiCam365 激活设备").base_url("${ENV(DV_test_url)}")

    teststeps = [
        Step(
            RunRequest("激活设备")
            .post("device/auth/active")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({"uuid": "$uuid", "actived": "$actived"})
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_equal("body.data", "$data")
        ),
    ]


if __name__ == "__main__":
    TestCaseDeviceAuthActive().test_start()

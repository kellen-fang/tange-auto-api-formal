# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_device_list_least/app_device_list_least.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseAppDeviceListLeast(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids-device_ids": [
                    [200, 1, "ok", 200, 0, "0"]
                ],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("app/device/list/least")
        .base_url("${ENV(api_url)}")
        .export(*["token", "id", "device_id", "uuid"])
    )

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("查询设备信息：ID， 名称，uuid")
            .post("http://static-cn01.tange365.com/app/device/list/least")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "token": "$token",
                    "pkgname": "$pkgname",
                    "version": "$version",
                    "platform": "$platform",
                    "language": "$language",
                    "user_id": "$id",
                }
            )
            .extract()
            .with_jmespath("body.data[0].device_id", "device_id")
            .with_jmespath("body.data[0].uuid", "uuid")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data[0].device_id", "$device_ids")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppDeviceListLeast().test_start()

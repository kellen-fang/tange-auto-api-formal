# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_device_emergency_get/app_device_emergency_get.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseAppDeviceEmergencyGet(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-device_id-phone-language-push_id-push_channel-version-pkgname": "${parameterize(test_data/urgent_contact.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("查询紧急联系人").base_url("${ENV(api_url)}").export(*["idss", "token", "id"])
    )

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("查询紧急联系人")
            .post("/app/device/emergency/get")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "push_id": "$push_id",
                    "push_channel": "$push_channel",
                    "language": "$language",
                    "version": "$version",
                    "token": "$token",
                    "user_id": "$id",
                    "device_id": "$device_id",
                }
            )
            .extract()
            .with_jmespath("body.data[0].id", "idss")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppDeviceEmergencyGet().test_start()
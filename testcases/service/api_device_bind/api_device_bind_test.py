# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/api_device_bind/api_device_bind.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseApiDeviceBind(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-uuid-add_type-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids-device_id": [[200, 1, "ok", 200, 0, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("App发起绑定").base_url("${ENV(api_url)}").export(*["id", "token"])

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("App发起绑定")
            .post("api/device/bind")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "token": "$token",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "version": "$version",
                    "language": "$language",
                    "uuid": "$uuid",
                    "add_type": "$add_type",
                }
            )
            .extract()
            .with_jmespath("body.data.id", "id")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data.id", "$device_id")
        ),
    ]


if __name__ == "__main__":
    TestCaseApiDeviceBind().test_start()

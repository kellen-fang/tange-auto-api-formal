# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/personal_modifyname/personal_modifyname.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCasePersonalModifyname(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-nickname-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids-idss": [[200, 1, "ok", 200, 0, "0"]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("修改账户昵称").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("修改账户昵称")
            .post("personal/modifyname")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "language": "$language",
                    "nickname": "$nickname",
                    "pkgname": "com.tange365.icam365",
                    "platform": "$platform",
                    "token": "$token",
                    "version": "2.7.9",
                }
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data.id", "$idss")
        ),
    ]


if __name__ == "__main__":
    TestCasePersonalModifyname().test_start()
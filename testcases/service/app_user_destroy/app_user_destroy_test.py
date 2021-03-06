# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_user_destroy/app_user_destroy.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_register.app_user_register_test import (
    TestCaseAppUserRegister as AppUserRegister,
)

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseAppUserDestroy(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-scene-platform-channel-channel_id-captcha-pwd-language-pkgname-push_id-push_channel-version": "${parameterize(test_data/normal_destroy_data.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("注销用户").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("校验验证码").call(AppUserRegister)),
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("注销用户")
            .post("app/user/destroy")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "token": "$token",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "version": "$version",
                    "language": "$language",
                }
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data.id", "$ids")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppUserDestroy().test_start()

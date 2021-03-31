# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_user_change_pwd/app_user_change_pwd.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_password_verify.app_user_password_verify_test import (
    TestCaseAppUserPasswordVerify as AppUserPasswordVerify,
)


class TestCaseAppUserChangePwd(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-pwd-new-old-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("修改密码").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("校验密码").call(AppUserPasswordVerify).export(*["token"])),
        Step(
            RunRequest("修改密码")
            .post("app/user/change_pwd")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "language": "$language",
                    "new": "$new",
                    "old": "$old",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "push_channel": "$push_channel",
                    "push_id": "$push_id",
                    "token": "$token",
                    "version": "$version",
                }
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppUserChangePwd().test_start()
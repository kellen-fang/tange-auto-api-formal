# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_user_login/app_user_login.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseAppUserLogin(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids-token": [
                    [200, 1, "ok", 200, 0, "_app"]
                ],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("tange-iCam365-手机号/邮箱-用户登录")
        .base_url("${ENV(api_url)}")
        .export(*["token", "id"])
    )

    teststeps = [
        Step(
            RunRequest("手机号/邮箱-用户登录")
            .post("app/user/login")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "push_id": "$push_id",
                    "push_channel": "$push_channel",
                    "username": "$username",
                    "version": "$version",
                    "language": "$language",
                    "pwd": "$pwd",
                }
            )
            .extract()
            .with_jmespath("body.data.token", "token")
            .with_jmespath("body.data.id", "id")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data.id", "$ids")
            .assert_endswith("body.data.token", "$token")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppUserLogin().test_start()
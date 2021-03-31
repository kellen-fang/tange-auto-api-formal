# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_user_captcha_verify/app_user_captcha_verify.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_captcha_send.app_user_captcha_send_test import (
    TestCaseAppUserCaptchaSend as AppUserCaptchaSend,
)


class TestCaseAppUserCaptchaVerify(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-scene-platform-channel-channel_id-captcha-language-pkgname-push_id-push_channel-version": "${parameterize(test_data/normal_captcha_data.csv)}",
                "status_code-ok-status-code": [[200, 1, "ok", 200]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("校验验证码").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("获取发送验证码").call(AppUserCaptchaSend)),
        Step(
            RunRequest("校验验证码")
            .post("/app/user/captcha/verify")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "username": "$username",
                    "scene": "$scene",
                    "captcha": "$captcha",
                    "platform": "$platform",
                    "version": "$version",
                    "language": "$language",
                    "pkgname": "$pkgname",
                }
            )
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppUserCaptchaVerify().test_start()
# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_user_captcha_send/app_user_captcha_send.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseAppUserCaptchaSend(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-scene-platform-channel-channel_id-language-pkgname-push_id-push_channel-version": "${parameterize(test_data/normal_captcha_data.csv)}",
                "status_code-ok-status-code": [[200, 1, "ok", 200]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("tange-iCam365-发送验证码").base_url("${ENV(api_url)}")

    teststeps = [
        Step(
            RunRequest("注册/忘记密码-发送验证码")
            .post("app/user/captcha/send")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "pkgname": "$pkgname",
                    "version": "$version",
                    "language": "$language",
                    "username": "$username",
                    "scene": "$scene",
                    "platform": "$platform",
                    "channel": "$channel",
                    "channel_id": "$channel_id",
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
    TestCaseAppUserCaptchaSend().test_start()

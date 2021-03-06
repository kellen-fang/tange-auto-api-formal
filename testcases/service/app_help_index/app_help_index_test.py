# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_help_index/app_help_index.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseAppHelpIndex(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("帮助中心首页")
        .base_url("${ENV(api_url)}")
        .export(*["detail_id", "pid", "token", "id"])
    )

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("帮助中心首页")
            .post("http://static-cn01.tange365.com/app/help/index")
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
            .with_jmespath("body.data.recommend[0].id", "detail_id")
            .with_jmespath("body.data.category[0].id", "pid")
            .validate()
            .assert_equal("status_code", "$status_code")
            .assert_equal("body.ok", "$ok")
            .assert_equal("body.status", "$status")
            .assert_equal("body.code", "$code")
            .assert_greater_than("body.data.category[0].id", "$ids")
        ),
    ]


if __name__ == "__main__":
    TestCaseAppHelpIndex().test_start()

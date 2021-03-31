# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/open_exception_report/open_exception_report.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseOpenExceptionReport(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0, "0"]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("tange-iCam365-open/exception_report").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("open/exception_report")
            .post("open/exception_report")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    'detail"': "P2P_LIVE_PWD_START  p2p:TANGE-023483-CPWJB uuid:1C01FU6691QE revTime:15:05:510",
                    "function_module": "APP端",
                    "language": "$language",
                    "level": "NORMAL",
                    "path": "Camera/command",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "source": "$platform",
                    "title": "P2p_live",
                    "token": "$token",
                    "version": "$version",
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
    TestCaseOpenExceptionReport().test_start()

# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/app_geofence_list/app_geofence_list.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.app_user_login.app_user_login_test import (
    TestCaseAppUserLogin as AppUserLogin,
)


class TestCaseAppGeofenceList(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-uuid-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids": [[200, 1, "ok", 200, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("创建电子围栏").base_url("${ENV(api_url)}")

    teststeps = [
        Step(RunTestCase("获取登录token").call(AppUserLogin).export(*["id", "token"])),
        Step(
            RunRequest("创建电子围栏")
            .post("/app/geofence/list")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "token": "$token",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "version": "$version",
                    "language": "$language",
                    "uuid": "$uuid",
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
    TestCaseAppGeofenceList().test_start()
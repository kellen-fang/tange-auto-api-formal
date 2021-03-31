# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/service/version_version_update/version_version_update.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.service.version_version_list.version_version_list_test import (
    TestCaseVersionVersionList as VersionVersionList,
)


class TestCaseVersionVersionUpdate(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "username-pwd-platform-device_id-pkgname-push_id-push_channel-version-language": "${parameterize(test_data/normal_device_bind_data.csv)}",
                "status_code-ok-status-code-ids-idss": [[200, 1, "ok", 200, 0, 0]],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("固件版本升级").base_url("${ENV(api_url)}")

    teststeps = [
        Step(
            RunTestCase("获取登录token")
            .call(VersionVersionList)
            .export(*["token", "version_no"])
        ),
        Step(
            RunRequest("固件版本升级")
            .post("version/version_update")
            .with_headers(**{"Content-Type": "application/json"})
            .with_json(
                {
                    "device_id": "$device_id",
                    "language": "$language",
                    "pkgname": "$pkgname",
                    "platform": "$platform",
                    "token": "$token",
                    "version": "$version",
                    "version_no": "$version_no",
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
    TestCaseVersionVersionUpdate().test_start()

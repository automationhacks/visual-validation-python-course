import pytest

from automation.config.apps import APP_URLS
from automation.core.test_helper import TestInfo

APP = 'the-internet'
test_info = TestInfo(APP, APP_URLS[APP]['dynamic_content_for_a_section'])


@pytest.mark.parametrize('setup_test', [test_info], indirect=True)
def test_dynamic_content(setup_test, manager):
    manager.validate_window()

from automation.tests.conftest import validate_window


def test_match_level_content(driver, eyes):
    validate_window(driver, eyes)
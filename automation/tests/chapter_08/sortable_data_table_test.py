import pytest

from automation.page_objects.the_internet.tables.sortable_tables import \
    SortableTablePage


@pytest.fixture(scope='module')
def setup_suite(manager, driver):
    app_name = 'the-internet'
    app_under_test = 'https://the-internet.herokuapp.com/tables'

    manager.set_batch('sortable table test suite')
    manager.set_app_name(app_name)

    driver.get(app_under_test)
    driver.maximize_window()


@pytest.fixture(scope='function', autouse=True)
def setup_eyes(request, setup_suite, manager):
    test_name = request.function.__name__
    manager.open_eyes(test_name)
    yield setup_eyes
    manager.close_eyes()


def test_sort_by_first_name(manager):
    page = SortableTablePage(manager.driver)
    page.sort_by_first_name()

    manager.validate_window(tag='by_first_name')


def test_sort_by_last_name(manager):
    page = SortableTablePage(manager.driver)
    page.sort_by_last_name()

    manager.validate_window(tag='by_last_name')

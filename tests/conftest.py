import faker as external_faker
import pytest

_faker_instance = external_faker.Faker()


@pytest.fixture(scope='session')
def faker():
    return _faker_instance

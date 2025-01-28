import pytest

from django_core.chunk_updater import DjangoChunkUpdater
from tests.django_core.model_factory import PersonFactory


@pytest.fixture(scope='module')
def django_chunk_updater_stub(faker):
    return DjangoChunkUpdater(chunk_size=faker.pyint())

@pytest.fixture()
def ten_unhappy_and_without_job_persons(db):
    return PersonFactory.create_batch(10, is_happy=False, has_job=False)

@pytest.fixture()
def ten_unhappy_and_same_name_and_without_job_persons(db):
    return PersonFactory.create_batch(10, name="SameName", is_happy=False, has_job=False)

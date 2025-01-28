from tests.django_core.fake_project.fakeapp.models import Person


def test_should_update_by_fields(django_chunk_updater_stub, ten_unhappy_and_without_job_persons):
    # GIVEN
    payload = {
        "name": "MyNewName",
        "is_happy": True,
        "has_job": True
    }
    queryset = Person.objects.filter(id__in=[person.id for person in ten_unhappy_and_without_job_persons])

    # WHEN
    django_chunk_updater_stub.update(queryset=queryset, fields=payload, modified_columns=payload.keys())

    # THEN
    for person in queryset:
        assert person.name == payload["name"]
        assert person.has_job == payload["has_job"]
        assert person.is_happy == payload["is_happy"]


def test_should_update_only_modified_columns_by_fields(django_chunk_updater_stub, ten_unhappy_and_without_job_persons):
    # GIVEN
    payload = {
        "name": "MyNewName",
        "is_happy": True,
        "has_job": True
    }
    queryset = Person.objects.filter(id__in=[person.id for person in ten_unhappy_and_without_job_persons])

    # WHEN
    django_chunk_updater_stub.update(queryset=queryset, fields=payload, modified_columns=["name"])

    # THEN
    for person in queryset:
        assert person.name == payload["name"]
        assert person.has_job != payload["has_job"]
        assert person.is_happy != payload["is_happy"]


def test_should_ignore_duplicated_modified_columns(django_chunk_updater_stub, ten_unhappy_and_without_job_persons):
    # GIVEN
    payload = {
        "name": "MyNewName",
        "is_happy": True,
        "has_job": True
    }
    queryset = Person.objects.filter(id__in=[person.id for person in ten_unhappy_and_without_job_persons])

    # WHEN
    django_chunk_updater_stub.update(queryset=queryset, fields=payload, modified_columns=["name", "name"])

    # THEN
    for person in queryset:
        assert person.name == payload["name"]
        assert person.has_job != payload["has_job"]
        assert person.is_happy != payload["is_happy"]


def test_should_update_by_calls(django_chunk_updater_stub, ten_unhappy_and_same_name_and_without_job_persons):
    # GIVEN
    calls = {"smile", "take_a_job"}
    queryset = Person.objects.filter(id__in=[person.id for person in ten_unhappy_and_same_name_and_without_job_persons])
    initial_name = queryset.first().name

    # WHEN
    django_chunk_updater_stub.update(queryset=queryset, calls=calls, modified_columns=["has_job", "is_happy"])

    # THEN
    for person in queryset:
        assert person.name == initial_name
        assert person.has_job is True
        assert person.is_happy is True

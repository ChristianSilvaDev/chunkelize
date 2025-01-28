import factory
from factory.django import DjangoModelFactory

from tests.django_core.fake_project.fakeapp.models import Person


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker('name')
    has_job = factory.Faker('boolean')
    is_happy = factory.Faker('boolean')

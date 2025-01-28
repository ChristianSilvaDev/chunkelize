from django.db import transaction

from commons.base_updater import BaseUpdater


class DjangoChunkUpdater(BaseUpdater):
    @transaction.atomic
    def _do_persist_chunk(self, model, modified_columns):
        model.objects.bulk_update(self._objects_to_update, fields=modified_columns)

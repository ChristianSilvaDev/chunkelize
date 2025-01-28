import abc

from commons.exceptions import ArgumentError


class BaseUpdater(abc.ABC):
    def __init__(self, chunk_size):
        self._chunk_size = chunk_size
        self._objects_to_update = []

    def update(self, queryset, modified_columns, fields=None, calls=None):
        calls = calls or []
        fields = fields or {}

        if not any((fields, calls)):
            raise ArgumentError("At least one of fields or calls must be specified.")

        for obj in queryset.iterator(chunk_size=self._chunk_size):
            self._update_object_by_fields(obj, fields)
            self._invoke_object_calls(obj, calls)

            self._append_object(obj)

            if self._is_chunk_complete():
                self._persist_chunk(modified_columns=modified_columns, model=queryset.model)

        if self._remain_objects_to_update():
            self._persist_chunk(modified_columns=modified_columns, model=queryset.model)

    def _append_object(self, obj):
        self._objects_to_update.append(obj)

    def _is_chunk_complete(self):
        return len(self._objects_to_update) >= self._chunk_size

    @abc.abstractmethod
    def _do_persist_chunk(self, model, modified_columns):
        raise NotImplementedError()

    def _persist_chunk(self, model, modified_columns):
        self._do_persist_chunk(modified_columns=modified_columns, model=model)
        self._reset_objects_to_update()

    def _reset_objects_to_update(self):
        self._objects_to_update = []

    def _remain_objects_to_update(self):
        return bool(self._objects_to_update)

    def _update_object_by_fields(self, obj, fields):
        for key, value in fields.items():
            setattr(obj, key, value)

    def _invoke_object_calls(self, obj, calls):
        for call in calls:
            obj_call = getattr(obj, call, None)
            if obj_call:
                obj_call()

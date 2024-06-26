import orjson
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import Field, ValidationError

# JSONField taken from Django rest framework version 3.9.0
# See https://github.com/encode/django-rest-framework/blob/0eb2dc1137189027cc8d638630fb1754b02d6cfa/rest_framework/fields.py
# or https://www.django-rest-framework.org/api-guide/fields/#jsonfield
# for more information


class JSONField(Field):
    default_error_messages = {"invalid": _("Value must be valid JSON.")}

    def to_internal_value(self, data):
        try:
            orjson.dumps(data)
        except (TypeError, ValueError, orjson.JSONEncodeError):
            raise ValidationError(self.default_error_messages["invalid"])
        return data

import six

from sevenbridges.meta.resource import Resource
from sevenbridges.meta.fields import StringField, IntegerField


class Disk(Resource):
    """
    Disk resource contains information about EBS disk size.
    """
    size = IntegerField(read_only=True)
    unit = StringField(read_only=True)
    type = StringField(read_only=True)

    def __str__(self):
        return six.text_type(
            '<Disk size={size}, unit={unit}, type={type_}>'.format(
                id=self.size, unit=self.unit, type_=self.type
            )
        )

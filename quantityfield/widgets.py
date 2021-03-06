

from django.forms.widgets import MultiWidget, Select, NumberInput

from . import ureg


class QuantityWidget(MultiWidget):

	def get_choices(self, allowed_types=None):
		allowed_types = allowed_types or dir(ureg)			
		return [(x, x) for x in allowed_types]

	def __init__(self, attrs=None, base_units=None, allowed_types=None):
		choices = self.get_choices(allowed_types)
		self.base_units = base_units
		attrs = attrs or {}
		attrs.setdefault('step', 'any')

		widgets = (
					NumberInput(attrs=attrs),
					Select(attrs=attrs, choices=choices)
				)

		super(QuantityWidget, self).__init__(widgets, attrs)

	def decompress(self, value):
		if value:
			return [value, self.base_units]
		return [None, self.base_units]




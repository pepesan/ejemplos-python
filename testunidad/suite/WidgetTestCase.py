import unittest

from testunidad.suite.Widget import Widget


class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
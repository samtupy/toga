import toga
import toga_dummy
from toga_dummy.utils import TestCase


class SwitchTests(TestCase):
    def setUp(self):
        super().setUp()

        self.label = 'Test Label'

        def callback(widget):
            pass

        self.on_change = callback
        self.value = True
        self.enabled = True
        self.switch = toga.Switch(self.label,
                                  on_change=self.on_change,
                                  value=self.value,
                                  enabled=self.enabled,
                                  factory=toga_dummy.factory)

    def test_widget_created(self):
        self.assertEqual(self.switch._impl.interface, self.switch)
        self.assertActionPerformed(self.switch, 'create Switch')

    def test_arguments_are_all_set_properly(self):
        self.assertEqual(self.switch.label, self.label)
        self.assertEqual(self.switch._label, self.label)
        self.assertEqual(self.switch.on_change._raw, self.on_change)
        self.assertEqual(self.switch.enabled, self.enabled)

    def test_label_with_None(self):
        self.switch.label = None
        self.assertEqual(self.switch.label, '')
        self.assertEqual(self.switch._label, '')

    def test_setting_label_invokes_impl_method(self):
        new_label = 'New Label'
        self.switch.label = new_label
        self.assertValueSet(self.switch, 'label', new_label)

    def test_setting_value_invokes_impl_method(self):
        new_value = False
        self.switch.value = new_value
        self.assertValueSet(self.switch, 'value', False)

    def test_getting_value_invokes_impl_method(self):
        self.switch.value
        self.assertValueGet(self.switch, 'value')

    def test_focus(self):
        self.switch.focus()
        self.assertActionPerformed(self.switch, "focus")

    def test_toggle_from_true_to_false(self):
        self.switch.value = True
        self.switch.toggle()
        self.assertValueSet(self.switch, 'value', False)

    def test_toggle_from_false_to_true(self):
        self.switch.value = False
        self.switch.toggle()
        self.assertValueSet(self.switch, 'value', True)

    def test_set_value_with_non_boolean(self):
        with self.assertRaises(ValueError):
            self.switch.value = "on"

    def test_set_is_on(self):
        new_value = False
        with self.assertWarns(DeprecationWarning):
            self.switch.is_on = new_value
        self.assertValueSet(self.switch, 'value', False)

    def test_get_is_on(self):
        with self.assertWarns(DeprecationWarning):
            self.switch.is_on
        self.assertValueGet(self.switch, 'value')

    def test_on_change(self):
        def my_callback(widget):
            pass

        self.switch.on_change = my_callback
        self.assertEqual(self.switch.on_change._raw, my_callback)

    def test_on_toggle(self):
        def my_callback(widget):
            pass

        with self.assertWarns(DeprecationWarning):
            self.switch.on_toggle = my_callback
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(self.switch.on_toggle._raw, my_callback)
        self.assertEqual(self.switch.on_change._raw, my_callback)

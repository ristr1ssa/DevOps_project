import unittest
from filters.filter_utils import sanitize_input, escape_output


class TestSanitization(unittest.TestCase):

    def test_sanitize_input_removes_script(self):
        malicious = "<script>alert('XSS')</script>"
        cleaned = sanitize_input(malicious)
        # script-теги удалены, текст остался
        self.assertEqual(cleaned, "alert('XSS')")

    def test_escape_output_escapes_html(self):
        raw = "<div>Test & 'quotes'</div>"
        escaped = escape_output(raw)
        self.assertEqual(
            escaped, "&lt;div&gt;Test &amp; &#x27;quotes&#x27;&lt;/div&gt;")

    def test_sanitize_input_empty_for_non_string(self):
        self.assertEqual(sanitize_input(None), "")
        self.assertEqual(sanitize_input(123), "")

    def test_escape_output_empty_for_non_string(self):
        self.assertEqual(escape_output(None), "")
        self.assertEqual(escape_output(456), "")


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest tests.test_xss

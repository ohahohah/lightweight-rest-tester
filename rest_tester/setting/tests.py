class Tests(object):
    KEY_STATUS_CODE = 'statusCode'
    KEY_JSON_SCHEMA = 'jsonSchema'
    KEY_TIMEOUT = 'timeout'

    def __init__(self, tests_data):
        self._status_code = tests_data.get(self.KEY_STATUS_CODE)
        self._json_schema = tests_data.get(self.KEY_JSON_SCHEMA)

        if self._status_code is None and self._json_schema is None:
            """One of them can be missing, but not all of them."""
            raise SettingTestsError('Test case should have either status code or json schema!')

        self._timeout = tests_data.get(self.KEY_TIMEOUT, 10)

    @property
    def status_code(self):
        return self._status_code

    @property
    def json_schema(self):
        return self._json_schema

    @property
    def timeout(self):
        return self._timeout


class SettingTestsError(Exception):
    """Test types are not supported"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

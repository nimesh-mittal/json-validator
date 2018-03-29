class Prop:
    def __init__(self):
        self.max_len = None
        self.min_len = None
        self.field_type = "string"
        self.enum_values = []
        self._properties = {}
        self._items = {}

    def string(self):
        self.field_type = "string"
        return self

    def number(self):
        self.field_type = "number"
        return self

    def object(self):
        self.field_type = "object"
        return self

    def array(self):
        self.field_type = "array"
        return self

    def enum(self):
        self.field_type = "enum"
        return self

    def values(self, enum_values):
        self.enum_values = enum_values
        return self

    def properties(self, schema):
        self._properties = schema
        return self

    def items(self, schema):
        self._items = schema
        return self

    def boolean(self):
        self.field_type = "boolean"
        return self

    def max(self, value):
        self.max_len = value
        return self

    def min(self, value):
        self.min_len = value
        return self

    def build(self):
        prop = {}
        prop["type"] = self.field_type

        if self.max_len is not None:
            if self.field_type == 'number':
                prop["maximum"] = self.max_len
            elif self.field_type == 'array':
                prop["maxItems"] = self.max_len
            else:
                prop["maxLength"] = self.max_len

        if self.min_len is not None:
            if self.field_type == 'number':
                prop["minimum"] = self.min_len
            elif self.field_type == 'array':
                prop["minItems"] = self.min_len
            else:
                prop["minLength"] = self.min_len

        if self.field_type == "object":
            prop["properties"] = self._properties

        if self.field_type == "array":
            prop["items"] = self._items

        if self.field_type == "enum":
            prop["enum"] = self.enum_values
            del prop["type"]

        return prop
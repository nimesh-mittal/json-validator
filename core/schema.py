
class Schema:

    def __init__(self):
        self.schema_type = "object"
        self.additionalProperties = False

    def keys(self, properties):
        self.keys = properties
        return self

    def required(self, fields):
        self.required = fields
        return self

    def additionalProperties(self, flag):
        self.additionalProperties = flag
        return self

    def build(self):
        return dict(type=self.schema_type, properties=self.keys, required=self.required, additionalProperties=self.additionalProperties)
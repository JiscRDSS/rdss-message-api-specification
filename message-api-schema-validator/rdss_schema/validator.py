import os
import json
import jsonschema


class RDSSSchemaValidator(object):

    RDSS_SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), 'schemas')

    def __init__(self):
        self._schemas = self._load_schemas()
        self.resolver = jsonschema.RefResolver(
            '',
            {},
            store={
                schema['$id']: schema
                for schema in self._schemas
            }
        )
        self.format_checker = jsonschema.FormatChecker()

        self.schema_lookup = {
            full_id: definition_schema
            for schema in self._schemas
            for full_id, definition_schema in self._generate_definition_schemas(schema)
        }

    def _generate_definition_schemas(self, schema_json):
        schema = schema_json['$schema']
        base_id = schema_json['$id']
        schemas = {}
        for definition in schema_json.get('definitions', {}).keys():
            full_id = base_id + '/definitions/' + definition
            definition_schema = {
                '$id': full_id,
                '$schema': schema,
                '$ref': full_id
            }
            yield full_id, definition_schema

    def _list_schema_paths(self):
        schema_paths = []
        for base_dir, dirs, files in os.walk(self.RDSS_SCHEMAS_DIR):
            for f in files:
                if f.endswith('.json'):
                    schema_paths.append(os.path.join(base_dir, f))
        return schema_paths

    def _load_schemas(self):
        return [self._load_json(path) for path in self._list_schema_paths()]

    def _load_json(self, path):
        with open(path) as file_in:
            return json.load(file_in)

    def _validate_json(self, json_data, json_schema):
        jsonschema.validate(
            json_data,
            json_schema,
            resolver=self.resolver,
            format_checker=self.format_checker
        )

    def validate_json_with_schema(self, schema_ref, json_data):
        json_schema = self.schema_lookup[schema_ref]
        self._validate_json(json_data, json_schema)

    def validate_json_file_with_schema(self, schema_ref, json_file_path):
        json_data = self._load_json(json_file_path)
        self.validate_json_with_schema(schema_ref, json_data)

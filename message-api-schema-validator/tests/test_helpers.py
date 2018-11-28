import pytest
import json
import jsonschema
from rdss_schema.validator import RDSSSchemaValidator


def valid_against_schema(schema_name, json_data):
    rdss_validator = RDSSSchemaValidator()
    rdss_validator.validate_json_with_schema(
        schema_name,
        json_data
    )


def invalid_against_schema(schema_name, json_data):
    rdss_validator = RDSSSchemaValidator()
    with pytest.raises(jsonschema.exceptions.ValidationError):
        rdss_validator.validate_json_with_schema(
            schema_name,
            json_data
        )


def valid_file_against_schema(schema_name, json_path):
    rdss_validator = RDSSSchemaValidator()
    rdss_validator.validate_json_file_with_schema(
        schema_name,
        json_path
    )


def invalid_file_against_schema(schema_name, json_path):
    rdss_validator = RDSSSchemaValidator()
    with pytest.raises(jsonschema.exceptions.ValidationError):
        rdss_validator.validate_json_file_with_schema(
            schema_name,
            json_path
        )


def load_json(json_path):
    with open(json_path) as json_in:
        return json.load(json_in)

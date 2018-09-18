import pytest
import json
import jsonschema
from rdss_schema.validator import RDSSSchemaValidator


@pytest.fixture
def valid_against_schema():
    rdss_validator = RDSSSchemaValidator()

    def _valid_against_schema(schema_name, json_data):
        rdss_validator.validate_json_with_schema(
            schema_name,
            json_data
        )
    return _valid_against_schema


@pytest.fixture
def invalid_against_schema():
    rdss_validator = RDSSSchemaValidator()

    def _invalid_against_schema(schema_name, json_data):
        with pytest.raises(jsonschema.exceptions.ValidationError):
            rdss_validator.validate_json_with_schema(
                schema_name,
                json_data
            )
    return _invalid_against_schema


@pytest.fixture
def valid_file_against_schema():
    rdss_validator = RDSSSchemaValidator()

    def _valid_file_against_schema(schema_name, json_path):
        rdss_validator.validate_json_file_with_schema(
            schema_name,
            json_path
        )
    return _valid_file_against_schema


@pytest.fixture
def invalid_file_against_schema():
    rdss_validator = RDSSSchemaValidator()

    def _invalid_file_against_schema(schema_name, json_path):
        with pytest.raises(jsonschema.exceptions.ValidationError):
            rdss_validator.validate_json_file_with_schema(
                schema_name,
                json_path
            )
    return _invalid_file_against_schema

@pytest.fixture
def load_json():
    def _load_json(json_path):
        with open(json_path) as json_in:
            return json.load(json_in)
    return _load_json

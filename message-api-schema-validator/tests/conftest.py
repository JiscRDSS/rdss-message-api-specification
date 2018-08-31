import pytest
import jsonschema
from rdss_schema.validator import RDSSSchemaValidator 


@pytest.fixture
def valid_against_schema():
    rdss_validator = RDSSSchemaValidator()
    def _valid_against_schema(schema_name, json_path):
        rdss_validator.validate_json_with_schema(
                schema_name, 
                json_path
                )
    return _valid_against_schema

@pytest.fixture
def invalid_against_schema():
    rdss_validator = RDSSSchemaValidator()
    def _invalid_against_schema(schema_name, json_path):
        with pytest.raises(jsonschema.exceptions.ValidationError):
            rdss_validator.validate_json_with_schema(
                    schema_name, 
                    json_path
                    )
    return _invalid_against_schema

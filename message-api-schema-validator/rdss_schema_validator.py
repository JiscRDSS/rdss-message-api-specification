from json import load
from jsonschema import validate, FormatChecker, RefResolver
from abc import ABCMeta, abstractmethod
from sys import argv
from unittest import TestCase
import os


class AbstractSchemaValidatorTest(TestCase):
    __metaclass__ = ABCMeta

    schema_id_path_pairs = [
        (
            'https://www.jisc.ac.uk/rdss/schema/enumeration.json/#',
            'schemas/enumeration.json'
        ),
        (
            'https://www.jisc.ac.uk/rdss/schema/intellectual_asset.json/#',
            'schemas/intellectual_asset.json'
        ),
        (
            'https://www.jisc.ac.uk/rdss/schema/material_asset.json/#',
            'schemas/material_asset.json'
        ),
        (
            'https://www.jisc.ac.uk/rdss/schema/research_object.json/#',
            'schemas/research_object.json'
        ),
        (
            'https://www.jisc.ac.uk/rdss/schema/types.json/#',
            'schemas/types.json'
        ),
        (
            'https://www.jisc.ac.uk/rdss/schema/header.json/#',
            'schemas/header.json'
        )
    ]

    # base_path = argv[1]
    # Replaced above with below to pass tests as argv[1] is not set when this is run, change made to gain pass in travis
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Remove test directories, windows and unix, to move the based dir up
    dir_path = dir_path.replace('\\tests', '')
    dir_path = dir_path.replace('\\message-api-schema-validator', '')
    dir_path = dir_path.replace('/tests', '')
    dir_path = dir_path.replace('/message-api-schema-validator', '')

    @abstractmethod
    def get_json_schema_file_name(self): pass

    def validate_json(self, json_file_name):
        json_schema = self.get_json(self.get_json_schema_file_name())
        json_data = self.get_json(json_file_name)
        validate(
            json_data,
            json_schema,
            resolver=RefResolver(
                '',
                {},
                store={
                    schema_id: self.get_json(schema_path)
                    for schema_id, schema_path in self.schema_id_path_pairs
                }
            ),
            format_checker=FormatChecker()
        )

    def get_json(self, file_name):
        with open(self.prepare_file_name(file_name)) as json_data:
            return load(json_data)

    def prepare_file_name(self, file_name):
        return self.dir_path + '/' + file_name

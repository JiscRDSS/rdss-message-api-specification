from ..test_helpers import load_json, valid_against_schema, invalid_against_schema


def test_metadata_delete_request_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_delete_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/delete/research_object_delete_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/delete_request.json/#/definitions/MetadataDeleteRequest',
        message
    )


def test_metadata_delete_request_with_research_object_body_is_invalid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_delete_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/research_object_create_request.json'
        )
    }
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/delete_request.json/#/definitions/MetadataDeleteRequest',
        message
    )

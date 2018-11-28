from ..test_helpers import load_json, valid_against_schema, invalid_against_schema, valid_file_against_schema


def test_example_message_is_valid():
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        '../messages/example_message.json'
    )


def test_metadata_create_article_body_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_create_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/article_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        message
    )


def test_metadata_create_dataset_body_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_create_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/dataset_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        message
    )


def test_metadata_create_research_object_body_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_create_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/research_object_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        message
    )


def test_metadata_create_thesis_dissertation_body_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_create_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/thesis_dissertation_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        message
    )


def test_metadata_create_information_package_body_is_invalid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_create_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/preservation/preservation_event_request.json'
        )
    }
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
        message
    )

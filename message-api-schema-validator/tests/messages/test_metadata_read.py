from ..test_helpers import load_json, valid_against_schema, invalid_against_schema


def test_metadata_read_request_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_request_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/read/research_object_read_request.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_request.json/#/definitions/MetadataReadRequest',
        message
    )

def test_metadata_read_response_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_response_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/read/research_object_read_response.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_response.json/#/definitions/MetadataReadResponse',
        message
    )

def test_metadata_read_article_response_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_response_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/create/article_create_request.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_response.json/#/definitions/MetadataReadResponse',
        message
    )

def test_metadata_read_dataset_response_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_response_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/create/dataset_create_request.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_response.json/#/definitions/MetadataReadResponse',
        message
    )


def test_metadata_read_research_object_response_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_response_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/create/research_object_create_request.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_response.json/#/definitions/MetadataReadResponse',
        message
    )


def test_metadata_read_thesis_dissertation_response_is_valid():
    message = {
        'messageHeader': load_json(
            '../messages/header/metadata_read_response_header.json'
        ),
        'messageBody': load_json(
        '../messages/body/metadata/create/thesis_dissertation_create_request.json'
        )
    }

    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/read_response.json/#/definitions/MetadataReadResponse',
        message
    )

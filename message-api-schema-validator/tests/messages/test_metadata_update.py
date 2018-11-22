
def test_metadata_update_article_body_is_valid(load_json, valid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/article_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/update_request.json/#/definitions/MetadataUpdateRequest',
        message
    )


def test_metadata_update_dataset_body_is_valid(load_json, valid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/dataset_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/update_request.json/#/definitions/MetadataUpdateRequest',
        message
    )


def test_metadata_update_research_object_body_is_valid(load_json, valid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/research_object_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/update_request.json/#/definitions/MetadataUpdateRequest',
        message
    )


def test_metadata_update_thesis_dissertation_body_is_valid(load_json, valid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/thesis_dissertation_create_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/update_request.json/#/definitions/MetadataUpdateRequest',
        message
    )


def test_metadata_update_information_package_body_is_invalid(load_json, invalid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/header.json'
        ),
        'messageBody': load_json(
            '../messages/body/preservation/preservation_event_request.json'
        )
    }
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/metadata/update_request.json/#/definitions/MetadataUpdateRequest',
        message
    )

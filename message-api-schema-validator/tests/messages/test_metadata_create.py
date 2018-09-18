
def test_metadata_create_article_body_is_valid(load_json, valid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/metadata/create/article_create_request.json'
                )
            }
    valid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
            message
    )

def test_metadata_create_dataset_body_is_valid(load_json, valid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/metadata/create/dataset_create_request.json'
                )
            }
    valid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
            message
    )

def test_metadata_create_research_object_body_is_valid(load_json, valid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/metadata/create/research_object_create_request.json'
                )
            }
    valid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
            message
    )

def test_metadata_create_thesis_dissertation_body_is_valid(load_json, valid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/metadata/create/thesis_dissertation_create_request.json'
                )
            }
    valid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
            message
    )

def test_metadata_create_information_package_body_is_invalid(load_json, invalid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/preservation/create/information_package_create_request.json'
                )
            }
    invalid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/metadata/create_request.json/#/definitions/MetadataCreateRequest',
            message
    )


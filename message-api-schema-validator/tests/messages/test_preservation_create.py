
def test_preservation_create_information_package_body_is_valid(load_json, valid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/preservation/create/information_package_create_request.json'
                )
            }
    valid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/preservation/create_request.json/#/definitions/PreservationCreateRequest',
            message
    )

def test_preservation_create_research_object_body_is_invalid(load_json, invalid_against_schema):
    message = {
            'messageHeader': load_json(
                '../messages/header/header.json'
                ),
            'messageBody': load_json(
                '../messages/body/metadata/create/research_object_create_request.json'
                )
            }
    invalid_against_schema(
            'https://www.jisc.ac.uk/rdss/schema/message/preservation/create_request.json/#/definitions/PreservationCreateRequest',
            message
    )


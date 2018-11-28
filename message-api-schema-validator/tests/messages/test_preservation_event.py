
def test_preservation_event_information_package_body_is_valid(load_json, valid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/preservation_event_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/preservation/preservation_event_request.json'
        )
    }
    valid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/preservation/preservation_event_request.json/#/definitions/PreservationEventRequest',
        message
    )


def test_preservation_event_research_object_body_is_invalid(load_json, invalid_against_schema):
    message = {
        'messageHeader': load_json(
            '../messages/header/preservation_event_header.json'
        ),
        'messageBody': load_json(
            '../messages/body/metadata/create/research_object_create_request.json'
        )
    }
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/message/preservation/preservation_event_request.json/#/definitions/PreservationEventRequest',
        message
    )

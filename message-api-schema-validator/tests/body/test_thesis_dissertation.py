
def test_thesis_dissertation_is_valid(valid_file_against_schema):
    valid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        '../messages/body/metadata/create/thesis_dissertation_create_request.json'
    )


def test_thesis_dissertation_without_awarded_date_is_invalid(load_json, invalid_against_schema):
    message_body = load_json(
        '../messages/body/metadata/create/thesis_dissertation_create_request.json')
    message_body['objectDate'] = [
        i for i in message_body['objectDate'] if i['dateType'] != 'awarded']
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        message_body
    )


def test_thesis_dissertation_without_awarding_institution_is_invalid(load_json, invalid_against_schema):
    message_body = load_json(
        '../messages/body/metadata/create/thesis_dissertation_create_request.json')
    message_body['objectOrganisationRole'] = [
        i for i in message_body['objectOrganisationRole'] if i['role'] != 'awardingInstitution']
    invalid_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        message_body
    )


def test_article_is_not_a_valid_thesis_dissertation(invalid_file_against_schema):
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        '../messages/body/metadata/create/article_create_request.json'
    )


def test_research_object_is_not_a_valid_thesis_dissertation(invalid_file_against_schema):
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        '../messages/body/metadata/create/research_object_create_request.json'
    )


def test_dataset_is_not_a_valid_thesis_dissertation(invalid_file_against_schema):
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        '../messages/body/metadata/create/dataset_create_request.json'
    )


def test_information_package_is_not_a_valid_thesis_dissertation(invalid_file_against_schema):
    invalid_file_against_schema(
        'https://www.jisc.ac.uk/rdss/schema/thesis_dissertation.json/#/definitions/ThesisDissertation',
        '../messages/body/preservation/preservation_event_request.json'
    )

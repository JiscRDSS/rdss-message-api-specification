
def test_article_is_valid(valid_against_schema): 
    valid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/article.json/#/definitions/Article",
            "../messages/body/metadata/create/article_create_request.json"
            )


def test_research_object_is_not_a_valid_article(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/article.json/#/definitions/Article",
            "../messages/body/metadata/create/research_object_create_request.json"
            )

def test_thesis_dissertation_is_not_a_valid_article(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/article.json/#/definitions/Article",
            "../messages/body/metadata/create/thesis_dissertation_create_request.json"
            )

def test_dataset_is_not_a_valid_article(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/article.json/#/definitions/Article",
            "../messages/body/metadata/create/dataset_create_request.json"
            )


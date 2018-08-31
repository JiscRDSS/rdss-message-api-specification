
def test_research_object_is_valid(valid_against_schema): 
    valid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/research_object.json/#/definitions/ResearchObject",
            "../messages/body/metadata/research_object/create/request.json"
            )


def test_article_is_not_a_valid_research_object(invalid_against_schema):
    invalid_against_schema(
            "https://www.jisc.ac.uk/rdss/schema/research_object.json/#/definitions/ResearchObject",
            "../messages/body/metadata/article/create/request.json"
            )


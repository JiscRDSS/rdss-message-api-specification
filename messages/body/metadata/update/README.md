# Metadata Update

Message Type: `MetadataUpdate`.
Message Class: `Command`.

Describes a JSON payload of metadata of a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) that is generated during a `UPDATE` operation.

## Scenarios

- Sent to subscribers to notify that metadata for a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj), [Article](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Article-content-model.mdj), [Dataset](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Dataset-content-model.mdj) or [Thesis](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Content-Models/Thesis-content-model.mdj) has been updated.

## Request

- Research Object example: [`research_object_update_request.json`](research_object_create_request.json)
- Schema: [`schemas/message/metadata/update_request.json`](../../../../schemas/message/metadata/update_request.json)

(n.b. Payloads for these messages are identical in form to those for `MetadataCreate` messages, so only a `ResearchObject` payload is provided as an example.)

## Response

N/A.

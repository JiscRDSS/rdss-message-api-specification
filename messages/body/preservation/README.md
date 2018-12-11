# Preservation Event

Message Type: `PreservationEvent`.
Message Class: `Event`.

A JSON payload consisting of an [InformationPackage](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Information-Package/Information-package-model.mdj), which describes an event during the preservation of an object (e.g. a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj)).

## Scenarios

- Sent to subscribers to notify them of events occurring during the preservation of an object (e.g. a [ResearchObject](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Canonical-data-model.mdj)). The full range of supported events can be found under `PreservationEventType` in [`schemas/enumeration.json`](../../../../schemas/enumeration.json), and are documented in the [InformationPackage](https://github.com/JiscRDSS/Canonical-data-model/blob/4.0.0/Data-Model/Information-Package/Information-package-model.mdj) model.

## Request

- Example: [`preservation_event_request.json`](preservation_event_request.json)
- Schema: [`schemas/message/preservation/preservation_event_request.json`](../../../../schemas/message/preservation/preservation_event_request.json)

## Response

N/A.

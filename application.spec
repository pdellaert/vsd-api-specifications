{
    "attributes": {
        "assocEgressACLTemplateId": {
            "description": "The ID of the ACL template that this application is pointing to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "assocIngressACLTemplateId": {
            "description": "The ID of the ACL template that this application is pointing to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedDomainID": {
            "description": "Domain id where the application is running.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedDomainType": {
            "description": "Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.",
            "allowed_choices": [
                "DOMAIN",
                "L2DOMAIN"
            ],
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectID": {
            "description": "ID of the network object that this App is associated with.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectType": {
            "description": "Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.",
            "allowed_choices": [
                "ENTERPRISE",
                "DOMAIN"
            ],
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the application.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the application.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "flow": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        },
        "tier": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a real life application like a vendor website, or a social network.",
        "entity_name": "App",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "applications",
        "rest_name": "application",
        "update": true
    }
}
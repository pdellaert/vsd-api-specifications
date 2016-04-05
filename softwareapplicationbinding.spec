{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Associated software application ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedSoftwareApplicationID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Priority of the Application within an Application Group",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 1000,
            "min_length": null,
            "min_value": 10,
            "name": "priority",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "member",
            "rest_name": "softwareapplication",
            "update": true
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": null,
        "entity_name": "SoftwareApplicationBinding",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "softwareapplicationbindings",
        "rest_name": "softwareapplicationbinding",
        "root": null,
        "update": true
    }
}
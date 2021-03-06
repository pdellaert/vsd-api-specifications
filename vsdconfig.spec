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
            "description": "This Attribute defines the VSD config attribute value",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 512,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "attributeValue",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Attribute Value"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "This Attribute defines the VSD config attribute name.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "id",
            "orderable": false,
            "read_only": true,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Attribute Name"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "The VSD Configuration which can be dynamically managed using REST Api.",
        "entity_name": "VSDConfig",
        "extends": [],
        "get": true,
        "package": "common",
        "resource_name": "vsdconfigs",
        "rest_name": "vsdconfig",
        "root": false,
        "template": null,
        "update": true,
        "userlabel": "VSD Config"
    }
}
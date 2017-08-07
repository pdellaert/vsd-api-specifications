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
            "description": "The list of L4 Services to be grouped",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "L4Services",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "L4 Services"
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
            "description": "Describes the L4 Service Group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 256,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
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
            "description": "Name of the L4 Services group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 256,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "name",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": true,
            "uniqueScope": null,
            "userlabel": "Name"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "L4 Service Group is a set of L4 Services that can be used in ACLs.",
        "entity_name": "L4servicegroup",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "l4servicegroups",
        "rest_name": "l4servicegroup",
        "root": null,
        "update": true
    }
}
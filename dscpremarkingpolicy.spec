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
            "description": "DSCP value range from enumeration of 65 values: *, 0, 1, ..., 63",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "DSCP",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Map DSCP"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Class of service to be used.Service classes in order of priority are A, B, C, D, E, F, G, and H.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "forwardingClass",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Forwarding Class to DSCP"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "Provides the definition of a single Forwarding class to DSCP mapping that is part of a DSCP Remarking table used in Egress QoS policies.",
        "entity_name": "DSCPRemarkingPolicy",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/dscpmapping",
        "resource_name": "dscpremarkingpolicies",
        "rest_name": "dscpremarkingpolicy",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "DSCP Remarking Policy"
    }
}
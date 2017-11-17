{
    "attributes": [
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
                "H",
                "NONE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Value of the Service Class to be overridden in the packet when the match conditions are satisfied.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "FCOverride",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "FC Override"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "IKE",
                "UNDERLAY_PAT",
                "UNDERLAY_ROUTE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of forwarding action associated with this entry.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "forwardingAction",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Forwarding Action"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "PRIMARY",
                "SECONDARY"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of forwarding uplink preference associated with this entry.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "uplinkPreference",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Uplink Preference"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "Forwarding path list entry to be associated with forwarding path list for l4 based policy to PAT / IKE to underlay.",
        "entity_name": "ForwardingPathListEntry",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "forwardingpathlistentries",
        "rest_name": "forwardingpathlistentry",
        "root": null,
        "update": true,
        "userlabel": "Forwarding Path List Entry"
    }
}
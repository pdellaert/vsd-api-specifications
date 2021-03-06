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
            "description": "List of Controller-VRS links associated with the nsg",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "controllervrslinks",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": "ControllerVRSLink",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Controller VRS Links"
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
            "description": "An embedded object from the nsinfo entity from VSD. Contains info such as software version, CPU type, BIOS version etc. The embedded object is returned in JSON format",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "nsginfo",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Nsginfo"
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
            "description": "Information from the NSGState object in VSD in JSON format. Contains information about connection status, TPM status, operation mode etc.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "nsgstate",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Nsgstate"
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
            "description": "NSG summary in JSON format - contains alarm counts, locality, bootstrap info etc.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "nsgsummary",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Nsgsummary"
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
            "description": "information about VRS reported from sysmon in JSON format. Has info about cpu usage, memory usage, physical interfaces etc.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "vrsinfo",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": "VRS",
            "transient": false,
            "type": "object",
            "unique": true,
            "uniqueScope": null,
            "userlabel": "VRS information"
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
            "description": "List of controllers associated with the nsg",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "vscs",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": "VSC",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Vscs"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "This API can be used to gather read-only information about an NSG, including information on its state, system metrics, alarm counts, location and version. It is a single view of the full data available for an NSG.",
        "entity_name": "NSGatewayMonitor",
        "extends": [],
        "get": true,
        "package": "nsg",
        "resource_name": "nsgatewaysmonitors",
        "rest_name": "nsgatewaysmonitor",
        "root": null,
        "template": null,
        "update": false,
        "userlabel": "NSG monitor"
    }
}
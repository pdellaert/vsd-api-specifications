{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV4",
                "IPV6"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "PATEnabled": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "address": {
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationID": {
            "description": "The associated application ID.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectID": {
            "description": "The associated application object ID.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectType": {
            "allowed_choices": [
                "ACLENTRY_LOCATION",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "ALARM",
                "APPD_APPLICATION",
                "APPD_EXTERNAL_APP_SERVICE",
                "APPD_FLOW",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPLICATION",
                "AUTO_DISC_GATEWAY",
                "BACK_HAUL_SERVICE_RESP",
                "BGPPEER",
                "BGP_NEIGHBOR",
                "BGP_NEIGHBOR_MED_RESPONSE",
                "BGP_PROFILE",
                "BGP_PROFILE_MED_RESPONSE",
                "BOOTSTRAP",
                "BOOTSTRAP_ACTIVATION",
                "BRIDGEINTERFACE",
                "CERTIFICATE",
                "CHILD_ENTITY_POLICY_CHANGE",
                "CLOUD_MGMT_SYSTEM",
                "CUSTOMER_VRF_SEQUENCENO",
                "DC_CONFIG",
                "DHCP_ALLOC_MESSAGE",
                "DHCP_CONFIG_RESP",
                "DHCP_OPTION",
                "DISKSTATS",
                "DOMAIN",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "DOMAIN_TEMPLATE",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_QOS_MR",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "ENDPOINT",
                "ENTERPRISE",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "ENTERPRISE_NETWORK",
                "ENTERPRISE_PERMISSION",
                "ENTERPRISE_PROFILE",
                "ENTERPRISE_SECURED_DATA",
                "ENTERPRISE_SECURITY",
                "ENTITY_METADATA_BINDING",
                "ESI_SEQUENCENO",
                "EVENT_LOG",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "FLOATINGIP",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "GATEWAY",
                "GATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "GATEWAY_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_PROFILE",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_TEMPLATE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GEO_VM_EVENT",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GROUP",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "HEALTH_REQ",
                "HOSTINTERFACE",
                "HSC",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_GATEWAY",
                "INFRASTRUCTURE_CONFIG",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "IP_BINDING",
                "JOB",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "LDAP_CONFIG",
                "LIBVIRT_INTERFACE",
                "LICENSE",
                "LOCATION",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "METADATA",
                "METADATA_TAG",
                "MIRROR_DESTINATION",
                "MONITORING_PORT",
                "MULTI_NIC_VPORT",
                "NATMAPENTRY",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "NETWORK_MACRO_GROUP",
                "NETWORK_POLICY_GROUP",
                "NEXT_HOP_RESP",
                "NODE_EXECUTION_ERROR",
                "NSGATEWAY",
                "NSGATEWAY_CONFIG",
                "NSGATEWAY_TEMPLATE",
                "NSG_NOTIFICATION",
                "NSPORT",
                "NSPORT_STATIC_CONFIG",
                "NSPORT_TEMPLATE",
                "NSREDUNDANT_GW_GRP",
                "NS_REDUNDANT_PORT",
                "PATCONFIG_CONFIG_RESP",
                "PATNATPOOL",
                "PERMISSION",
                "PERMITTED_ACTION",
                "POLICING_POLICY",
                "POLICY_DECISION",
                "POLICY_GROUP",
                "POLICY_GROUP_TEMPLATE",
                "PORT",
                "PORT_MR",
                "PORT_TEMPLATE",
                "PUBLIC_NETWORK",
                "QOS_PRIMITIVE",
                "RATE_LIMITER",
                "RD_SEQUENCENO",
                "REDUNDANT_GW_GRP",
                "RESYNC",
                "ROUTING_POLICY",
                "ROUTING_POL_MED_RESPONSE",
                "RTRD_ENTITY",
                "RTRD_SEQUENCENO",
                "SERVICES_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICE_VRF_SEQUENCENO",
                "SHAPING_POLICY",
                "SHARED_RESOURCE",
                "SITE",
                "SITE_REQ",
                "SITE_RES",
                "STATIC_ROUTE",
                "STATIC_ROUTE_RESP",
                "STATISTICS",
                "STATSSERVER",
                "STATS_COLLECTOR",
                "STATS_POLICY",
                "STATS_TCA",
                "SUBNET",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "SUBNET_POOL_ENTRY",
                "SUBNET_TEMPLATE",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SYSTEM_MONITORING",
                "UNSUPPORTED",
                "UPLINK_RD",
                "USER",
                "VIRTUAL_IP",
                "VIRTUAL_MACHINE",
                "VIRTUAL_MACHINE_REPORT",
                "VLAN",
                "VLAN_CONFIG_RESPONSE",
                "VLAN_TEMPLATE",
                "VMWARE_RELOAD_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VM_DESCRIPTION",
                "VM_INTERFACE",
                "VNID_SEQUENCENO",
                "VPN_CONNECT",
                "VPORT",
                "VPORTTAG",
                "VPORTTAGTEMPLATE",
                "VPORT_GATEWAY_RESPONSE",
                "VPORT_MEDIATION_REQUEST",
                "VPORT_MIRROR",
                "VPORT_TAG_BASE",
                "VPRN_LABEL_SEQUENCENO",
                "VRS",
                "VSC",
                "VSD",
                "VSD_COMPONENT",
                "VSG_REDUNDANT_PORT",
                "VSP",
                "WAN_SERVICE",
                "ZONE",
                "ZONE_TEMPLATE"
            ],
            "description": "The associated application object type. Refer to API section for supported types.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedSharedNetworkResourceID": {
            "description": "The ID of public subnet that is associated with this subnet",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description field provided by the user that identifies the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "encryption": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "Determines whether or not IPSEC is enabled.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "The IP address of the gateway of this subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayMACAddress": {
            "description": "",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "maintenanceMode": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "ENABLED_INHERITED"
            ],
            "description": "maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests.",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "multicast is enum that indicates multicast policy on Subnet/Subnet Template.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "Netmask of the subnet defined",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "proxyARP": {
            "description": " when set VRS will act as  ARP Proxy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "public": {
            "description": "when set to true means public subnet under a public zone",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "routeDistinguisher": {
            "description": "The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "routeTarget": {
            "description": "The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "serviceID": {
            "description": "The service ID used by the VSCs to identify this subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "splitSubnet": {
            "description": "Need to add correct description",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the subnet template that this subnet object was derived from",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "underlayEnabled": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "Indicates whether UNDERLAY is enabled for the subnets in this domain",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "vnId": {
            "description": "Current Network's  globally unique  VXLAN network identifier generated by VSD",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "children": {
        "addressrange": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "dhcpoption": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "ipreservation": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "resync": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        },
        "statisticspolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "tca": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "virtualip": {
            "get": true,
            "relationship": "child"
        },
        "vm": {
            "get": true,
            "relationship": "child"
        },
        "vminterface": {
            "get": true,
            "relationship": "child"
        },
        "vport": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a subnet associated with a zone.",
        "entity_name": "Subnet",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "subnets",
        "rest_name": "subnet",
        "update": true
    }
}
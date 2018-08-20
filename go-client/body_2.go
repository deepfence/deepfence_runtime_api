/*
 * Deepfence Runtime API v1.3
 *
 * Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider, container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.
 *
 * API version: 1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package deepfence_runtime_api

type Body2 struct {

	// action to take, when a policy is enforced
	Action string `json:"action,omitempty"`

	// Number of seconds to block/allow the ip address
	BlockDuration int32 `json:"block_duration,omitempty"`

	// Host name
	HostName string `json:"host_name,omitempty"`

	// List of IP addresses
	IpAddressList []string `json:"ip_address_list,omitempty"`

	// Policy type - whitelist or blacklist
	NodePolicyType string `json:"node_policy_type,omitempty"`

	// Packet direction - inbound or outbound
	PacketDirection string `json:"packet_direction,omitempty"`

	// List of ports
	PortList []string `json:"port_list,omitempty"`
}

/*
 * Deepfence Runtime API v1.3
 *
 * Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider, container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.
 *
 * API version: 1.3
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package deepfence_runtime_api

type Body3 struct {

	// List of policy ids
	PolicyIdList []int32 `json:"policy_id_list,omitempty"`
}

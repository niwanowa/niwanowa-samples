variable "static_web_apps_location" {
  description = "The location/region where the static web apps should be created"
  default     = "East US"
  type = string
}

variable "resource_static_web_apps_prefix" {
  type        = string
  default     = "swa"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

variable "resource_group_name" {
  type       = string
}

variable "resource_group_location" {
  type       = string  
}

variable "subnet_id" {
  type       = string
}
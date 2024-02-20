variable "resource_virtual_network_prefix" {
  type        = string
  default     = "vnet"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

variable "resource_subnet_prefix" {
  type        = string
  default     = "subnet"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

variable "resource_group_name" {
  type        = string
}

variable "resource_virtual_network_location" {
  type        = string
  default     = "eastus"
  description = "Location of the resource group."
}

variable "virtual_network_address_space" {
    type        = list(string)
    default     = ["10.0.0.0/16"]
}

variable "subnet_address_prefixes" {
    type        = list(string)
    default     = ["10.0.1.0/24"]
}
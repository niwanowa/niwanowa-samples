variable "name_prefix" {
  type = string
  default = "DEV"
    description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}

variable "default_location" {
  type        = string
  default     = "japaneast"
  description = "Location of the resource group."
}
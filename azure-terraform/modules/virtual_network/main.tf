resource "random_pet" "vnet_name" {
  prefix = var.resource_virtual_network_prefix
}

resource "random_pet" "subnet_name" {
  prefix = var.resource_subnet_prefix
}

resource "azurerm_virtual_network" "swa_vnet" {
  name     = random_pet.vnet_name.id
  address_space       = var.virtual_network_address_space
  location = var.resource_virtual_network_location
  resource_group_name = var.resource_group_name
}

resource "azurerm_subnet" "swa_subnet" {
    name = random_pet.subnet_name.id
    resource_group_name = var.resource_group_name
    virtual_network_name = azurerm_virtual_network.swa_vnet.name
    address_prefixes = var.subnet_address_prefixes
}
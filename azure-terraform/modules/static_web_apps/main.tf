resource "random_pet" "swa_name" {
  prefix = var.resource_static_web_apps_prefix
}

resource "azurerm_static_site" "example" {
  name                = random_pet.swa_name.id
  resource_group_name = var.resource_group_name
  location            = var.static_web_apps_location
}
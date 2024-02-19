resource "azurerm_static_site" "example" {
  name                = "example"
  resource_group_name = "rg-holy-coral"
  location            = var.resource_group_location
}
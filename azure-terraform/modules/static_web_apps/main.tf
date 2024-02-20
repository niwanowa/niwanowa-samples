resource "random_pet" "swa_name" {
  prefix = var.resource_static_web_apps_prefix
}

resource "azurerm_static_site" "example" {
  name                = random_pet.swa_name.id
  resource_group_name = var.resource_group_name
  location            = var.static_web_apps_location
  sku_tier           = "Standard"
  sku_size           = "Standard"
}

resource "azurerm_private_endpoint" "example"{
  name                = "example-privateendpoint"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
  subnet_id           = var.subnet_id
  private_service_connection {
    name                           = "example-privateserviceconnection"
    is_manual_connection           = false
    private_connection_resource_id = azurerm_static_site.example.id
    subresource_names              = ["staticSites"]
  }
}
module "resource_group" {
    source = "../../modules/resource_group"

    resource_group_name_prefix = var.name_prefix
    resource_group_location = var.default_location
}

module "virtual_network" {
    source = "../../modules/virtual_network"

    resource_group_name = module.resource_group.resource_group_name
    resource_virtual_network_prefix = var.name_prefix
    resource_subnet_prefix = var.name_prefix
    resource_virtual_network_location = var.default_location
}

module "static_web_apps" {
    source = "../../modules/static_web_apps"
  
    resource_group_name = module.resource_group.resource_group_name
    resource_group_location = module.resource_group.resource_group_location
    static_web_apps_location = var.static_web_apps_location
    subnet_id =  module.virtual_network.subnet_id
}
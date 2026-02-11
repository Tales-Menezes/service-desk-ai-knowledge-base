resource "random_string" "suffix" {
  length  = 6
  upper   = false
  special = false
}

locals {
  name_suffix = random_string.suffix.result
  rg_name     = "${var.project_name}-${var.environment}-rg-${local.name_suffix}"
  search_name = lower("${var.project_name}-${var.environment}-srch-${local.name_suffix}")
  raw_sa      = lower("${var.project_name}${var.environment}${local.name_suffix}")
  sa_name     = substr(join("", regexall("[a-z0-9]", local.raw_sa)), 0, 24)
}


resource "azurerm_resource_group" "rg" {
  name     = local.rg_name
  location = var.location
}

# Azure AI Search (Basic tier for cost control)
resource "azurerm_search_service" "search" {
  name                = local.search_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  sku = "basic"

  replica_count   = 1
  partition_count = 1

  tags = {
    project     = var.project_name
    environment = var.environment
    owner       = "tales"
    purpose     = "portfolio"
    ttl         = "ephemeral"
  }
}

# Optional but useful soon (documents)
resource "azurerm_storage_account" "sa" {
  name                     = local.sa_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  allow_nested_items_to_be_public = false

  tags = {
    project     = var.project_name
    environment = var.environment
  }
}

resource "azurerm_storage_container" "kb" {
  name                  = "kb-docs"
  storage_account_name    = azurerm_storage_account.sa.name
  container_access_type = "private"
}

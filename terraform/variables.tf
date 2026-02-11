variable "project_name" {
  type    = string
  default = "sd-ai-kb"
}

variable "location" {
  type    = string
  default = "UK South"
}

variable "environment" {
  type    = string
  default = "ephemeral"
}

variable "subscription_id" {
  type        = string
  description = "Azure subscription ID used by Terraform"
}

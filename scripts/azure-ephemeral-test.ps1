Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Push-Location terraform
terraform init
terraform apply -auto-approve

if ($LASTEXITCODE -ne 0) {
  throw "Terraform apply failed. Aborting index creation."
}

if ([string]::IsNullOrWhiteSpace($endpoint)) { throw "search_endpoint output is empty." }
if ([string]::IsNullOrWhiteSpace($key))      { throw "search_admin_key output is empty." }
if ([string]::IsNullOrWhiteSpace($index))    { throw "search_index_name output is empty/missing. Add it to terraform/outputs.tf and re-apply." }


if ([string]::IsNullOrWhiteSpace($index)) {
  throw "search_index_name output is empty/missing. Add it to terraform/outputs.tf and re-apply."
}

Pop-Location

.\scripts\create-search-index.ps1 -SearchEndpoint $endpoint -AdminKey $key -IndexName $index

Write-Host "`n✅ Azure Search + index ready."
Write-Host "Endpoint: $endpoint"
Write-Host "Index:    $index"

Write-Host "`nWhen done testing, run:"
Write-Host "  scripts\azure-down.ps1"

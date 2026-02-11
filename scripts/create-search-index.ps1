param(
  [Parameter(Mandatory=$true)][string]$SearchEndpoint,
  [Parameter(Mandatory=$true)][string]$AdminKey,
  [Parameter(Mandatory=$true)][string]$IndexName
)

$headers = @{
  "api-key"      = $AdminKey
  "Content-Type" = "application/json"
}

$body = @{
  name = $IndexName
  fields = @(
    @{ name="id"; type="Edm.String"; key=$true; searchable=$false; filterable=$false; sortable=$false; facetable=$false },
    @{ name="content"; type="Edm.String"; searchable=$true; filterable=$false; sortable=$false; facetable=$false },
    @{ name="client"; type="Edm.String"; searchable=$false; filterable=$true; sortable=$true; facetable=$true },
    @{ name="category"; type="Edm.String"; searchable=$false; filterable=$true; sortable=$true; facetable=$true },
    @{ name="title"; type="Edm.String"; searchable=$true; filterable=$false; sortable=$true; facetable=$false },
    @{ name="source_file"; type="Edm.String"; searchable=$false; filterable=$false; sortable=$true; facetable=$false },
    @{ name="chunk_index"; type="Edm.Int32"; searchable=$false; filterable=$true; sortable=$true; facetable=$false }
    # embedding field added later when we enable vector search
  )
} | ConvertTo-Json -Depth 10

# API version: keep stable for now, but may need to update in the future as new features are added
$apiVersion = "2023-11-01"

$uri = "$SearchEndpoint/indexes/$IndexName?api-version=$apiVersion"

Write-Host "Creating/updating index: $IndexName"
$response = Invoke-RestMethod -Method Put -Uri $uri -Headers $headers -Body $body
Write-Host "Index ready: $($response.name)"

$urls = @(
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-900/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-200/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-300/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-400/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-401/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-500/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-100/",
    "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-700/"
)

foreach ($url in $urls) {
    try {
        $response = Invoke-WebRequest -Uri $url -Method Head -UseBasicParsing
        Write-Host "[OK] $($response.StatusCode) $url"
    }
    catch {
        Write-Host "[FAIL] $url"
    }
}

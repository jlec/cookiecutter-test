output "github_repo" {
  value       = module.controller.github_repo_url
  description = "GitHub repo URL"
}

output "tfe_workspace_url" {
  value       = module.controller.tfe_workspace_url
  description = "TFE workspace URL"
}

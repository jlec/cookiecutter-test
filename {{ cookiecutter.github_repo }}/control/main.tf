module "controller" {
  source  = "app.terraform.io/jlec/controller/module"
  version = "~>0.3.12"

  tfe_oauth_token_id = var.tfe_oauth_token_id

  gh_repo_name        = "{{ cookiecutter.github_repo }}"
  gh_repo_description = "{{ cookiecutter.cookiecutter_description }}"

  tfe_workspace_name        = "{{ cookiecutter.cookiecutter_slug }}"
  tfe_workspace_description = "{{ cookiecutter.cookiecutter_description }}"
}

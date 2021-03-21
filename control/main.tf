module "controller" {
  source  = "app.terraform.io/jlec/controller/module"
  version = "~>0.3.12"

  tfe_oauth_token_id = var.tfe_oauth_token_id

  gh_repo_name        = "cookiecutter-cookie"
  gh_repo_description = "Cookies for Cookiecutters"

  tfe_workspace_name        = "cookiecutter_cookie"
  tfe_workspace_description = "Cookies for Cookiecutters"
}

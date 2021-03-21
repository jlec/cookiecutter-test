terraform {
  backend "remote" {
    organization = "jlec"

    workspaces {
      name = "cookiecutter_cookie"
    }
  }
}

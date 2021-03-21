# Project control for {{ cookiecutter.project_slug }}

GH repo and TFE config for {{ cookiecutter.project_slug }}
<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## Requirements

No requirements.

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_controller"></a> [controller](#module\_controller) | app.terraform.io/jlec/controller/module | ~>0.3.12 |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_tfe_oauth_token_id"></a> [tfe\_oauth\_token\_id](#input\_tfe\_oauth\_token\_id) | GH to TFE oauth token ID | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_github_repo"></a> [github\_repo](#output\_github\_repo) | GitHub repo URL |
| <a name="output_tfe_workspace_url"></a> [tfe\_workspace\_url](#output\_tfe\_workspace\_url) | TFE workspace URL |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## License

Apache-2.0

## Author Information

- {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

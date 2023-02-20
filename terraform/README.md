# ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)

## How to use it?


### First Steps

First of all, you need to install Terraform following their [guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

Then check your installation...

```sh
terraform --version
# Terraform v1.3.7
# on linux_amd64
```

Terraform Validate, Terraform check if your stack looks ok.

```sh
terraform validate
```

Terraform Plan, is to show you a preview waht well be created, like an preview. *(this is optional)*

This command can also output an execution plan that you can specify at `terraform apply`.

```sh
terraform plan
```

Terraform apply, this command will create all resources you set on the `main.tf`.

If you didn't execute the `terraform plan` and generated a output, the `terraform apply` you create one in runtime.

```sh
terraform apply
```

Terraform destroy, this command will delete all resources created based on your stack. **(But pay attention if the resource you created is not secure protect from accidental excludes)**

```sh
terraform destroy
```

### That is it 🚀
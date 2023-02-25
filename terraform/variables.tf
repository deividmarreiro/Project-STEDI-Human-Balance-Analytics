variable "aws_region" {
    type = string
    default = "us-east-1"  
}

variable "bucket_name" {
    type = string
    default = "udacity-stedi-data-lakehouse"
}

variable "glue_iam_role" {
    type = string
    default = "my-glue-service-role"   
}
variable "credentials" {
  description = "My Credentials"
  default     = "~/.keys/terraform-runner.json"
}

variable "project" {
  description = "Project name"
  default     = "de-practice-414118"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Location"
  default     = "US"
}

variable "bq_dataset" {
  description = "BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "GCS Bucket Name"
  default     = "terraform-de-practice-v1"
}

variable "gcs_storage_class" {
  description = "GCS Bucket Storage Class"
  default     = "STANDARD"
}
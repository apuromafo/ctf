
- IAM (Identity and Access Management) -> AWS service used to manage identities, control who can access what, and define permissions for AWS resources
- IAM policies: written in JSON; policies can end up being overly permissive
  
- S3 (Simple Storage Service) is AWS’s object storage

### Commands: 
- `aws iam list-users` : lists all IAM users in the account
- `aws iam list-user-policies --user-name sir.carrotbane` : returns the names of inline policies attached to sir.carrotbane
- `aws iam list-attached-user-policies --user-name sir.carrotbane` : checks for attatched policies
- `aws iam list-groups-for-user --user-name sir.carrotbane` : checks for group membership


## Answers:
- Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? : `123456789012`
- What IAM component is used to describe the permissions to be assigned to a user or a group? : `policy`
- What is the name of the policy assigned to sir.carrotbane? : `SirCarrotbanePolicy`
- Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? : `ListAllMyBuckets`
- What are the contents of the cloud_password.txt file? : `THM{more_like_sir_cloudbane}`

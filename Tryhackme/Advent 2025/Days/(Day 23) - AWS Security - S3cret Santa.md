#Conceptos Fundamentales de AWS
IAM (Identity and Access Management): Servicio de AWS utilizado para gestionar identidades, controlar quién tiene acceso a qué y definir permisos para los recursos de AWS. Es el núcleo de la seguridad en la nube.

Políticas de IAM (IAM Policies): Documentos escritos en JSON que definen los permisos. En entornos reales, estas políticas suelen terminar siendo excesivamente permisivas (overly permissive), lo que abre vectores para el escalamiento de privilegios o el movimiento lateral.

S3 (Simple Storage Service): El servicio de almacenamiento de objetos de AWS. Es un objetivo común en auditorías debido a configuraciones incorrectas en sus políticas de acceso o ACLs.



#Comandos de Enumeración de IAM
`aws iam list-users`: Lista todos los usuarios de IAM presentes en la cuenta. Útil para identificar objetivos potenciales.

`aws iam list-user-policies --user-name sir.carrotbane`: Devuelve los nombres de las políticas integradas (inline policies) que están directamente vinculadas al usuario.

`aws iam list-attached-user-policies --user-name sir.carrotbane`: Busca las políticas administradas que están adjuntas al usuario.

`aws iam list-groups-for-user --user-name sir.carrotbane`: Verifica la pertenencia a grupos del usuario, lo cual es clave para identificar permisos heredados.

## Answers:
- Run aws sts get-caller-identity. What is the number shown for the "Account" parameter? : 
`123456789012`
- What IAM component is used to describe the permissions to be assigned to a user or a group? : `
policy`
- What is the name of the policy assigned to sir.carrotbane? : 
`SirCarrotbanePolicy`
- Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role? : 
`ListAllMyBuckets`
- What are the contents of the cloud_password.txt file? : 
`THM{more_like_sir_cloudbane}`
 
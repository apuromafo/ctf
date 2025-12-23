- A **virtual machine** runs on a hypervisor (software that emulates and manages multiple operating systems on one physical host)
- **Containers** share the host OS kernel, isolating only applications and their dependencies, which makes them lightweight and fast to start

- Docker: build, deploy, and maintain containers; isolate application and use the host OS kernel
- A **container escape** is a technique that enables code running inside a container to obtain rights or execute on the host kernel (or other containers) beyond its isolated environment (escaping).

## Answers:
- What exact command lists running Docker containers? : `docker ps`
- What file is used to define the instructions for building a Docker image? : `Dockerfile`
- What's the flag? : `THM{DOCKER_ESCAPE_SUCCESS}`
- Bonus Question: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it? : `DeployMaster2025!`


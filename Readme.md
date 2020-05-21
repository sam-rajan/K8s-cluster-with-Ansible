
# Kubernetes cluster using Ansible.

These are the set of ansible playbooks intended to create a minimum viable single control-plane Kubernetes cluster that conforms to best practices using [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/).

**Prerequisites**

 - Two or more machines running on Ubuntu `16.04+`
 - Deployment environment must have Ansible `2.4.0+` and  `Python 3`
 - Unique hostname, MAC address, and product_uuid for every node
 - Full network connectivity among all machines that is going to be the part of cluster.

    

## How these playbooks make a Kuberenetes cluster?

These are the series of straightforward steps for creating a cluster using kubeadm by installing kubeadm, kubelet, kubectl, etc.

 1. As a Pre-Check, it will print UUID and MAC address for all your machines, and pause for your confirmation. Here you can verify all UUID and MAC addresses are unique for each node.
 2. Next step is installing all the essential tools/programs such as **curl, ca-certificates, etc.**  Mostly your Linux distribution will have these programs and if you are sure about it, you can skip this by commenting out the `- common` under roles section in playbook `site.yml`.
 3.Then we are installing the legacy version of iptables since **kubeadm is not compatible** with the modern version of **iptables which is backed with nftables**(replacement for the kernel’s iptables subsystem).
 4. Then installing container runtime in all the machines, i.e **Docker** in our case.
 5. And after that, we are installing **Kubelet and Kubeadm** in all the machines.
 6. The next step is Creating cluster and then all the nodes are joining the newly created cluster. And please do remind **this is a single control-plane cluster**.
 7. Finally, it will install **Calico Pod network addon and Kubernetes dashboard** as well.

# Usage

Add your system's IP address under the different sections in `hosts` file based on the role for each nodes.
For example:

```
[masters] 
192.168.10.10

[slaves]
192.168.10.[11:13]
```
*Here `masters` represent all the control plane nodes and `slaves` as the name implies slave nodes* 

Edit `group_vars/all.yml` and add your `ssh username and password`
  

After above steps, run the `site.yml` playbook:

  

    ansible-playbook -i hosts site.yml

**Note:** This probably requires privilege escalation, in that case add `--ask-become-pass` or `-K`, Ansible prompts you for the password to use for privilege escalation.

# Contributing

We are open for pull requests. Feel free to dig through the [issues](https://github.com/sam-rajan/K8s-cluster-with-Ansible/issues) and jump in.

 We encourage everyone to follow the feature branching model. See [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) for more details and best practices.

## Road map

 - Add sonobuoy for conformance test
 - High availability Kubernetes cluster
 - Support for multiple Linux distributions
 - High Availability etcd cluster
 - Adding support for Kops, KRIB and Kubespray
 - Support for more networking addons such as Flannel, Cilium, Weave net
 - 
 - 
 - 

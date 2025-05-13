# Load Balancing

## what is a load balancer

A load balancer is a networking device or software application that distributes and balances the incomming traffic among the servers to provide high availability, efficient utilization or servers, and high performance. A load balancer works as a "traffic cop" sitting in front of your server and routing client requests across all servers.

- Load balancers are highly used in cloud computing domains, data centers, and large-scale web applications where traffic flow needs to be managed.
- It simply distributes the set of requests operations effectively across multiple servers and ensures that no single server bears too many requests.


## What Happens Without a Load Balancer?

![load balancer](../img/load_balancer.avif)

### Without Load Balancing

There are three main problems with this model:

* **Single Point of Failure**:
  If the server goes down, the entire application becomes unavailable, resulting in a poor user experience.

* **Overloaded Servers**:
  A single server has a limit to how many requests it can handle. As traffic grows, it becomes overwhelmed.

* **Limited Scalability**:
  Adding more servers doesn’t help unless there's a mechanism (like a load balancer) to distribute traffic among them.


## Key Characteristics of Load Balancers

* **Traffic Distribution**: Evenly splits incoming traffic among servers.
* **High Availability**: Ensures that traffic is redirected to healthy servers.
* **Scalability**: Makes it easy to add/remove resources.
* **Optimization**: Prevents bottlenecks and improves resource use.
* **Health Monitoring**: Detects and avoids sending traffic to unhealthy servers.
* **SSL Termination**: Can handle encryption/decryption to offload that task from servers.


## How Load Balancers Work

1. **Receives Incoming Requests**: All client requests go through the load balancer.
2. **Checks Server Health**: Monitors servers to identify which ones are available.
3. **Distributes Traffic**: Sends traffic to the best-suited server based on algorithms.
4. **Handles Server Failures**: Reroutes traffic when a server fails.
5. **Optimizes Performance**: Balances loads to improve user experience.


## Types of Load Balancers

### 1. Hardware Load Balancers

* Physical devices installed in data centers.
* High performance but expensive and harder to scale.
* Used in high-traffic, enterprise environments.

### 2. Software Load Balancers

* Runs on existing infrastructure or in the cloud.
* More scalable and cost-effective.
* Easier to modify and maintain.

### 3. Cloud Load Balancers

* Managed by providers like AWS, Azure, GCP.
* Highly scalable and pay-as-you-go.
* Ideal for dynamic workloads.

### 4. Layer 4 Load Balancers (Transport Layer)

* Uses TCP/UDP (IP addresses and ports) to route traffic.
* Faster but doesn't inspect application-level data.

### 5. Layer 7 Load Balancers (Application Layer)

* Uses HTTP headers, URLs, cookies, etc., for intelligent routing.
* Allows content-based routing.

### 6. Global Server Load Balancers (GSLB)

* Distributes traffic across geographic regions.
* Reduces latency and improves disaster recovery.


## Load Balancing Algorithms

To distribute traffic efficiently, different algorithms are used:

### 1. Static Load Balancing

* Predefined rules; doesn't adapt to real-time conditions.

**Types:**

* Round Robin
* Weighted Round Robin
* Source IP Hash

### 2. Dynamic Load Balancing

* Adjusts based on current server conditions.

**Types:**

* Least Connection Method
* Least Response Time Method


## Benefits of Load Balancing

* **Increased Performance**: Prevents slowdowns and downtime.
* **Scalability**: Works well with auto-scaling features.
* **Failure Management**: Redirects traffic away from failing servers.
* **Prevents Bottlenecks**: Predicts traffic spikes.
* **Efficient Resource Use**: Distributes workload evenly.
* **Session Persistence**: Maintains user sessions effectively.


## Challenges of Load Balancers

* **Single Point of Failure**: If the load balancer fails, everything fails.
* **Cost and Complexity**: High-end solutions can be costly and hard to manage.
* **Configuration Issues**: Misconfiguration can lead to performance issues.
* **Overhead**: Can introduce latency.
* **SSL Inspection Issues**: End-to-end encryption can be harder to manage.

## reference

[load balancer gfg](https://www.geeksforgeeks.org/what-is-load-balancer-system-design/)

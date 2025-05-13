# Backend system design

## Load Balancing

A load balancer is a networking device or software application that distributes and balances the incoming traffic among the servers to provide high availability, efficient utilization of servers, and high performance. A load balancer works as a “traffic cop” sitting in front of your server and routing client requests across all servers

- Load balancers are highly used in cloud computing domains, data centers, and large-scale web applications where traffic flow needs to be managed.
- It simply distributes the set of requested operations effectively across multiple servers and ensures that no single server bears too many requests.

## Caching  

Caching is the process of storing copies of frequently accessed data in a temporary storage location, called a cache, so that future requests for that data can be served faster.

- Common types of caches: memory (e.g., Redis, Memcached), browser cache, CDN cache.
- Reduces database load, increases response time, and improves scalability.
- Useful in read-heavy applications where the same data is requested multiple times.

## CDN

A CDN is a geographically distributed network of servers that work together to deliver web content (like images, videos, stylesheets, scripts) to users based on their geographic location.

- Improves website speed and performance.
- Reduces server load and latency.
- Provides protection against DDoS attacks and ensures high availability.

## Microservices

Microservices is an architectural style where an application is composed of small, independent services that communicate over APIs.

- Each service handles a specific business function (e.g., user service, payment service).
- Enables independent deployment, scaling, and development.
- Often used with containers, CI/CD, and service discovery tools.

## API gateway

An API Gateway acts as a single entry point for all client requests to a set of microservices.

- Handles routing, authentication, rate limiting, and load balancing.
- Improves security by hiding backend service details.
- Examples: Kong, AWS API Gateway, NGINX.

## Webhook

A webhook is a way for one application to send real-time data or notifications to another application when a specific event occurs.

- Works on a “push” mechanism (event-driven).
- Common in payment gateways, Git services, and messaging apps.
- Requires a URL endpoint to receive the data payload.

## Sharding

Sharding is a database partitioning technique where large datasets are divided into smaller, more manageable pieces called shards, which are stored across multiple database instances.

- Improves performance and scalability.
- Each shard handles a subset of data (e.g., based on user ID ranges).
- Common in distributed databases like MongoDB, Cassandra.

## Proxy

A proxy is an intermediary server between the client and the backend server.

- Forward Proxy: Used by clients to access external resources (e.g., for privacy or security).
- Reverse Proxy: Used by servers to route incoming requests (e.g., for load balancing or caching).
- Enhances security, controls traffic, and provides anonymity.

## Message queues

A message queue is a form of asynchronous communication where messages are sent between services via a queue.

- Producers send messages; consumers read them later.
- Helps decouple services and handle high traffic or delayed processing.
- Ensures reliability, fault tolerance, and load smoothing.
- Examples: RabbitMQ, Apache Kafka, Amazon SQS.

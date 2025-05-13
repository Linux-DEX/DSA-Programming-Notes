# Software Architecture Patterns

## 1. Layered Architecture Pattern

As the name suggests, components(code) in this pattern are separated into layers of subtasks and they are arranged one above another. Each layer has unique tasks to do and all the layers are independent of one another. Since each layer is independent, one can modify the code inside a layer without affecting others. It is the most commonly used pattern for designing the majority of software. This layer is also known as ‘N-tier architecture’. Basically, this pattern has 4 layers.

- **Presentation layer**: The user interface layer where we see and enter data into an application.)
- **Business layer**: This layer is responsible for executing business logic as per the request.)
- **Application layer**: This layer acts as a medium for communication between the ‘presentation layer’ and ‘data layer’.
- **Data layer**: This layer has a database for managing data.)

### Advantages:

- **Scalability**: Individual layers in the architecture can be scaled independently to meet performance needs.
- **Flexibility**: Different technologies can be used within each layer without affecting others.
- **Maintainability**: Changes in one layer do not necessarily impact other layers, thus simplifying the maintenance.

### Disadvantages:

- **Complexity**: Adding more layers to the architecture can make the system more complex and difficult to manage.
- **Performance Overhead**: Multiple layers can introduce latency due to additional communication between the layers.
- **Strict Layer Separation**: Strict layer separation can sometimes lead to inefficiencies and increased development effort.

### Use Cases:

- Enterprise Applications like Customer Relationship Management (CRM).
- Web Applications like E-commerce platforms.
- Desktop Applications such as Financial Software.
- Mobile Applications like Banking applications.
- Content Management Systems like WordPress.

## 2. Client-Server Architecture Pattern

The client-server pattern has two major entities. They are a server and multiple clients. Here the server has resources(data, files or services) and a client requests the server for a particular resource. Then the server processes the request and responds back accordingly.

### Advantages:

- **Centralized Management**: Servers can centrally manage resources, data, and security policies, thus simplifying the maintenance.
- **Scalability**: Servers can be scaled up to handle increased client requests.
- **Security**: Security measures such as access controls, data encryption can be implemented in a better way due to centralized controls.

### Disadvantages:

- **Single Point of Failure**: Due to centralized server, if server fails clients lose access to services, leading loss of productivity.
- **Costly**: Setting up and maintaining servers can be expensive due to hardware, software, and administrative costs.
- **Complexity**: Designing and managing a client-server architecture can be complex.

### Use Cases:

- Web Applications like Amazon.
- Email Services like Gmail, Outlook.
- File Sharing Services like Dropbox, Google Drive.
- Media Streaming Services like Netflix.
- Education Platforms like Moodle.

## 3. Event-Driven Architecture Pattern

Event-Driven Architecture is an agile approach in which services (operations) of the software are triggered by events. When a user takes action in the application built using the EDA approach, a state change happens and a reaction is generated that is called an event.

### Example:

A new user fills the signup form and clicks the signup button on Facebook and then a FB account is created for him, which is an event.

### Advantages:

- **Scalability**: System can scale horizontally by adding more consumers.
- **Real-time Processing**: This enables real-time processing and immediate response to events.
- **Flexibility**: New event consumers can be added without modifying existing components.

### Disadvantages:

- **Complexity**: The architecture can be complex to design, implement, and debug.
- **Complex Testing**: Testing event-driven systems can be complicated compared to synchronous systems.
- **Reliability**: Ensuring reliability requires additional mechanisms to handle failed events.

### Use Cases:

- Real-Time Analytics like stock market analysis systems.
- IoT Applications like smart home systems.
- Financial Systems like fraud detection systems monitor transactions in real-time.
- Online multiplayer games.
- Customer Support Systems like Chatbots.

## 4. Microkernel Architecture Pattern

Microkernel pattern has two major components. They are a core system and plug-in modules.

- The core system handles the fundamental and minimal operations of the application.
- The plug-in modules handle the extended functionalities (like extra features) and customized processing.

Let’s imagine, you have successfully built a chat application. And the basic functionality of the app is that you can text with people across the world without an internet connection. After some time, you would like to add a voice messaging feature to the application, then you are adding the feature successfully. You can add that feature to the already developed application because the microkernel pattern facilitates you to add features as plug-ins.

### Advantages:

- **Flexibility**: New functionalities can be added easily through plug-ins.
- **Scalability**: The system can scale by adding more plug-ins to handle more tasks.
- **Maintainability**: Plug-ins are developed and tested independently which makes maintenance easier.

### Disadvantages:

- **Complex Communication**: Managing communication between the core systems and plug-ins can be complex.
- **Lack Built-in Functionalities**: Due to minimalistic design the basic functionalities are absent that are common in monolithic architectures.
- **Complex Design**: Designing the microkernel and its communication mechanisms can be challenging.

### Use Cases:

- Operating Systems like Windows NT and macOS.
- Embedded Systems like Automotive Software Systems.
- Plugin-based Applications like Eclipse IDE.

## 5. Microservices Architecture Pattern

The collection of small services that are combined to form the actual application is the concept of microservices pattern. Instead of building a bigger application, small programs are built for every service (function) of an application independently. And those small programs are bundled together to be a full-fledged application. So adding new features and modifying existing microservices without affecting other microservices are no longer a challenge when an application is built in a microservices pattern. Modules in the application of microservices patterns are loosely coupled. So they are easily understandable, modifiable and scalable.

### Advantages:

- **Scalability**: Each service can be scaled independently based on demand.
- **Faster Delivery**: Independent services allows teams to develop, test, and deploy features faster.
- **Easier Maintenance**: Services can be updated and maintained independently.

### Disadvantages:

- **Complex Management**: Managing multiple services requires robust monitoring and management tools.
- **Network Congestion**: Increased network traffic between services can lead to congestion and overhead.
- **Security**: Securing multiple services and their communication increases the probability of attack.

### Use Cases:

- E-commerce Platforms like Amazon and eBay.
- Streaming services like Netflix and Spotify.
- Online Banking Platforms.
- Electronic Health Record (EHR) Systems.
- Social Media Platforms like Twitter and Facebook.

## 6. Space-Based Architecture Pattern

Space-Based Architecture Pattern is also known as Cloud-Based or Grid-Based Architecture Pattern. It is designed to address the scalability issues associated with large-scale and high-traffic applications. This pattern is built around the concept of shared memory space that is accessed by multiple nodes.

### Advantages:

- **Scalability**: The system can be easily scaled horizontally by adding more processing units.
- **Performance**: In-memory data grids reduces the data access latency.
- **Flexibility**: Modular components allow for flexible deployment.

### Disadvantages:

- **Complexity**: Designing and managing distributed system is complex.
- **Cost**: The infrastructure for space-based architecture pattern requires multiple servers and advanced middleware, which can be expensive.
- **Network Latency**: Communication between distributed components can introduce network latency.

### Use Cases:

- E-commerce Platforms like Amazon.
- Telecom Service Providers.
- Multiplayer Online Games.

## 7. Master-Slave Architecture Pattern

The Master-Slave Architecture Pattern is also known as Primary-Secondary Architecture. It involves a single master component and that controls multiple slave components. The master components assign tasks to slave components and the slave components report the results of task execution back to the master. This is often used for parallel processing and load distribution.

### Advantages:

- **Scalability**: The system can scale horizontally by adding more slave units to handle increased load.
- **Fault Tolerance**: If slave fails, then the master can reassign the tasks to some another slave. thus enhancing the fault tolerance.
- **Performance**: Parallel execution of tasks can improve the performance of the system.

### Disadvantages:

- **Single Point of Failure**: The master component is a single point of failure. If the master fails then the entire system can collapse.
- **Complex Communication**: The communication overhead between master and slave can be significant especially in large systems.
- **Latency**: Systems’ responsiveness can be affected by the latency introduced by master-slave communication.

### Use Cases:

- Database Replication.
- Load Balancing.
- Sensor Networks.
- Backup and Recovery Systems.

## 8. Pipe-Filter Architecture Pattern

Pipe-Filter Architecture Pattern structures a system around a series of processing elements called filters that are connected by pipes. Each filter processes data and passes it to the next filter via pipe.

### Advantages:

- **Reusability**: Filters can be reused in different pipelines or applications.
- **Scalability**: Additional filters can be added to extend the functionality to the pipeline.
- **Parallelism**: Filters can be executed in parallel if they are stateless, thus improving performance.

### Disadvantages:

- **Debugging Difficulty**: Identifying and debugging issues are difficult in long pipelines.
- **Data Format constraints**: Filters must agree on the data format, requiring careful design and standardization.
- **Latency**: Data must be passed through multiple filters, which can introduce latency.

### Use Cases:

- Data Processing Pipelines like Extract, Transform, Load (ETL) processes in data warehousing.
- Compilers.
- Stream-Processing like Apache Flink.
- Image and Signal Processing.

## 9. Broker Architecture Pattern

The Broker architecture pattern is designed to manage and facilitate communication between decoupled components in a distributed system. It involves a broker that acts as a intermediary to route the requests to the appropriate server.

### Advantages:

- **Scalability**: Brokers support horizontal scaling by adding more servers to handle increased load.
- **Flexibility**: New servers can be added and the existing ones can be removed or modified without impacting the entire system.
- **Fault Tolerance**: If a server fails, then broker can route the request to another server.

### Disadvantages:

- **Complex Implementation**: Implementing a broker requires robust management of routing and load balancing, thus make system more complex.
- **Single Point of Failure**: If broker is not designed with failover mechanisms then it can become a single point of failure.
- **Security Risks**: Securing broker component is important to prevent potential vulnerabilities.

### Use Cases:

- Integration of various enterprise applications like CRM, ERP, and HR systems.
- Systems using message brokers like RabbitMQ or Apache Kafka.
- Sensor networks in IoT applications.

## 10. Peer-to-Peer Architecture Pattern

The Peer-to-Peer (P2P) architecture pattern is a decentralized network model where each node, known as a peer, acts as both a client and a server. There is no central authority or single point of control in P2P architecture pattern. Peers can share resources, data, and services directly with each other.

### Advantages:

- **Scalability**: The network can scale easily as more peers join.
- **Fault Tolerance**: As data is replicated across multiple peers, this results in system being resilient to failures.
- **Cost Efficiency**: There is no need for centralized servers, thus reducing the infrastructure cost.

### Disadvantages:

- **Security Risks**: Decentralized nature of the architecture makes it difficult to enforce security policies.
- **Data Consistency**: Ensuring data consistency across peers can be challenging.
- **Complex Management**: Managing a decentralized network with numerous independent peers can be complex.

### Use Cases:

- File Sharing like BitTorrent Protocol.
- Blockchain and Cryptocurrencies such as Bitcoin and Ethereum.
- VoIP and Communication like Skype.

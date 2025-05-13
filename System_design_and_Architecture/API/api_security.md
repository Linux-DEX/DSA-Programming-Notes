# API Security methods

## 1. **Use HTTPS**

- **How it Helps**: Encrypts data in transit, protecting against eavesdropping, tampering, and man-in-the-middle attacks. This ensures that sensitive data like credentials and tokens remain private and unaltered during transmission.
- **How it Works**: HTTPS uses SSL/TLS encryption to secure HTTP requests. A server must have an SSL certificate from a trusted authority, allowing clients to verify its identity. HTTPS encrypts data before transmission, making it unreadable to unauthorized parties.

## 2. **Use OAuth2**

- **How it Helps**: Provides a secure way to authorize users and applications without exposing their credentials, allowing only authenticated clients to access certain data or actions.
- **How it Works**: OAuth2 operates through authorization tokens (e.g., Bearer tokens) rather than credentials. After the user authenticates, the API grants an access token for specific permissions, which the client uses in requests, reducing the need to repeatedly transmit sensitive credentials.

## 3. **Use WebAuthn**

- **How it Helps**: Adds an extra layer of security through passwordless, cryptographic authentication, making it resistant to phishing and credential theft.
- **How it Works**: WebAuthn uses public-key cryptography. During the initial setup, the server stores a public key while the client holds the private key. For subsequent authentications, the server sends a challenge that the client signs with its private key, verifying identity without passwords.

## 4. **Use Leveled API Keys**

- **How it Helps**: Limits access based on predefined roles or privileges, restricting actions users or apps can perform, which reduces exposure in case of compromised keys.
- **How it Works**: API keys are configured with specific access levels (e.g., read-only, read-write). Each key is assigned permissions according to user roles, ensuring minimal privilege for each key and reducing risk if one is exposed.

## 5. **Authorization**

- **How it Helps**: Controls access by enforcing permissions, ensuring that users can only perform actions or view data they are authorized for.
- **How it Works**: Authorization checks occur after authentication, verifying that the user has the required permissions (e.g., roles, scopes) for a specific request, often using access control lists or role-based access control (RBAC).

## 6. **Rate Limiting**

- **How it Helps**: Prevents abuse and malicious activity, like brute force attacks or excessive requests, which could lead to service disruptions.
- **How it Works**: The API tracks the number of requests from each client/IP and imposes limits based on a time window (e.g., 100 requests per minute). If a client exceeds the limit, the API temporarily blocks or slows requests to prevent overload.

## 7. **API Versioning**

- **How it Helps**: Maintains backward compatibility and stability, allowing updates without disrupting existing clients, reducing security risks from outdated API calls.
- **How it Works**: API versions are defined in the URL (e.g., `/v1/users`) or headers. Clients specify the version they want, and updates are released as new versions, ensuring that older clients continue to function without forced changes.

## 8. **Allowlisting**

- **How it Helps**: Restricts API access to approved clients or IP addresses, blocking unknown or malicious sources.
- **How it Works**: The API maintains a list of allowed IPs or domains. Requests from sources not on the list are denied, ensuring only trusted sources can access the API.

## 9. **Check OWASP API Security Risks**

- **How it Helps**: Protects against common vulnerabilities by addressing known security risks, such as broken authentication, excessive data exposure, or insecure endpoints.
- **How it Works**: Developers regularly review and address the top security issues listed by OWASP for APIs, implementing patches or best practices to close vulnerabilities.

## 10. **Use API Gateway**

- **How it Helps**: Acts as a central entry point for managing security, traffic, and monitoring across multiple APIs, simplifying and centralizing control.
- **How it Works**: The API Gateway authenticates, authorizes, and routes requests to backend services. It often includes built-in security features like rate limiting, logging, and IP blocking.

## 11. **Error Handling**

- **How it Helps**: Prevents sensitive information leaks by showing generic errors to clients while logging detailed errors on the server side.
- **How it Works**: The API responds to clients with simple, non-descriptive error messages (e.g., "400 Bad Request"), while logging technical details internally, ensuring that sensitive information about the system’s internal structure isn’t exposed.

## 12. **Input Validation**

- **How it Helps**: Blocks malicious data from being processed by the API, reducing the risk of injection attacks, buffer overflows, and other vulnerabilities.
- **How it Works**: Input validation checks incoming data to ensure it meets expected formats (e.g., numeric, text) and size constraints. Data is sanitized to remove harmful characters or code before processing, protecting the API from harmful input.


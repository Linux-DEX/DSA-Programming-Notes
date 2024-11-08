# Rendering Patterns for Web Apps

## 1. Static websites

- Pre-build HTML, CSS, & javascript files that are served to the client as-is.
- No dynamic content, as all content is pre-rendered and does not change.
- Fast load times due to the lack of server processing.

### Pros:

- Extremely fast load times and low server costs.
- Great for sites with little to no dynamic content, such as portfolios or blogs.

### Cons:

- Limited interactivity and functionality, as all content is pre-rendered.
- Not suitable for sites that require dynamic content or user input.

### Best for:

- Sites with limited dynamic content or sites that do not require dynamic functionality.

## 2. Single Page Application( SPAs )

- All content is dynamically rendered client-side through javascript.
- Only a single page is loaded, with content updates handled by javascript.
- Dynamic content can be easily added through APIs.

### Pros

- High interactivity and functionality, as all content is dynamic and can be updated without refreshing the page.
- Ideal for complex, data-driven applications that require frequent content updates.

### Cons

- Slower initial load times due to the need to load javascript and dynamically render content.
- Can be difficult to implement proper SEO techniques due to the lack of pre-rendered content.

### Best for:

- Applications that require complex interactivity of frequent content updates.

## 3. Server Side Rendering ( SSR )

- Server side rendering ( SSR ) is a process in which web pages are generated on the server and sent to the client as fully rendered HTML.
- The server sends a complete HTML response to the client, which includes all the dynamic content, after processing the data on the server.

### Pros

- Improved SEO because search engine crawlers can easily parse the complete HTML content.
- Better performance because the initial HTML is sent in a single response, which reduces the time for the browser to load and display the content.
- Works well for content-rich applications or dynamic web applications that require data to be fetched from APIs.

### Cons

- Higher server overhead because every request is processed on the server.
- More complex to set up because it requires a server-side framework that support SSR.
- Less interactive because interactions require additional server requests.

### Best for

- Applications with content that changes frequently.
- Applications with dynamic data that needs to be processed on the server before sending the response.

## 4. Static site generation ( SSG )

- Static site generation ( SSG ) is a process in which web pages are pre-built as static files during the building process and served to the client as static HTML pages.
- The server sends static HTML pages to the client, which includes all the content, without processing any data on the server.

### Pros

- Very fast and effecient because static pages can be served from a CDN or cache.
- Lower server overhead because the server only needs to serve static files.
- Can be deployed on a static file host or serverless environments like AWS Lambda.

### Cons

- Not suitable for dynamic content that changes frequently.
- Interactions require additional client-side javascipt.

### Best for

- Application with mostly static content and few interactions.
- Applications with limited interactivity.

## 5. Incremental static regeneration ( ISR )

- Incremental static regeneration ( ISR ) is a hybrid approach between SSG and SSR, where pages are pre-rendered as static HTML pages during the build process, and then the content is regenerated periodically or on-demand as required.

### Pros

- Faster time-to-content because static pages are served initially, but content can be updated quickly.
- Lower server overhead because static pages can be served from a CDN or cache, and dynamic content is regenerated only when required.

### Cons

- Limited dynamic content because content regeneration requires a server request.
- Requires a complex caching strategy to ensure that stale content is not served to clients.

### Situations:

- Applications with content that changes frequently but can tolerate some latency.
- Applications with limited dynamic content.

## 6. Islands

- The Island rendering pattern refers to rendering parts of the page on the server while other parts are rendered on the client-side.
- The server renders the critical content, while the client fetches the rest of the content.
- The server-side rendering can improve the initial page load speed and improve SEO.
- The client-side rendering can improve the interactivity and reduce server overhead.

### Pros

- Faster page load times because the server renders critical content while the client fetches the rest.
- Works well for applications that require partial server-side rendering and partial client-side rendering.

### Cons

- More complex to set up because it requires a hybrid framework that can support both server-side and client-side rendering.
- May result in inconsistencies if the server and client render different versions of the content.

### Best for

- Applications with dynamic content that require some server-side processing.
- Applications that require a fast initial page load.

## 7. Streaming SSR

- The server sends the HTML response in a streaming fashion, which enables the client to start rendering the content as soon as possible.
- The client can see content being rendered progressively, which improves the user experience.

### Pros

- Improved time-to-content because the client can start rendering the content while the server is still processing the request.
- Better user experience because the client can see content being rendered progressively.

### Cons

- More complex to set up because it requires a server framework that supports streaming.

### Best for

- Applications with large pages or media that require a long time to load.
- Applications that require a smooth user experience with minimal waiting time.

# HTTP vs HTTPS

- HTTP (Hypertext Transfer Protocol) is the standard protocol for data transfer on the web but it is not encrypted, making it vulnerable to eavesdropping.  

- HTTPS (Secure) adds an encryption layer using SSL/TLS to protect data from being intercepted or tampered with. 

---

# HTTP Structure Diagram 
<img width="1334" height="416" alt="image" src="https://github.com/user-attachments/assets/f0b2fed1-1947-4642-830e-a8d6dfef5316" />

- Request Structure: Contains the Method (GET), Headers (like User-Agent), and Path. 

- Response Structure: Contains the Status Code (200 OK), Headers (like Content-Type), and the Body (Data).

---

# Practical Observation: HTTP Request and Response Structure 
<img width="1024" height="585" alt="image" src="https://github.com/user-attachments/assets/8992c9b8-dd8a-44d0-b455-94ab93b63740" />

HTTP Request and Response Analysis:

- Request URL: chrome://new-tab-page/ (The resource requested by the client). 

- Request Method: GET (The method used to retrieve data from the server). 

- Status Code: 200 OK (Indicates that the request was successful and the server returned the requested data). 

- Remote Address: Shows the IP address and port of the web server providing the resource.

---

# Recognize and explain the common HTTP methods and status codes : 
<img width="936" height="480" alt="unknown" src="https://github.com/user-attachments/assets/b5f80246-04c0-4912-992c-706786b321c4" />

These methods define the action to be performed on the resource. For example, GET was used to load the Google search page in my practical observation, while POST would be used if I were to submit a search query or a login form. 

<img width="936" height="601" alt="unknown" src="https://github.com/user-attachments/assets/fa60d311-89bd-46be-9415-5971249c8e16" />

Status codes are issued by the server in response to a client's request. As shown in my screenshot, the code 200 OK indicates a successful connection, while codes like 404 or 500 notify the user of client-side or server-side errors respectively. 

---

# Conclusion : 
Conclusion: Understanding the HTTP/HTTPS protocols, request structures, and status codes is fundamental for web development and API integration. This assignment demonstrates both the theoretical flow and the practical application of these web communications .




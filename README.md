# Loan-Mangement-Microcervices
 the Application Service sends a request to the Commercial Service to check the borrower's eligibility for the loan, and the Commercial Service responds with the eligibility score.
 Similarly, the Application Service sends the loan application data to the Risk Management Service for risk assessment, and the Risk Management Service responds with the loan approval status.

In addition to this, the Credit Service stores the generated credit agreement and amortization table in the database, which the Application Service can retrieve later if needed. 
And finally, the Notification Service receives the notification status from the Application Service and sends a notification to the borrower, which can be done using an email or a push notification service.
Technologies:
For this loan management module, we could use the following technologies:
`1.Docker: This is a containerization platform that would make it easy to package and deploy the microservices.`
`2.Kubernetes: This is a container orchestration platform that would make it easy to manage and scale the microservices.`
`3.Python/flask: This is a lightweight and flexible web framework that allows developers to easily create web services and APIs.`
`4.Tesseract OCR: This is an open-source OCR engine that could be used for the OCR capabilities required by the Commercial Service and the Risk Management Service.`

![Diagramme sans nom drawio](https://github.com/safaakdidi/Loan-Mangement-Microcervices/assets/96058782/cc6572b1-038a-41f1-86ce-d51471da62fa)

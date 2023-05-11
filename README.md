# Loan-Mangement-Microcervices
 the Application Service sends a request to the Commercial Service to check the borrower's eligibility for the loan, and the Commercial Service responds with the eligibility score.
 Similarly, the Application Service sends the loan application data to the Risk Management Service for risk assessment, and the Risk Management Service responds with the loan approval status.

In addition to this, the Credit Service stores the generated credit agreement and amortization table in the database, which the Application Service can retrieve later if needed. 
And finally, the Notification Service receives the notification status from the Application Service and sends a notification to the borrower, which can be done using an email or a push notification service.

![Diagramme sans nom drawio](https://github.com/safaakdidi/Loan-Mangement-Microcervices/assets/96058782/cc6572b1-038a-41f1-86ce-d51471da62fa)

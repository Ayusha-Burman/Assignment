### Project Description

<b>PII Detection API: </b> This Flask API is designed to analyze text paragraphs and identify personally identifiable information (PII) within them. The API exposes an endpoint that accepts POST requests with JSON payloads, processes the text, and returns a response containing an array of detected PII.

### Installation

Follow these steps to get the project up and running:

- <b>Installing depenedencies : </b>

  ```python
  pip install -r requirements.txt
  ```

  - <b>Initializing server : </b>

  ```python
  python main.py
  ```

### Typical Request Sent

Request:
  {

  "body": "Priyanshu Sharma is a Mtech CSE student from Jadavpur University. His hometown is in Asansol. He has completed Btech from Jadavpur University. He recently applied for a Driving License in West Bengal with the help of his ADHAAR and Voter Card. The ADHAAR number of Priyanshu is 4567000007865 and the Voter ID number is SYG882745586. But the problem is that the address in the adhaar and the voter id are different. So therefore he was advised to provide his PAN Card having PAN no- AKKJM7875665D and the Bank account statement with an account in State Bank Of India, the account number is 6356278255789."
}

### Response from the flask server

{
  "error": "nil",
  "pii_detected": {
    "aadhar_number": "4567000007865",
    "account_number": "6356278255789",
    "name": "Priyanshu",
    "pan_number": "AKKJM7875665D",
    "voter_id_number": "SYG882745586"
  }
}



from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def extract_pii(text):
    # Regular expressions for detecting PII
    name_pattern = re.compile(r'\b[A-Z][a-z]+\b')
    aadhar_pattern = re.compile(r'\b\d{10,16}\b')
    voter_id_pattern = re.compile(r'\b[A-Z]{3}\d{9}\b')
    pan_pattern = re.compile(r'\b[A-Z0-9]{13}\b')
    account_number_pattern = re.compile(r'\b\d{10,16}\b')

    # Extract PII from the text
    names = name_pattern.findall(text)
    aadhar_numbers = aadhar_pattern.findall(text)
    voter_ids = voter_id_pattern.findall(text)
    pan_numbers = pan_pattern.findall(text)
    account_numbers = account_number_pattern.findall(text)

    # Combine all detected PII
    pii_detected = {
        "name": names[0] if names else None,
        "aadhar_number": aadhar_numbers[0] if aadhar_numbers else None,
        "voter_id_number": voter_ids[0] if voter_ids else None,
        "pan_number": pan_numbers[1] if pan_numbers else None,
        "account_number": account_numbers[1] if account_numbers else None
    }

    return pii_detected


@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data['body']
        pii_detected = extract_pii(text)

        response = {
            "pii_detected": pii_detected,
            "error": "nil"
        }

        return jsonify(response)

    except Exception as e:
        response = {
            "pii_detected": [],
            "error": str(e)
        }

        return jsonify(response)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
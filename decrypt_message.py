import json
import base64
import os

def decrypt_pubsub_message(pubsub_message):
    # Extract the 'data' field from the Pub/Sub message
    message_data = pubsub_message.get('message', {}).get('data', '')

    # Decode the base64 data
    decoded_data = base64.b64decode(message_data).decode('utf-8')

    # Parse the JSON
    parsed_data = json.loads(decoded_data)

    return parsed_data

# Example usage
if __name__ == "__main__":
    # Define the paths
    input_file_path = './pubsub_message_encrypted.json'
    output_file_path = './pubsub_message_decrypted.json'

    # Read the example Pub/Sub message from the JSON file
    with open(input_file_path, 'r') as file:
        pubsub_message = json.load(file)

    # Decrypt and parse the message
    decrypted_message = decrypt_pubsub_message(pubsub_message)

    # Save the decrypted message to a new JSON file
    with open(output_file_path, 'w') as file:
        json.dump(decrypted_message, file, indent=2)

    print("\nDecrypted message content:")
    print(json.dumps(decrypted_message, indent=2))

# mGanik Webhook Processor

This project processes webhook events from mGanik's messaging system in base64 encoding.

## Overview

The system receives encrypted Pub/Sub messages containing chat interaction data from mGanik's WhatsApp integration. It decrypts and parses these messages to extract relevant information for further processing.

## Key Components

1. `decrypt_message.py`: Contains the logic to decrypt and parse Pub/Sub messages.
2. `pubsub_message_encrypted.json`: Example of an encrypted Pub/Sub message.
3. `pubsub_message_decrypted.json`: Example of a decrypted and parsed message.
4. `pubssub_message_bigquery.json`: Example of a decrypted and parsed message which manually query from BigQuery.

## Usage

To decrypt a message:

1. Run `decrypt_message.py` to decrypt the message and save it to `pubsub_message_decrypted.json`.
2. It will overwrite the file if it already exists.
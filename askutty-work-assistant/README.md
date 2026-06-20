# Askutty Work Assistant

Mobile-first work entry assistant for curtain / DFC / invoice data entry.

## Current Version

v0.1 static PWA prototype.

## Features

- Mobile voice input using browser speech recognition
- Image capture and OCR using browser-side Tesseract.js CDN
- Manual field correction
- Save rows locally in browser storage
- Copy one row as Excel-ready tab-separated text
- Copy all rows for Excel paste
- Export CSV

## Fields

- S/No
- TR Number
- Order No
- DFC No
- Customer Name
- Customer Contact
- No. of Packets
- Joining
- Alteration Height Reduction
- Alteration Height Extension
- Stitching
- Express
- Tie Back
- B-Out
- Eyelets
- Remarks

## Safety / Privacy

This prototype stores saved rows only in the browser local storage. It does not include any Microsoft/OneDrive token or private API key.

## Next Stages

1. Improve voice command parser for Tamil/Tanglish work phrases.
2. Add better invoice OCR field mapping.
3. Add authenticated OneDrive / Microsoft Graph sync only after explicit user setup.
4. Add NOVA/QBIT decision layer for field validation.

Universal Dragon Aslam continues.

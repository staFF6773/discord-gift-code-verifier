# Discord Gift Code Verifier

This Python script verifies Discord gift codes using the Discord API.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library (you can install it using `pip install requests`)

### Obtaining Your Discord Account Token

1. **Open Discord**:
   - Launch the Discord application or go to the [Discord web app](https://discord.com/).

2. **Open Developer Tools**:
   - Right-click anywhere on the Discord page and select **Inspect** (or press `Ctrl + Shift + I` on Windows/Linux or `Cmd + Option + I` on macOS).

3. **Go to the Network Tab**:
   - In the Developer Tools, click on the **Network** tab.

4. **Reload Discord**:
   - Refresh the page (press `F5` or click the refresh button). This will populate the network requests.

5. **Find a WebSocket Connection**:
   - Look for any request that has the type "WS" (WebSocket). You can filter the requests by typing "websocket" in the filter box.

6. **Inspect the WebSocket**:
   - Click on the WebSocket connection and go to the **Headers** tab.

7. **Locate the Authorization Token**:
   - In the request headers, look for `Authorization`. The value next to it is your Discord account token.

8. **Copy Your Token**:
   - Copy the token value (it will look like a long string of letters and numbers).

### Using the Script

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

# Documentation for folder: .

## `./mcp_sever.ipynb`
```python
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0bf12621",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv \n",
    "from langchain_google_genai import ChatGoogleGenerativeAI #type:ignore\n",
    "from langchain_core.messages import HumanMessage, SystemMessage\n",
    "\n",
    "load_dotenv()\n",
    "google_api_key = os.getenv(\"GOOGLE_API_KEY\")\n",
    "if not google_api_key:\n",
    "    print(\"Cảnh báo: GOOGLE_API_KEY không được tìm thấy trong biến môi trường.\")\n",
    "    print(\"Vui lòng đảm bảo bạn đã đặt nó trong file .env hoặc thiết lập thủ công.\")\n",
    "\n",
    "llm = ChatGoogleGenerativeAI(model=\"gemini-2.0-flash\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f747ce54",
   "metadata": {},
   "source": [
    "# Connect to Google Sheet\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "849e915d",
   "metadata": {},
   "outputs": [
    {
     "ename": "RefreshError",
     "evalue": "('invalid_grant: Invalid JWT Signature.', {'error': 'invalid_grant', 'error_description': 'Invalid JWT Signature.'})",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRefreshError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 10\u001b[0m\n\u001b[1;32m      7\u001b[0m client \u001b[38;5;241m=\u001b[39m gspread\u001b[38;5;241m.\u001b[39mauthorize(creds)\n\u001b[1;32m      9\u001b[0m \u001b[38;5;66;03m# Mở Google Sheet\u001b[39;00m\n\u001b[0;32m---> 10\u001b[0m sheet \u001b[38;5;241m=\u001b[39m \u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mopen\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mDaily Report\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39msheet1\n\u001b[1;32m     11\u001b[0m \u001b[38;5;66;03m# Lấy dữ liệu hàng đầu tiên\u001b[39;00m\n\u001b[1;32m     12\u001b[0m data \u001b[38;5;241m=\u001b[39m sheet\u001b[38;5;241m.\u001b[39mget_all_values()\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/gspread/client.py:145\u001b[0m, in \u001b[0;36mClient.open\u001b[0;34m(self, title, folder_id)\u001b[0m\n\u001b[1;32m    129\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mopen\u001b[39m(\u001b[38;5;28mself\u001b[39m, title: \u001b[38;5;28mstr\u001b[39m, folder_id: Optional[\u001b[38;5;28mstr\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Spreadsheet:\n\u001b[1;32m    130\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Opens a spreadsheet.\u001b[39;00m\n\u001b[1;32m    131\u001b[0m \n\u001b[1;32m    132\u001b[0m \u001b[38;5;124;03m    :param str title: A title of a spreadsheet.\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    143\u001b[0m \u001b[38;5;124;03m    >>> gc.open('My fancy spreadsheet')\u001b[39;00m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 145\u001b[0m     spreadsheet_files, response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_list_spreadsheet_files\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtitle\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfolder_id\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    146\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    147\u001b[0m         properties \u001b[38;5;241m=\u001b[39m finditem(\n\u001b[1;32m    148\u001b[0m             \u001b[38;5;28;01mlambda\u001b[39;00m x: x[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m==\u001b[39m title,\n\u001b[1;32m    149\u001b[0m             spreadsheet_files,\n\u001b[1;32m    150\u001b[0m         )\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/gspread/client.py:118\u001b[0m, in \u001b[0;36mClient._list_spreadsheet_files\u001b[0;34m(self, title, folder_id)\u001b[0m\n\u001b[1;32m    115\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m page_token:\n\u001b[1;32m    116\u001b[0m     params[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpageToken\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m page_token\n\u001b[0;32m--> 118\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhttp_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mget\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    119\u001b[0m response_json \u001b[38;5;241m=\u001b[39m response\u001b[38;5;241m.\u001b[39mjson()\n\u001b[1;32m    120\u001b[0m files\u001b[38;5;241m.\u001b[39mextend(response_json[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfiles\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/gspread/http_client.py:114\u001b[0m, in \u001b[0;36mHTTPClient.request\u001b[0;34m(self, method, endpoint, params, data, json, files, headers)\u001b[0m\n\u001b[1;32m    104\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mrequest\u001b[39m(\n\u001b[1;32m    105\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m    106\u001b[0m     method: \u001b[38;5;28mstr\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    112\u001b[0m     headers: Optional[MutableMapping[\u001b[38;5;28mstr\u001b[39m, \u001b[38;5;28mstr\u001b[39m]] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m    113\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Response:\n\u001b[0;32m--> 114\u001b[0m     response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msession\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    115\u001b[0m \u001b[43m        \u001b[49m\u001b[43mmethod\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmethod\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    116\u001b[0m \u001b[43m        \u001b[49m\u001b[43murl\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mendpoint\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    117\u001b[0m \u001b[43m        \u001b[49m\u001b[43mjson\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mjson\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    118\u001b[0m \u001b[43m        \u001b[49m\u001b[43mparams\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    119\u001b[0m \u001b[43m        \u001b[49m\u001b[43mdata\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mdata\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    120\u001b[0m \u001b[43m        \u001b[49m\u001b[43mfiles\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfiles\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    121\u001b[0m \u001b[43m        \u001b[49m\u001b[43mheaders\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    122\u001b[0m \u001b[43m        \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    123\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    125\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mok:\n\u001b[1;32m    126\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/auth/transport/requests.py:535\u001b[0m, in \u001b[0;36mAuthorizedSession.request\u001b[0;34m(self, method, url, data, headers, max_allowed_time, timeout, **kwargs)\u001b[0m\n\u001b[1;32m    532\u001b[0m remaining_time \u001b[38;5;241m=\u001b[39m max_allowed_time\n\u001b[1;32m    534\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m TimeoutGuard(remaining_time) \u001b[38;5;28;01mas\u001b[39;00m guard:\n\u001b[0;32m--> 535\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcredentials\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbefore_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mauth_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mmethod\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_headers\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    536\u001b[0m remaining_time \u001b[38;5;241m=\u001b[39m guard\u001b[38;5;241m.\u001b[39mremaining_timeout\n\u001b[1;32m    538\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m TimeoutGuard(remaining_time) \u001b[38;5;28;01mas\u001b[39;00m guard:\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/auth/credentials.py:239\u001b[0m, in \u001b[0;36mCredentials.before_request\u001b[0;34m(self, request, method, url, headers)\u001b[0m\n\u001b[1;32m    237\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_non_blocking_refresh(request)\n\u001b[1;32m    238\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 239\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_blocking_refresh\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    241\u001b[0m metrics\u001b[38;5;241m.\u001b[39madd_metric_header(headers, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_metric_header_for_usage())\n\u001b[1;32m    242\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapply(headers)\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/auth/credentials.py:202\u001b[0m, in \u001b[0;36mCredentials._blocking_refresh\u001b[0;34m(self, request)\u001b[0m\n\u001b[1;32m    200\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_blocking_refresh\u001b[39m(\u001b[38;5;28mself\u001b[39m, request):\n\u001b[1;32m    201\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mvalid:\n\u001b[0;32m--> 202\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrefresh\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/oauth2/service_account.py:448\u001b[0m, in \u001b[0;36mCredentials.refresh\u001b[0;34m(self, request)\u001b[0m\n\u001b[1;32m    446\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m    447\u001b[0m     assertion \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_authorization_grant_assertion()\n\u001b[0;32m--> 448\u001b[0m     access_token, expiry, _ \u001b[38;5;241m=\u001b[39m \u001b[43m_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mjwt_grant\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    449\u001b[0m \u001b[43m        \u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_token_uri\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43massertion\u001b[49m\n\u001b[1;32m    450\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    451\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtoken \u001b[38;5;241m=\u001b[39m access_token\n\u001b[1;32m    452\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mexpiry \u001b[38;5;241m=\u001b[39m expiry\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/oauth2/_client.py:299\u001b[0m, in \u001b[0;36mjwt_grant\u001b[0;34m(request, token_uri, assertion, can_retry)\u001b[0m\n\u001b[1;32m    275\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Implements the JWT Profile for OAuth 2.0 Authorization Grants.\u001b[39;00m\n\u001b[1;32m    276\u001b[0m \n\u001b[1;32m    277\u001b[0m \u001b[38;5;124;03mFor more details, see `rfc7523 section 4`_.\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    295\u001b[0m \u001b[38;5;124;03m.. _rfc7523 section 4: https://tools.ietf.org/html/rfc7523#section-4\u001b[39;00m\n\u001b[1;32m    296\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    297\u001b[0m body \u001b[38;5;241m=\u001b[39m {\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124massertion\u001b[39m\u001b[38;5;124m\"\u001b[39m: assertion, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgrant_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: _JWT_GRANT_TYPE}\n\u001b[0;32m--> 299\u001b[0m response_data \u001b[38;5;241m=\u001b[39m \u001b[43m_token_endpoint_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m    300\u001b[0m \u001b[43m    \u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    301\u001b[0m \u001b[43m    \u001b[49m\u001b[43mtoken_uri\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    302\u001b[0m \u001b[43m    \u001b[49m\u001b[43mbody\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    303\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcan_retry\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcan_retry\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    304\u001b[0m \u001b[43m    \u001b[49m\u001b[43mheaders\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m{\u001b[49m\n\u001b[1;32m    305\u001b[0m \u001b[43m        \u001b[49m\u001b[43mmetrics\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mAPI_CLIENT_HEADER\u001b[49m\u001b[43m:\u001b[49m\u001b[43m \u001b[49m\u001b[43mmetrics\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtoken_request_access_token_sa_assertion\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    306\u001b[0m \u001b[43m    \u001b[49m\u001b[43m}\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    307\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    309\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    310\u001b[0m     access_token \u001b[38;5;241m=\u001b[39m response_data[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maccess_token\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/oauth2/_client.py:270\u001b[0m, in \u001b[0;36m_token_endpoint_request\u001b[0;34m(request, token_uri, body, access_token, use_json, can_retry, headers, **kwargs)\u001b[0m\n\u001b[1;32m    259\u001b[0m response_status_ok, response_data, retryable_error \u001b[38;5;241m=\u001b[39m _token_endpoint_request_no_throw(\n\u001b[1;32m    260\u001b[0m     request,\n\u001b[1;32m    261\u001b[0m     token_uri,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    267\u001b[0m     \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs\n\u001b[1;32m    268\u001b[0m )\n\u001b[1;32m    269\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m response_status_ok:\n\u001b[0;32m--> 270\u001b[0m     \u001b[43m_handle_error_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse_data\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mretryable_error\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    271\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m response_data\n",
      "File \u001b[0;32m~/mcp-sever/mcp_sever/lib/python3.10/site-packages/google/oauth2/_client.py:69\u001b[0m, in \u001b[0;36m_handle_error_response\u001b[0;34m(response_data, retryable_error)\u001b[0m\n\u001b[1;32m     66\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m (\u001b[38;5;167;01mKeyError\u001b[39;00m, \u001b[38;5;167;01mValueError\u001b[39;00m):\n\u001b[1;32m     67\u001b[0m     error_details \u001b[38;5;241m=\u001b[39m json\u001b[38;5;241m.\u001b[39mdumps(response_data)\n\u001b[0;32m---> 69\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exceptions\u001b[38;5;241m.\u001b[39mRefreshError(\n\u001b[1;32m     70\u001b[0m     error_details, response_data, retryable\u001b[38;5;241m=\u001b[39mretryable_error\n\u001b[1;32m     71\u001b[0m )\n",
      "\u001b[0;31mRefreshError\u001b[0m: ('invalid_grant: Invalid JWT Signature.', {'error': 'invalid_grant', 'error_description': 'Invalid JWT Signature.'})"
     ]
    }
   ],
   "source": [
    "import gspread #type:ignore\n",
    "from oauth2client.service_account import ServiceAccountCredentials #type:ignore\n",
    "\n",
    "# Xác thực\n",
    "scope = [\"https://spreadsheets.google.com/feeds\", \"https://www.googleapis.com/auth/drive\"]\n",
    "creds = ServiceAccountCredentials.from_json_keyfile_name(\"/home/hai/mcp-sever/gen-lang-client-0447346298-52beea69cd6f.json\", scope)\n",
    "client = gspread.authorize(creds)\n",
    "\n",
    "# Mở Google Sheet\n",
    "sheet = client.open(\"Daily Report\").sheet1\n",
    "# Lấy dữ liệu hàng đầu tiên\n",
    "data = sheet.get_all_values()\n",
    "print(data[0])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f10c6a6d",
   "metadata": {},
   "source": [
    "# Create tool for Google Sheets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2dd9b38f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.tools import Tool\n",
    "\n",
    "def read_sheet_data(query: str) -> str:\n",
    "    # có thể thêm logic xử lý `query` để đọc theo yêu cầu\n",
    "    values = sheet.get_all_values()\n",
    "    return str(values[:5])  # trả về 5 dòng đầu\n",
    "\n",
    "# Định nghĩa các công cụ\n",
    "def writing_document_markdown(query: str) -> str:\n",
    "    \"\"\"\n",
    "    Tạo document markdown cho toàn bộ thư mục hiện tại và ghi ra file.\n",
    "    Nếu query là đường dẫn file, sẽ ghi vào đó. Nếu không, chỉ trả về chuỗi markdown.\n",
    "    Nếu không có query, sẽ ghi vào file mặc định là \"documentation.md\" trong thư mục hiện tại.\n",
    "    \"\"\"\n",
    "    # Nếu query là đường dẫn file, tách ra\n",
    "    if query and query.endswith(\".md\"):\n",
    "        folder_path = \".\"\n",
    "        output_file = query\n",
    "    elif query:\n",
    "        folder_path = query\n",
    "        output_file = None\n",
    "    else:\n",
    "        folder_path = \".\"\n",
    "        output_file = \"documentation.md\"\n",
    "\n",
    "    markdown = \"# Documentation for folder: {}\\n\\n\".format(folder_path)\n",
    "    for root, dirs, files in os.walk(folder_path):\n",
    "        for file in files:\n",
    "            if file.endswith(\".ipynb\") or file.endswith(\".py\"):\n",
    "                file_path = os.path.join(root, file)\n",
    "                markdown += f\"## `{file_path}`\\n\"\n",
    "                try:\n",
    "                    with open(file_path, \"r\", encoding=\"utf-8\") as f:\n",
    "                        content = f.read()\n",
    "                    markdown += \"```python\\n\" + content[:] + \"\\n```\\n\\n\"\n",
    "                except Exception as e:\n",
    "                    markdown += f\"Không thể đọc file: {e}\\n\\n\"\n",
    "\n",
    "    if output_file:\n",
    "        try:\n",
    "            os.makedirs(os.path.dirname(output_file), exist_ok=True)\n",
    "            with open(output_file, \"w\", encoding=\"utf-8\") as f:\n",
    "                f.write(markdown)\n",
    "            return f\"Đã ghi document vào {output_file}\"\n",
    "        except Exception as e:\n",
    "            return f\"Lỗi khi ghi file: {e}\"\n",
    "    return markdown\n",
    "\n",
    "google_sheet_tool = Tool(\n",
    "    name=\"GoogleSheetReader\",\n",
    "    func=read_sheet_data,\n",
    "    description=\"Dùng để đọc dữ liệu từ Google Sheets\"\n",
    ")\n",
    "document_tool = Tool(\n",
    "    name=\"DocumentCreator\",\n",
    "    func=writing_document_markdown,\n",
    "    description=\"Tạo document markdown cho toàn bộ thư mục (truyền vào đường dẫn thư mục nếu muốn).\"\n",
    ")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f19d40d0",
   "metadata": {},
   "source": [
    "# Run Agent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2ee8ee79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[1m> Entering new AgentExecutor chain...\u001b[0m\n",
      "\u001b[32;1m\u001b[1;3mTôi cần tạo một document markdown cho thư mục hiện tại, và lưu nó vào đường dẫn `/home/hai/mcp-sever/doc/test.md`. Để làm điều này, tôi sẽ sử dụng công cụ `DocumentCreator`.\n",
      "\n",
      "Action: DocumentCreator\n",
      "Action Input: /home/hai/mcp-sever/doc/test.md\u001b[0m\n",
      "Observation: \u001b[36;1m\u001b[1;3mĐã ghi document vào /home/hai/mcp-sever/doc/test.md\u001b[0m\n",
      "Thought:\u001b[32;1m\u001b[1;3mI have successfully created the document.\n",
      "Final Answer: Đã ghi document vào /home/hai/mcp-sever/doc/test.md\u001b[0m\n",
      "\n",
      "\u001b[1m> Finished chain.\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Đã ghi document vào /home/hai/mcp-sever/doc/test.md'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from langchain.agents import initialize_agent, AgentType\n",
    "from langchain_google_genai import ChatGoogleGenerativeAI\n",
    "\n",
    "llm = ChatGoogleGenerativeAI(model=\"gemini-2.0-flash\")\n",
    "\n",
    "agent = initialize_agent(\n",
    "    tools=[document_tool],\n",
    "    llm=llm,\n",
    "    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,\n",
    "    verbose=True\n",
    ")\n",
    "\n",
    "agent.run(\"Viết document cho tôi ở thư mục hiện tại dưới dạng markdown và truyền vào Document ở thư mục '/home/hai/mcp-sever/doc/test.md'\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49190ea0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "mcp_sever",
   "language": "python",
   "name": "mcp_sever"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

```

## `./.ipynb_checkpoints/Untitled-checkpoint.ipynb`
```python
{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

```


from django.shortcuts import render, redirect
from pathlib import Path
import uuid
import json
import hmac
import hashlib
import base64
import environ
import requests

# Create your views here.
def index(request):
    return render(request,"index.html")

#連接.env變數
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()

#line pay API header
def create_headers(body, uri):
    channel_id = env('LINE_CHANNEL_ID')
    secret_key = env('LINE_CHANNEL_SECRET_KEY')
    nonce = str(uuid.uuid4())
    #header 轉換成json格式
    body_to_json = json.dumps(body)

    # 組裝簽名
    message = secret_key + uri + body_to_json + nonce
    
    binary_message = message.encode()
    binary_secret_key = secret_key.encode()
    
    #雜湊
    hash = hmac.new(binary_secret_key, binary_message, hashlib.sha256)
    signature = base64.b64encode(hash.digest()).decode()

    headers = {
        "Content-Type": "application/json",
        "X-LINE-ChannelId":channel_id,
        "X-LINE-ChannelSecret":secret_key,
        "X-LINE-Authorization-Nonce": nonce,
        "X-LINE-Authorization": signature,
    }
    return headers


#line pay API body
def request_payment(request):
    if request.method == "POST":
        # 設定訂單與付款資訊
        order_id = f"order_{str(uuid.uuid4())}"
        package_id = f"package_{str(uuid.uuid4())}"
        payload = {
            'amount': 399,
            'currency': 'TWD',
            'orderId': order_id,
            'packages': [{
                'id': package_id,
                'amount': 399,
                'products': [{
                    'id': '1',
                    'name': '方案Ｂ超好揪',
                    'quantity': 1,
                    'price': 399,
                }]
            }],
            'redirectUrls': {
                'confirmUrl': f"https://{env('HOSTNAME')}/payment/confirm",
                'cancelUrl': f"https://{env('HOSTNAME')}/payment/cancel"
            }
        }

    # 發送 API 請求
        uri = env('LINE_REQUEST_URL')
        headers = create_headers(payload, uri)
        url = f"{env('LINE_SANDBOX_URL')}{uri}"
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # 根據狀態，處理回應
        if response.status_code == 200:
            data = response.json()
            if data['returnCode'] == '0000':
                return redirect(data['info']['paymentUrl']['web'])
            else:
                return render(request, "payment/error.html", {"message": data['returnMessage']})
        else:
            return render(request, "payment/error.html", {"message": f"Error: {response.status_code}"})
   
    return render(request, "payment/checkout.html")
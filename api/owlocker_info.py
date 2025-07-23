import requests

def handler(request):
    try:
        r = requests.get('https://owlocker.com/api/info', timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}, 500
import requests

def handler(request):
    site_no = request.args.get('site_no')
    if not site_no:
        return {"error": "缺少 site_no"}, 400
    try:
        r = requests.get(f'https://owlocker.com/api/locker/{site_no}', timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}, 500
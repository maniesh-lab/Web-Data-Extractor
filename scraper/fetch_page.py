import requests

def fetch_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Wikipedia may be slow or unreachable.")
        return None

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or could not reach the site.")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"Error: Bad response from server — {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Something unexpected went wrong — {e}")
        return None
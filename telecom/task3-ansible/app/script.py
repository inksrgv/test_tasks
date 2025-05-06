import requests
import logging
from requests.exceptions import RequestException, Timeout, ConnectionError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def make_request(status_code):
    url = f"https://httpstat.us/{status_code}"
    try:
        response = requests.get(url, timeout=5)
        status_class = response.status_code // 100
        
        if status_class in [1, 2, 3]:
            logger.info(f"Успешный запрос {status_code}: {response.text.strip()}")
        elif status_class in [4, 5]:
            logger.error(f"Ошибка {status_code}: {response.text.strip()}")
            
        return response.status_code, response.text.strip()
        
    except Timeout:
        logger.error(f"Таймаут при запросе {status_code}: сервер не ответил за 5 секунд")
    except ConnectionError:
        logger.error(f"Ошибка подключения при запросе {status_code}: сервер недоступен")
    except RequestException as e:
        logger.error(f"Ошибка запроса {status_code}: {str(e)}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка при запросе {status_code}: {str(e)}")

def main():
    test_codes = [101, 200, 300, 404, 501]
    
    for code in test_codes:
        make_request(code)

if __name__ == "__main__":
    main()
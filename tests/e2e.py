from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(port):
    driver = webdriver.Chrome()
    driver.get(f"http://127.0.0.1:{port}/score")
    score = driver.find_element(By.ID, "score").text
    if score.isnumeric() is False:
        print("Score is not a number")
        return False
    if 1 <= int(score) <= 1000:
        print("Score is within the acceptable range")
        return True
    else:
        print("Score is not within the acceptable range")
        return False


def main_function():
    if test_scores_service("8777") is True:
        return 0
    else:
        return -1


if __name__ == "__main__":
    exit(main_function())

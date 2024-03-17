from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get(f"http://127.0.0.1:8777/score")
    score = driver.find_element(By.ID, "score").text
    if score.isnumeric() is False:
        print("Score is not a number")
        return False
    if 1 < int(score) < 1000:
        return True
    else:
        print("Score is not within the acceptable range")
        return False


def main_function():
    if test_scores_service() is True:
        return 0
    else:
        return -1


main_function()



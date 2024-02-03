from app import welcome, start_play
import utils
try:
    welcome()
    utils.screen_cleaner()
    start_play()
except Exception as error:
    utils.bad_return_code = error

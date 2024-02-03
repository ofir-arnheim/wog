import utils


# A function used to add up the scores from all games.
# If file only has numbers, we read and add up existing score
# If file does not exist we create it with a+
def add_score(difficulty):
    points_of_winning = (int(difficulty) * 3) + 5
    score_file = open(utils.scores_file_name, "a+", encoding="UTF-8")
    content = score_file.read()
    if content.isdigit():
        points = int(content) + points_of_winning
    else:
        points = points_of_winning
    # We truncate before adding our content
    score_file.truncate()
    score_file.write(str(points))
    score_file.close()


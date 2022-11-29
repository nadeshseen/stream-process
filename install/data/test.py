import pandas as pd

def avg_percentage(game_id, ft_attempt_id, team, result):
    """
    :param game_id: (list) The ID of the game. 
    :param ft_attempt_id: (list) The ID of the free throw attempt for a given game.
    :param team: (list) Which team took the free throw.
    :param result: (list) The result of the free throw, which is either missed or made.
    :returns: (float) The mean value of the percentages (0.0-100.0) of free throws that
               each team scored in each game.
    """
    df = pd.DataFrame({"game_id":[], "ft_attempt_id":[], "team":[], "result":[]})
    df["game_id"] = game_id
    print(df)
    return None

#For example, with the parameters below, the function should return 58.33
print(avg_percentage(
    [1, 1, 1, 1, 2, 2],
    [1, 2, 3, 4, 1, 2],
    ['home','home','away','home','away','home'],
    ['made','missed','made','missed','missed','made']
))
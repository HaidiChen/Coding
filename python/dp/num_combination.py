def num_combinations_for_final_score(final_score, individual_play_score):
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_score]

    for i in range(len(individual_play_score)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i - 1][j] if i >= 1 else 0)
            with_this_play = num_combination_for_score[i][j - individual_play_score[i]] if j >= individual_play_score[i] else 0
            num_combinations_for_score[i][j] = with_this_play + without_this_play

    return num_combinations_for_score[-1][-1]

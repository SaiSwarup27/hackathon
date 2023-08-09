file_path = "data.txt"
threshold_score = 1

def analysis():
    freq_dict = dict()
    with open(file_path, "r") as f:
        r = f.readlines()
        l = len(r)
    unique_sentence = set(r)
    for i in unique_sentence:
        freq_dict[i] = r.count(i)
    freq_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}
    score_dict = dict()
    for i in freq_dict:
        score = (freq_dict[i]/l) * 100
        if(score>threshold_score):
            score_dict[i] = score
        print(f"{i} - score: {score}")
    return score_dict

score_dict = analysis()















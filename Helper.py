import numpy as np


# Affiche les résultats suggérés pour chaque requête
def print_queries_results(documents, documents_processed, queries, queries_processed, scores):
    nb_results_to_show = 3
    for i in range(0, nb_results_to_show):
        print(f"\n########### Query n°{i + 1} ###########")
        print(f"Query : \"{queries[i]}\" :")
        print(f"Query processed : \"{queries_processed[i]}\" :")
        arr = np.array(scores[i])
        res = arr.argsort()[-3:][::-1]
        print(f"--> sorted : {sorted(scores[i], reverse=True)}")
        for idx, r in enumerate(res):
            print(f"--> Result n°{idx + 1} (doc_id = [{r + 1}], score = {arr[r]}) : {documents[r].strip()}")
            print(f"--> Result processed : {documents_processed[r]}")


# Calcule et affiche le taux de succès des résultats pour chaque requête
def print_success_rate(queries, results, scores):
    nb_results_extracted = 10
    average_success = 0
    for i in range(0, len(queries)):
        # print(f"\n########### Query n°{i+1} ###########")
        arr = np.array(scores[i])
        res = arr.argsort()[-nb_results_extracted:][::-1]
        nb_results_in_common = 0
        for idx, r in enumerate(res):
            if i + 1 in results and r + 1 in results[i + 1]:
                nb_results_in_common += 1
        success_rate = 100
        if i + 1 in results:
            success_rate = nb_results_in_common / (
                nb_results_extracted if nb_results_extracted <= len(results[i + 1]) else len(results[i + 1])) * 100
        print(f"Query n°{i + 1} --> success rate : {success_rate} %")
        average_success += success_rate
    average_success /= len(queries)
    print(f"\nAverage success rate : {average_success:.2f} %")

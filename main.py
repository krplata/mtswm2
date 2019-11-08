
import sys
import os
import feature_ranking as fr
import classifier as clsf


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def basic_rank():
    csv_path = os.path.join(get_script_path(), 'data/brzuch_dane.csv')
    x, y = fr.load_data(csv_path)
    ranking = fr.rank_features(x, y, sort=True)
    fr.pretty_print_ranking(ranking)


def run_experiment(x, y, upper_bound):
    results = []
    for i in range(1, upper_bound):
        new_x, new_y = fr.rank_n_transform(x, y, i)
        partial_res = clsf.run_grid_search(new_x, new_y)
        avg_test = clsf.get_avg_test_score(partial_res)
        results.append((i, i, avg_test))
    clsf.dump_to_latex(results, ['L.P.', 'Liczba cech', 'Jakość klasyfikacji [\%]'])


def main():
    csv_path = os.path.join(get_script_path(), 'data/brzuch_dane.csv')
    x, y = fr.load_data(csv_path)
    run_experiment(x, y, 10)


if __name__ == '__main__':
    main()

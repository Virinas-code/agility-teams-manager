import os
import modules.results
import modules.subshared

for file in os.walk("../Résultats"):
    parser: modules.results.ResultsParse = modules.results.ResultsParse()
    use_file: bool = False
    if file[2] and file[2][0][-5:] == ".html":
        print("read", file[1], file[2][0])
        with open(file[0] + "/" + file[2][0]) as file_obj:
            results = parser.parse(file_obj.read())
        modules.subshared.results.import_results(results, 2)
        ranks = modules.subshared.results.teams_ranking()

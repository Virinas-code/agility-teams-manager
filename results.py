import os
import modules.results
import modules.subshared

folder: str = input("Chemin: ")
day: int = int(input("Jour: "))

for file in os.walk(folder):
    parser: modules.results.ResultsParse = modules.results.ResultsParse()
    use_file: bool = False
    for subfile in file[2]:
        if subfile[-5:] == ".html":
            print("read", file[0] + "/" + subfile)
            with open(file[0] + "/" + subfile) as file_obj:
                results = parser.parse(file_obj.read())
            modules.subshared.results.import_results(results, day)
            ranks = modules.subshared.results.teams_ranking()

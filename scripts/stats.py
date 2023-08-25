import dataset


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def pretty_size(size):
    if size < 1000:
        return f"{size:.1f}"
    elif size < 1000 * 1000:
        return f"{(size / 1000.0):.1f}K"
    else:
        return f"{(size / 1000000.0):.1f}M"


def print_table(table):
    for row in table:
        print(", ".join([str(v) for v in row]))


def print_table_file(table, file):
    for row in table:
        file.write(", ".join([str(v) for v in row]) + "\n")


def build_table(cols: dict, prop):
    header = ["graph"]
    rows = dict()

    for col in cols.values():
        for row_name in col.keys():
            if row_name not in rows:
                rows[row_name] = []

    for name, col in cols.items():
        header.append(name)
        for row_name in rows:
            if row_name in col:
                rows[row_name].append(prop(col[row_name]))
            else:
                rows[row_name].append("none")

    return [header] + [[row_name] + row_data for row_name, row_data in rows.items()]


def output_stats(run_stats: dict):
    for algo, stats in run_stats.items():
        print("-" * 40 + f" {algo} " + "-" * 40)
        print_table(build_table(stats, lambda x: x.avg()))


def output_stats_overall(run_stats: dict, file_to_save):
    with open(file_to_save, 'w') as file:
        for algo, stats in run_stats.items():
            file.write(f"{algo}\n")
            print_table_file(build_table(stats, lambda x: x.avg()), file)


def output_stats_tool(run_stats: dict, file_to_save):
    with open(file_to_save, 'w') as file:
        file.write("graph,avg,sd,min,max\n")
        for algo, stats_algo in run_stats.items():
            file.write(f"{algo},,,,\n")
            for tool, stats_tool in stats_algo.items():
                file.write(f"{tool},,,,\n")
                for g, run in stats_tool.items():
                    file.write(f"{g},{run.avg()},{run.sd()},{run.minimum()},{run.maximum()}\n")


def output_stats_graphs(file_to_save):
    with open(file_to_save, 'w') as file:
        file.write(f"|Name|Vertices|Edges|Avg Deg|Sd Deg|Min Deg|Max Deg|Link|\n")
        file.write(f"|:---|-------:|----:|------:|-----:|------:|------:|---:|\n")
        for name, graph in dataset.GRAPHS_DATA.items():
            file.write(f"|"
                       f"{name}|"
                       f"{pretty_size(graph.dim[0])}|"
                       f"{pretty_size(graph.size)}|"
                       f"{graph.deg_avg:.1f}|"
                       f"{graph.deg_sd:.1f}|"
                       f"{graph.deg_min:.1f}|"
                       f"{graph.deg_max:.1f}|"
                       f"[link]({graph.link})|\n")

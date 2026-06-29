def render_table(jobs: list) -> str:
    headers = ["Stop", "Item", "Quantity", "Priority", "When"]

    rows = []
    for job in jobs:
        rows.append([
            str(job.get("stop", "")),
            str(job.get("item", "")),
            str(job.get("quantity", "")),
            str(job.get("priority", "")),
            str(job.get("when", ""))
        ])

    col_widths = []
    for i in range(len(headers)):
        max_width = max(
            len(headers[i]),
            *(len(str(row[i])) for row in rows)   
        )
        col_widths.append(max_width)

    header_row = " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
    separator_row = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    data_rows = []
    for row in rows:
        formatted = " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers)))
        data_rows.append(formatted)

    table = "\n".join([header_row, separator_row] + data_rows)
    return table

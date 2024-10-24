from rich.console import Console
from rich.table import Table

class Visualizer:
    def __init__(self):
        self.console = Console()

    def display_logs(self, logs):
        table = Table(title="HTTP Request Profiling Results")

        table.add_column("Method", justify="center")
        table.add_column("URL", justify="center")
        table.add_column("Response Time (s)", justify="center")

        for log in logs:
            table.add_row(log['method'], log['url'], f"{log['response_time']:.4f}")

        self.console.print(table)

from profiler import Profiler
from visualizer import Visualizer

def main():
    profiler = Profiler()
    visualizer = Visualizer()

    # Example of profiling requests
    urls = ["https://example.com", "https://httpbin.org/get"]
    
    for url in urls:
        profiler.profile_request("GET", url)

    visualizer.display_logs(profiler.logs)

if __name__ == "__main__":
    main()

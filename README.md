
![ReqTrace Logo](https://github.com/Joshdammy22/ReqTrace/blob/master/ReqTrace.png)

**ReqTrace** is a lightweight Python library designed to profile and visualize HTTP requests. It captures request details, such as response time, and presents the data in a user-friendly format, helping developers monitor, analyze, and optimize their application's HTTP interactions.

![Hero Image](https://github.com/Joshdammy22/ReqTrace/blob/master/bg.png) 


## Features

- Profiles both synchronous and asynchronous HTTP requests.
- Supports multiple HTTP methods (GET, POST, etc.).
- Captures and logs request duration for performance analysis.
- Visualizes profiling data in a clean, tabular format using the `rich` library.
- Extensible for additional request metrics (e.g., response size, headers).

## Installation

To install **ReqTrace**, first clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Joshdammy22/ReqTrace.git
cd ReqTrace
python -m venv reqtrace-env
source reqtrace-env/bin/activate   # On Windows: reqtrace-env\Scripts\activate
```

Next, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Below is a basic example of how to use **ReqTrace** to profile HTTP requests.

```python
from profiler import Profiler
from visualizer import Visualizer

def main():
    profiler = Profiler()
    visualizer = Visualizer()

    # Example of profiling GET requests
    urls = ["https://example.com", "https://httpbin.org/get"]
    
    for url in urls:
        profiler.profile_request("GET", url)

    visualizer.display_logs(profiler.logs)

if __name__ == "__main__":
    main()
```

## Functionality Overview

1. **Profiler Class**: Captures and logs HTTP request information such as the request method, URL, and response time.
2. **Visualizer Class**: Presents profiling data in a neat, readable table using the `rich` library.

## Example Output

```bash
+---------+-------------------------+-------------------+
| Method  | URL                     | Response Time (s)  |
+---------+-------------------------+-------------------+
| GET     | https://example.com      | 0.5321            |
| GET     | https://httpbin.org/get  | 0.2538            |
+---------+-------------------------+-------------------+
```

## Future Enhancements

- **Support for additional HTTP methods**: POST, PUT, DELETE, etc.
- **Asynchronous request support**: Using `httpx.AsyncClient`.
- **Advanced metrics**: Log response sizes, headers, and status codes.
- **Interactive dashboard**: Visualization via a web-based dashboard.

## Contributing

Contributions are welcome! If you'd like to contribute to **ReqTrace**, please fork the repository, create a new branch, and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using `httpx`, `requests`, and `rich`.
- Inspired by the need for better HTTP request profiling in Python.
``


from http.server import HTTPServer, BaseHTTPRequestHandler

class Portfolio(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Personal Portfolio</title>

            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    scroll-behavior: smooth;
                }

                body {
                    font-family: Arial, sans-serif;
                    background: #f4f7fb;
                    color: #222;
                }

                header {
                    background: #101d36;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }

                nav {
                    background: #243b60;
                    padding: 15px;
                    text-align: center;
                    position: sticky;
                    top: 0;
                }

                nav a {
                    color: white;
                    text-decoration: none;
                    margin: 15px;
                    font-weight: bold;
                }

                nav a:hover {
                    color: #00d4ff;
                }

                .hero {
                    background: linear-gradient(
                        120deg, #101d36, #176b87
                    );
                    color: white;
                    text-align: center;
                    padding: 90px 20px;
                }

                .hero h1 {
                    font-size: 42px;
                    margin-bottom: 15px;
                }

                .hero p {
                    font-size: 20px;
                }

                section {
                    padding: 50px 10%;
                    text-align: center;
                }

                section h2 {
                    color: #176b87;
                    margin-bottom: 25px;
                    font-size: 30px;
                }

                .card {
                    background: white;
                    padding: 25px;
                    margin: 15px auto;
                    max-width: 650px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px #0002;
                }

                .skills span {
                    display: inline-block;
                    background: #176b87;
                    color: white;
                    padding: 12px 20px;
                    margin: 8px;
                    border-radius: 20px;
                }

                .contact {
                    background: #101d36;
                    color: white;
                }

                .contact h2 {
                    color: #00d4ff;
                }

                footer {
                    background: #080f1d;
                    color: white;
                    text-align: center;
                    padding: 20px;
                }

                @media(max-width: 600px) {
                    nav a {
                        display: inline-block;
                        margin: 7px;
                    }

                    .hero h1 {
                        font-size: 30px;
                    }
                }
            </style>
        </head>

        <body>

            <header>
                <h1>MY PORTFOLIO</h1>
                <p>Welcome to My Personal Website</p>
            </header>

            <nav>
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#education">Education</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </nav>

            <div class="hero" id="home">
                <h1>Hello, I'm Your P YAKSITHA</h1>
                <p>B.Tech Student | Python Programmer</p>
                <p>Welcome to my personal portfolio!</p>
            </div>

            <section id="about">
                <h2>About Me</h2>
                <div class="card">
                    <p>
                        Hello! I am a B.Tech student interested
                        in programming, technology and web
                        development. I enjoy learning new skills
                        and developing creative projects.
                    </p>
                </div>
            </section>

            <section id="education">
                <h2>My Education</h2>
                <div class="card">
                    <h3>Bachelor of Technology</h3>
                    <p>College: JOY UNIVERSITY</p>
                    <p>Branch: CSE-AI-NXT WAVE</p>
                    <p>Year: 1st year</p>
                </div>
            </section>

            <section id="skills">
                <h2>My Technical Skills</h2>
                <div class="skills">
                    <span>Python</span>
                    <span>C Programming</span>
                    <span>HTML</span>
                    <span>CSS</span>
                    <span>Problem Solving</span>
                </div>
            </section>

            <section id="projects">
                <h2>My Projects</h2>

                <div class="card">
                    <h3>Personal Portfolio Website</h3>
                    <p>
                        A personal website created using Python
                        and web technologies.
                    </p>
                </div>

                <div class="card">
                    <h3>Python Mini Projects</h3>
                    <p>
                        Collection of beginner Python programs.
                    </p>
                </div>
            </section>

            <section id="contact" class="contact">
                <h2>Contact Me</h2>
                <p>Email: parimiyaksitha@gmail.com</p>
                <p>Phone: 7671863949</p>
                <p>Location: Anantapur</p>
            </section>

            <footer>
                <p>© 2026 My Personal Portfolio</p>
                <p>Designed with Python ❤️</p>
            </footer>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode("utf-8"))


server = HTTPServer(("localhost", 8000), Portfolio)

print("Portfolio Website Started!")
print("Open http://localhost:8000 in your browser")

server.serve_forever()
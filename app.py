from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question", "").strip()
    difficulty = request.form.get("difficulty", "Easy")
    action = request.form.get("action", "Explain")

    topic = question.lower()
    print("QUESTION:", question)
    print("TOPIC:", topic)
    print("ACTION:", action)
    print("DIFFICULTY:", difficulty)
    answer = ""
# Difficulty-based introduction
    if difficulty == "Easy":
        level_text = """
        <p><b>📗 Easy Level</b></p>
        <p>Explain this topic using very simple words with a basic example.</p>
        """

    elif difficulty == "Medium":
        level_text = """
        <p><b>📘 Medium Level</b></p>
        <p>Explain this topic with moderate technical details and examples.</p>
        """

    else:
        level_text = """
        <p><b>📕 Hard Level</b></p>
        <p>Explain this topic with advanced concepts, technical details and deeper examples.</p>
        """
    # ---------- PYTHON ----------
    if "python" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🐍 Python - Easy Level</h3>

                <p>
                Python is a programming language that is easy to learn
                and understand.
                </p>

                <p><b>Simple Example:</b></p>

                <pre>
                print("Hello World")
                </pre>

                <p>
                This program displays <b>Hello World</b> on the screen.
                </p>

                <p><b>Python is used for:</b></p>
                <ul>
                    <li>Web Development</li>
                    <li>Artificial Intelligence</li>
                    <li>Automation</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🐍 Python - Medium Level</h3>

                <p>
                Python is a high-level, interpreted programming language
                with simple and readable syntax.
                </p>

                <p><b>Important Python concepts:</b></p>
                <ul>
                    <li>Variables and Data Types</li>
                    <li>Conditions</li>
                    <li>Loops</li>
                    <li>Functions</li>
                    <li>Lists and Dictionaries</li>
                    <li>Object-Oriented Programming</li>
                </ul>

                <p>
                Python is widely used in Web Development, AI,
                Machine Learning and Data Science.
                </p>
                """

            else:
                answer = """
                <h3>🐍 Python - Hard Level</h3>

                <p>
                Python is a dynamically typed, interpreted programming
                language with a powerful object-oriented programming model.
                </p>

                <p><b>Advanced Python concepts:</b></p>
                <ul>
                    <li>Decorators</li>
                    <li>Generators</li>
                    <li>Iterators</li>
                    <li>Lambda Functions</li>
                    <li>Exception Handling</li>
                    <li>Object-Oriented Programming</li>
                    <li>Memory Management</li>
                </ul>

                <p>
                Python provides automatic memory management and supports
                advanced programming techniques for building complex applications.
                </p>
                """


        elif action == "Notes":
            answer = """
            <h3>📝 Python - Quick Notes</h3>

            <ul>
                <li>Python is a high-level programming language.</li>
                <li>It has simple and readable syntax.</li>
                <li>It supports Object-Oriented Programming.</li>
                <li>It is widely used in AI and Machine Learning.</li>
                <li>Python uses indentation to define code blocks.</li>
            </ul>

            <p><b>Remember:</b> Python is popular because it is
            simple, powerful and versatile.</p>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Python Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What type of language is Python?</b></p>

                <label>
                    <input type="radio" name="q1" value="A">
                    A) Low-level
                </label>

                <label>
                    <input type="radio" name="q1" value="B">
                    B) High-level
                </label>

                <label>
                    <input type="radio" name="q1" value="C">
                    C) Assembly
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Which feature makes Python beginner-friendly?</b></p>

                <label>
                    <input type="radio" name="q2" value="A">
                    A) Complex syntax
                </label>

                <label>
                    <input type="radio" name="q2" value="B">
                    B) Readable syntax
                </label>
            </div>

            <button type="button" id="checkQuiz">✅ Check Answers</button>

            <div id="quizResult"></div>
            """
    # ---------- JAVA ----------
    # ---------- JAVA ----------
    elif "java" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>☕ Java - Easy Level</h3>
                <p>
                Java is a programming language used to create
                applications and software.
                </p>

                <p><b>Simple Example:</b></p>
                <pre>
    System.out.println("Hello World");
                </pre>

                <p>This statement prints Hello World on the screen.</p>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>☕ Java - Medium Level</h3>

                <p>
                Java is an object-oriented and platform-independent
                programming language.
                </p>

                <p><b>Important Java concepts:</b></p>
                <ul>
                    <li>Classes and Objects</li>
                    <li>Inheritance</li>
                    <li>Polymorphism</li>
                    <li>Encapsulation</li>
                    <li>Abstraction</li>
                </ul>

                <p>
                Java applications run using the Java Virtual Machine (JVM).
                </p>
                """

            else:
                answer = """
                <h3>☕ Java - Hard Level</h3>

                <p>
                Java is a strongly typed, object-oriented programming
                language designed to provide portability through the JVM.
                </p>

                <p><b>Advanced Java concepts:</b></p>
                <ul>
                    <li>JVM Architecture</li>
                    <li>Garbage Collection</li>
                    <li>Multithreading</li>
                    <li>Exception Handling</li>
                    <li>Generics</li>
                    <li>Collections Framework</li>
                    <li>Java Memory Management</li>
                </ul>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 Java - Quick Notes</h3>

            <ul>
                <li>Java is an object-oriented programming language.</li>
                <li>Java uses the JVM to execute programs.</li>
                <li>Java supports classes and objects.</li>
                <li>Java supports inheritance and polymorphism.</li>
                <li>Java is platform independent.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Java Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What does JVM stand for?</b></p>

                <label>
                    <input type="radio" name="java_q1" value="A">
                    A) Java Virtual Machine
                </label>

                <label>
                    <input type="radio" name="java_q1" value="B">
                    B) Java Variable Method
                </label>

                <label>
                    <input type="radio" name="java_q1" value="C">
                    C) Java Visual Model
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Is Java an object-oriented programming language?</b></p>

                <label>
                    <input type="radio" name="java_q2" value="A">
                    A) No
                </label>

                <label>
                    <input type="radio" name="java_q2" value="B">
                    B) Yes
                </label>
            </div>

            <button type="button" id="checkJavaQuiz">✅ Check Answers</button>

            <div id="javaQuizResult"></div>
            """
    # ---------- HTML ----------
    elif "html" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🌐 HTML - Easy Level</h3>

                <p>
                HTML stands for HyperText Markup Language.
                It is used to create the basic structure of a web page.
                </p>

                <p><b>Simple Example:</b></p>

                <pre>
    &lt;h1&gt;Hello World&lt;/h1&gt;
                </pre>

                <p>
                The <b>&lt;h1&gt;</b> tag displays a large heading
                on a webpage.
                </p>

                <p><b>HTML can create:</b></p>
                <ul>
                    <li>Headings</li>
                    <li>Paragraphs</li>
                    <li>Images</li>
                    <li>Links</li>
                    <li>Forms</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🌐 HTML - Medium Level</h3>

                <p>
                HTML is a markup language used to structure content
                on web pages using elements and tags.
                </p>

                <p><b>Important HTML concepts:</b></p>
                <ul>
                    <li>HTML Elements</li>
                    <li>Attributes</li>
                    <li>Forms</li>
                    <li>Tables</li>
                    <li>Semantic Elements</li>
                    <li>Links and Images</li>
                </ul>

                <p>
                HTML provides the structure of a webpage, while CSS
                is mainly used for styling that structure.
                </p>
                """

            else:
                answer = """
                <h3>🌐 HTML - Hard Level</h3>

                <p>
                HTML5 provides semantic and structural elements that
                help browsers and assistive technologies understand
                webpage content.
                </p>

                <p><b>Advanced HTML concepts:</b></p>
                <ul>
                    <li>Semantic HTML</li>
                    <li>Accessibility</li>
                    <li>Forms and Validation</li>
                    <li>Multimedia Elements</li>
                    <li>Data Attributes</li>
                    <li>Web APIs</li>
                    <li>Responsive Structure</li>
                </ul>

                <p>
                Proper semantic HTML improves accessibility, maintainability
                and search-engine understanding of web pages.
                </p>
                """

        elif action == "Notes":
                answer = """
                <h3>📝 HTML - Quick Notes</h3>

                <ul>
                    <li>HTML creates webpage structure.</li>
                    <li>HTML uses tags and elements.</li>
                    <li>&lt;h1&gt; is used for headings.</li>
                    <li>&lt;p&gt; is used for paragraphs.</li>
                    <li>&lt;a&gt; is used for links.</li>
                </ul>
                """

        elif action == "Quiz":
            answer = """
            <h3>🧠 HTML Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What does HTML stand for?</b></p>

                <label>
                    <input type="radio" name="html_q1" value="A">
                    A) HyperText Markup Language
                </label>

                <label>
                    <input type="radio" name="html_q1" value="B">
                    B) HighText Machine Language
                </label>

                <label>
                    <input type="radio" name="html_q1" value="C">
                    C) Hyper Tool Multi Language
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Which tag is used to create a paragraph?</b></p>

                <label>
                    <input type="radio" name="html_q2" value="A">
                    A) &lt;h1&gt;
                </label>

                <label>
                    <input type="radio" name="html_q2" value="B">
                    B) &lt;p&gt;
                </label>

                <label>
                    <input type="radio" name="html_q2" value="C">
                    C) &lt;div&gt;
                </label>
            </div>

            <button type="button" id="checkHtmlQuiz">✅ Check Answers</button>

            <div id="htmlQuizResult"></div>
            """
    # ---------- CSS ----------
    # ---------- CSS ----------
    elif "css" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🎨 CSS - Easy Level</h3>

                <p>
                CSS stands for Cascading Style Sheets.
                It is used to make web pages look attractive.
                </p>

                <p><b>Simple Example:</b></p>

                <pre>
    h1 {
        color: purple;
    }
                </pre>

                <p>
                This code changes the heading color to purple.
                </p>

                <p><b>CSS controls:</b></p>
                <ul>
                    <li>Colors</li>
                    <li>Fonts</li>
                    <li>Spacing</li>
                    <li>Size</li>
                    <li>Layout</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🎨 CSS - Medium Level</h3>

                <p>
                CSS is used to control the appearance and layout
                of HTML elements on a webpage.
                </p>

                <p><b>Important CSS concepts:</b></p>
                <ul>
                    <li>Selectors</li>
                    <li>Properties and Values</li>
                    <li>Box Model</li>
                    <li>Flexbox</li>
                    <li>Grid</li>
                    <li>Responsive Design</li>
                </ul>

                <p>
                CSS can create attractive layouts and responsive
                websites that work on different screen sizes.
                </p>
                """

            else:
                answer = """
                <h3>🎨 CSS - Hard Level</h3>

                <p>
                CSS provides advanced mechanisms for controlling
                layout, rendering, responsiveness and visual behavior
                of web interfaces.
                </p>

                <p><b>Advanced CSS concepts:</b></p>
                <ul>
                    <li>CSS Grid Architecture</li>
                    <li>Advanced Flexbox</li>
                    <li>CSS Variables</li>
                    <li>Pseudo-classes and Pseudo-elements</li>
                    <li>Transitions and Animations</li>
                    <li>Media Queries</li>
                    <li>Responsive Design</li>
                </ul>

                <p>
                Modern CSS allows developers to build complex,
                responsive and interactive user interfaces without
                relying heavily on JavaScript.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 CSS - Quick Notes</h3>

            <ul>
                <li>CSS is used for webpage styling.</li>
                <li>It controls colors and fonts.</li>
                <li>It controls layout and spacing.</li>
                <li>CSS can create animations.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 CSS Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What does CSS stand for?</b></p>

                <label>
                    <input type="radio" name="css_q1" value="A">
                    A) Cascading Style Sheets
                </label>

                <label>
                    <input type="radio" name="css_q1" value="B">
                    B) Computer Style System
                </label>

                <label>
                    <input type="radio" name="css_q1" value="C">
                    C) Creative Styling Syntax
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. What is CSS mainly used for?</b></p>

                <label>
                    <input type="radio" name="css_q2" value="A">
                    A) Storing data
                </label>

                <label>
                    <input type="radio" name="css_q2" value="B">
                    B) Styling web pages
                </label>

                <label>
                    <input type="radio" name="css_q2" value="C">
                    C) Creating databases
                </label>
            </div>

            <button type="button" id="checkCssQuiz">✅ Check Answers</button>

            <div id="cssQuizResult"></div>
            """
    # ---------- AI ----------
    elif topic == "ai" or "artificial intelligence" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🤖 Artificial Intelligence - Easy Level</h3>

                <p>
                Artificial Intelligence, or AI, is a technology that
                allows computers to perform tasks that normally require
                human intelligence.
                </p>

                <p><b>Examples:</b></p>
                <ul>
                    <li>Voice Assistants</li>
                    <li>Chatbots</li>
                    <li>Recommendation Systems</li>
                    <li>Image Recognition</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🤖 Artificial Intelligence - Medium Level</h3>

                <p>
                AI enables machines to learn, reason, recognize patterns
                and make decisions using algorithms and data.
                </p>

                <p><b>Important areas:</b></p>
                <ul>
                    <li>Machine Learning</li>
                    <li>Natural Language Processing</li>
                    <li>Computer Vision</li>
                    <li>Robotics</li>
                </ul>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>🤖 Artificial Intelligence - Hard Level</h3>

                <p>
                AI involves computational techniques that enable systems
                to learn from data, reason about information and perform
                intelligent tasks.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Deep Learning</li>
                    <li>Neural Networks</li>
                    <li>Reinforcement Learning</li>
                    <li>Generative AI</li>
                    <li>Natural Language Processing</li>
                    <li>Computer Vision</li>
                </ul>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 AI - Quick Notes</h3>

            <ul>
                <li>AI stands for Artificial Intelligence.</li>
                <li>AI enables machines to perform intelligent tasks.</li>
                <li>Machine Learning is a major area of AI.</li>
                <li>AI is used in many real-world applications.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 AI Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What does AI stand for?</b></p>

                <label>
                    <input type="radio" name="ai_q1" value="A">
                    A) Artificial Intelligence
                </label>

                <label>
                    <input type="radio" name="ai_q1" value="B">
                    B) Automated Internet
                </label>

                <label>
                    <input type="radio" name="ai_q1" value="C">
                    C) Advanced Information
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Which is a major area of AI?</b></p>

                <label>
                    <input type="radio" name="ai_q2" value="A">
                    A) Machine Learning
                </label>

                <label>
                    <input type="radio" name="ai_q2" value="B">
                    B) Word Processing
                </label>

                <label>
                    <input type="radio" name="ai_q2" value="C">
                    C) File Management
                </label>
            </div>

            <button type="button" id="checkAiQuiz">✅ Check Answers</button>

            <div id="aiQuizResult"></div>
            """
            # ---------- MACHINE LEARNING ----------
    elif "machine learning" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🧠 Machine Learning - Easy Level</h3>

                <p>
                Machine Learning is a part of Artificial Intelligence
                that allows computers to learn from data and make
                predictions or decisions.
                </p>

                <p><b>Simple Example:</b></p>

                <p>
                An email system can learn from previous emails and
                identify whether a new email is spam or not.
                </p>

                <p><b>Common uses:</b></p>
                <ul>
                    <li>Spam Detection</li>
                    <li>Recommendations</li>
                    <li>Image Recognition</li>
                    <li>Prediction</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🧠 Machine Learning - Medium Level</h3>

                <p>
                Machine Learning enables computers to learn patterns
                from existing data without being explicitly programmed
                for every situation.
                </p>

                <p><b>Main types of Machine Learning:</b></p>
                <ul>
                    <li>Supervised Learning</li>
                    <li>Unsupervised Learning</li>
                    <li>Reinforcement Learning</li>
                </ul>

                <p>
                Machine Learning models are trained using data and
                evaluated using suitable performance measures.
                </p>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>🧠 Machine Learning - Hard Level</h3>

                <p>
                Machine Learning uses statistical and computational
                methods to learn patterns from data and generalize
                those patterns to unseen data.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Feature Engineering</li>
                    <li>Model Training</li>
                    <li>Overfitting and Underfitting</li>
                    <li>Regularization</li>
                    <li>Cross-Validation</li>
                    <li>Hyperparameter Tuning</li>
                    <li>Model Evaluation</li>
                </ul>

                <p>
                The goal is to build models that perform well not only
                on training data but also on previously unseen data.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 Machine Learning - Quick Notes</h3>

            <ul>
                <li>ML is a branch of Artificial Intelligence.</li>
                <li>ML systems learn patterns from data.</li>
                <li>Supervised learning uses labelled data.</li>
                <li>Unsupervised learning finds patterns in data.</li>
                <li>Reinforcement learning learns through rewards and penalties.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Machine Learning Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What is Machine Learning?</b></p>

                <label>
                    <input type="radio" name="ml_q1" value="A">
                    A) A method that allows computers to learn from data
                </label>

                <label>
                    <input type="radio" name="ml_q1" value="B">
                    B) A method used only for storing data
                </label>

                <label>
                    <input type="radio" name="ml_q1" value="C">
                    C) A type of computer hardware
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Which is a type of Machine Learning?</b></p>

                <label>
                    <input type="radio" name="ml_q2" value="A">
                    A) Supervised Learning
                </label>

                <label>
                    <input type="radio" name="ml_q2" value="B">
                    B) Web Development
                </label>

                <label>
                    <input type="radio" name="ml_q2" value="C">
                    C) Database Management
                </label>
            </div>

            <div class="quiz-question">
                <p><b>3. What is overfitting?</b></p>

                <label>
                    <input type="radio" name="ml_q3" value="A">
                    A) A model learning the training data too closely
                </label>

                <label>
                    <input type="radio" name="ml_q3" value="B">
                    B) A model deleting the training data
                </label>

                <label>
                    <input type="radio" name="ml_q3" value="C">
                    C) A model storing data permanently
                </label>
            </div>

            <button type="button" id="checkMlQuiz">✅ Check Answers</button>

            <div id="mlQuizResult"></div>
            """
            # ---------- CLOUD COMPUTING ----------
    elif "cloud computing" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>☁️ Cloud Computing - Easy Level</h3>

                <p>
                Cloud Computing means using computing services such as
                storage, servers and applications through the Internet.
                </p>

                <p><b>Simple Example:</b></p>

                <p>
                Google Drive allows us to store files online instead of
                storing everything only on our computer.
                </p>

                <p><b>Cloud services include:</b></p>
                <ul>
                    <li>Storage</li>
                    <li>Servers</li>
                    <li>Databases</li>
                    <li>Applications</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>☁️ Cloud Computing - Medium Level</h3>

                <p>
                Cloud Computing provides computing resources over the
                Internet whenever they are needed.
                </p>

                <p><b>Main service models:</b></p>
                <ul>
                    <li>IaaS - Infrastructure as a Service</li>
                    <li>PaaS - Platform as a Service</li>
                    <li>SaaS - Software as a Service</li>
                </ul>

                <p>
                Cloud platforms allow organizations to scale resources
                according to their requirements.
                </p>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>☁️ Cloud Computing - Hard Level</h3>

                <p>
                Cloud Computing provides on-demand access to shared
                computing resources through distributed infrastructure.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Virtualization</li>
                    <li>Containerization</li>
                    <li>Load Balancing</li>
                    <li>Auto Scaling</li>
                    <li>Distributed Computing</li>
                    <li>Cloud Security</li>
                    <li>Serverless Computing</li>
                </ul>

                <p>
                Cloud systems are designed to provide scalability,
                availability and efficient resource utilization.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 Cloud Computing - Quick Notes</h3>

            <ul>
                <li>Cloud Computing provides computing resources through the Internet.</li>
                <li>IaaS provides infrastructure resources.</li>
                <li>PaaS provides a development platform.</li>
                <li>SaaS provides ready-to-use software.</li>
                <li>Cloud computing supports scalability and flexibility.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Cloud Computing Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What is Cloud Computing?</b></p>

                <label>
                    <input type="radio" name="cloud_q1" value="A">
                    A) Providing computing resources through the Internet
                </label>

                <label>
                    <input type="radio" name="cloud_q1" value="B">
                    B) A type of computer hardware
                </label>

                <label>
                    <input type="radio" name="cloud_q1" value="C">
                    C) A programming language
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. What does SaaS stand for?</b></p>

                <label>
                    <input type="radio" name="cloud_q2" value="A">
                    A) Software as a Service
                </label>

                <label>
                    <input type="radio" name="cloud_q2" value="B">
                    B) System as a Software
                </label>

                <label>
                    <input type="radio" name="cloud_q2" value="C">
                    C) Storage as a System
                </label>
            </div>

            <div class="quiz-question">
                <p><b>3. Which is a cloud service model?</b></p>

                <label>
                    <input type="radio" name="cloud_q3" value="A">
                    A) IaaS
                </label>

                <label>
                    <input type="radio" name="cloud_q3" value="B">
                    B) HTML
                </label>

                <label>
                    <input type="radio" name="cloud_q3" value="C">
                    C) CSS
                </label>
            </div>

            <button type="button" id="checkCloudQuiz">✅ Check Answers</button>

            <div id="cloudQuizResult"></div>
            """
            # ---------- CYBER SECURITY ----------
    elif "cyber security" in topic or "cybersecurity" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🔐 Cyber Security - Easy Level</h3>

                <p>
                Cyber Security means protecting computers, networks,
                applications and data from unauthorized access and
                harmful activities.
                </p>

                <p><b>Simple Example:</b></p>

                <p>
                Using a strong password helps protect your online
                accounts from unauthorized access.
                </p>

                <p><b>Cyber Security protects:</b></p>
                <ul>
                    <li>Personal Data</li>
                    <li>Passwords</li>
                    <li>Computer Systems</li>
                    <li>Networks</li>
                    <li>Online Accounts</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🔐 Cyber Security - Medium Level</h3>

                <p>
                Cyber Security involves protecting digital systems and
                information from threats such as malware, phishing and
                unauthorized access.
                </p>

                <p><b>Important concepts:</b></p>
                <ul>
                    <li>Authentication</li>
                    <li>Authorization</li>
                    <li>Encryption</li>
                    <li>Firewalls</li>
                    <li>Network Security</li>
                    <li>Malware Protection</li>
                </ul>

                <p>
                Security systems use multiple layers of protection
                to reduce the risk of attacks.
                </p>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>🔐 Cyber Security - Hard Level</h3>

                <p>
                Cyber Security uses technical and organizational
                controls to protect the confidentiality, integrity
                and availability of information systems.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Cryptography</li>
                    <li>Intrusion Detection</li>
                    <li>Network Security</li>
                    <li>Access Control</li>
                    <li>Security Monitoring</li>
                    <li>Threat Detection</li>
                    <li>Incident Response</li>
                </ul>

                <p>
                A strong security architecture combines prevention,
                detection and response mechanisms.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 Cyber Security - Quick Notes</h3>

            <ul>
                <li>Cyber Security protects digital systems and data.</li>
                <li>Authentication verifies user identity.</li>
                <li>Authorization controls access to resources.</li>
                <li>Encryption protects information from unauthorized access.</li>
                <li>Firewalls help protect networks.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Cyber Security Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What is Cyber Security?</b></p>

                <label>
                    <input type="radio" name="cyber_q1" value="A">
                    A) Protecting digital systems, networks and data
                </label>

                <label>
                    <input type="radio" name="cyber_q1" value="B">
                    B) Creating websites
                </label>

                <label>
                    <input type="radio" name="cyber_q1" value="C">
                    C) Managing databases
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. What is encryption used for?</b></p>

                <label>
                    <input type="radio" name="cyber_q2" value="A">
                    A) Protecting information
                </label>

                <label>
                    <input type="radio" name="cyber_q2" value="B">
                    B) Increasing computer speed
                </label>

                <label>
                    <input type="radio" name="cyber_q2" value="C">
                    C) Creating web pages
                </label>
            </div>

            <div class="quiz-question">
                <p><b>3. What does authentication do?</b></p>

                <label>
                    <input type="radio" name="cyber_q3" value="A">
                    A) Verifies the identity of a user
                </label>

                <label>
                    <input type="radio" name="cyber_q3" value="B">
                    B) Deletes user accounts
                </label>

                <label>
                    <input type="radio" name="cyber_q3" value="C">
                    C) Increases storage space
                </label>
            </div>

            <button type="button" id="checkCyberQuiz">✅ Check Answers</button>

            <div id="cyberQuizResult"></div>
            """
            # ---------- DBMS ----------
    elif "dbms" in topic or "database" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🗄️ DBMS - Easy Level</h3>

                <p>
                DBMS stands for Database Management System.
                It is software used to store, manage and retrieve data.
                </p>

                <p><b>Simple Example:</b></p>

                <p>
                A college can use a database to store student names,
                register numbers, marks and course details.
                </p>

                <p><b>Examples of DBMS:</b></p>
                <ul>
                    <li>MySQL</li>
                    <li>Oracle</li>
                    <li>PostgreSQL</li>
                    <li>SQLite</li>
                </ul>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🗄️ DBMS - Medium Level</h3>

                <p>
                A DBMS provides a structured way to store, organize,
                update and retrieve data from databases.
                </p>

                <p><b>Important concepts:</b></p>
                <ul>
                    <li>Tables</li>
                    <li>Primary Key</li>
                    <li>Foreign Key</li>
                    <li>SQL</li>
                    <li>Relationships</li>
                    <li>Normalization</li>
                </ul>

                <p>
                DBMS helps reduce data redundancy and provides
                controlled access to stored information.
                </p>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>🗄️ DBMS - Hard Level</h3>

                <p>
                A DBMS manages persistent data while providing
                mechanisms for consistency, concurrency, security
                and reliable data access.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Transaction Management</li>
                    <li>ACID Properties</li>
                    <li>Concurrency Control</li>
                    <li>Indexing</li>
                    <li>Query Optimization</li>
                    <li>Normalization</li>
                    <li>Recovery Management</li>
                </ul>

                <p>
                Transaction management helps maintain database
                consistency even when multiple operations occur
                simultaneously or failures happen.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 DBMS - Quick Notes</h3>

            <ul>
                <li>DBMS stands for Database Management System.</li>
                <li>It is used to store and manage data.</li>
                <li>SQL is commonly used to interact with databases.</li>
                <li>Primary keys uniquely identify records.</li>
                <li>Foreign keys establish relationships between tables.</li>
                <li>Normalization helps reduce data redundancy.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 DBMS Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. What does DBMS stand for?</b></p>

                <label>
                    <input type="radio" name="dbms_q1" value="A">
                    A) Database Management System
                </label>

                <label>
                    <input type="radio" name="dbms_q1" value="B">
                    B) Data Backup Management System
                </label>

                <label>
                    <input type="radio" name="dbms_q1" value="C">
                    C) Digital Business Management System
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. What is a Primary Key?</b></p>

                <label>
                    <input type="radio" name="dbms_q2" value="A">
                    A) A key that uniquely identifies a record
                </label>

                <label>
                    <input type="radio" name="dbms_q2" value="B">
                    B) A key used only for deleting data
                </label>

                <label>
                    <input type="radio" name="dbms_q2" value="C">
                    C) A key used to create a database
                </label>
            </div>

            <div class="quiz-question">
                <p><b>3. What is SQL?</b></p>

                <label>
                    <input type="radio" name="dbms_q3" value="A">
                    A) Structured Query Language
                </label>

                <label>
                    <input type="radio" name="dbms_q3" value="B">
                    B) Simple Question Language
                </label>

                <label>
                    <input type="radio" name="dbms_q3" value="C">
                    C) System Query Logic
                </label>
            </div>

            <button type="button" id="checkDbmsQuiz">✅ Check Answers</button>

            <div id="dbmsQuizResult"></div>
            """
            # ---------- DATA STRUCTURES ----------
    elif "data structure" in topic or "data structures" in topic:

        if action == "Explain":

            if difficulty == "Easy":
                answer = """
                <h3>🌳 Data Structures - Easy Level</h3>

                <p>
                A Data Structure is a way of organizing and storing
                data so that it can be used efficiently.
                </p>

                <p><b>Simple Examples:</b></p>
                <ul>
                    <li>Array</li>
                    <li>Stack</li>
                    <li>Queue</li>
                    <li>Linked List</li>
                </ul>

                <p>
                For example, a queue works like a line of people:
                the person who enters first is usually served first.
                </p>
                """

            elif difficulty == "Medium":
                answer = """
                <h3>🌳 Data Structures - Medium Level</h3>

                <p>
                Data structures organize data in different ways
                depending on how the data needs to be accessed
                and modified.
                </p>

                <p><b>Important types:</b></p>
                <ul>
                    <li>Arrays</li>
                    <li>Linked Lists</li>
                    <li>Stacks</li>
                    <li>Queues</li>
                    <li>Trees</li>
                    <li>Graphs</li>
                    <li>Hash Tables</li>
                </ul>

                <p>
                Choosing a suitable data structure can improve the
                efficiency of a program.
                </p>
                """

            elif difficulty == "Hard":
                answer = """
                <h3>🌳 Data Structures - Hard Level</h3>

                <p>
                Data structures are fundamental abstractions for
                representing data and supporting efficient operations.
                </p>

                <p><b>Advanced concepts:</b></p>
                <ul>
                    <li>Binary Search Trees</li>
                    <li>AVL Trees</li>
                    <li>Heaps</li>
                    <li>Graphs</li>
                    <li>Hashing</li>
                    <li>Priority Queues</li>
                    <li>Time and Space Complexity</li>
                </ul>

                <p>
                The efficiency of data structure operations is often
                analyzed using Big-O notation.
                </p>
                """

        elif action == "Notes":
            answer = """
            <h3>📝 Data Structures - Quick Notes</h3>

            <ul>
                <li>Data structures organize and store data.</li>
                <li>Arrays store elements in an indexed structure.</li>
                <li>Stacks follow LIFO.</li>
                <li>Queues generally follow FIFO.</li>
                <li>Trees represent hierarchical data.</li>
                <li>Graphs represent relationships between entities.</li>
            </ul>
            """

        elif action == "Quiz":
            answer = """
            <h3>🧠 Data Structures Mini Quiz</h3>

            <div class="quiz-question">
                <p><b>1. Which data structure follows LIFO?</b></p>

                <label>
                    <input type="radio" name="ds_q1" value="A">
                    A) Queue
                </label>

                <label>
                    <input type="radio" name="ds_q1" value="B">
                    B) Stack
                </label>

                <label>
                    <input type="radio" name="ds_q1" value="C">
                    C) Array
                </label>
            </div>

            <div class="quiz-question">
                <p><b>2. Which data structure follows FIFO?</b></p>

                <label>
                    <input type="radio" name="ds_q2" value="A">
                    A) Stack
                </label>

                <label>
                    <input type="radio" name="ds_q2" value="B">
                    B) Tree
                </label>

                <label>
                    <input type="radio" name="ds_q2" value="C">
                    C) Queue
                </label>
            </div>

            <div class="quiz-question">
                <p><b>3. Which data structure stores elements in key-value pairs?</b></p>

                <label>
                    <input type="radio" name="ds_q3" value="A">
                    A) Dictionary
                </label>

                <label>
                    <input type="radio" name="ds_q3" value="B">
                    B) Stack
                </label>

                <label>
                    <input type="radio" name="ds_q3" value="C">
                    C) Queue
                </label>
            </div>

            <button type="button" id="checkDsQuiz">✅ Check Answers</button>

            <div id="dsQuizResult"></div>
            """
    # ---------- GENERAL TOPIC ----------
    else:

        if action == "Explain":
            answer = f"""
            <h3>📚 {question}</h3>

            <p>
            Let's understand <b>{question}</b> step by step.
            Start with its basic definition, important concepts,
            examples and real-world applications.
            </p>

            <p><b>Difficulty:</b> {difficulty}</p>
            """

        elif action == "Notes":
            answer = f"""
            <h3>📝 {question} - Quick Notes</h3>

            <ul>
                <li>Learn the basic definition.</li>
                <li>Understand the important concepts.</li>
                <li>Study simple examples.</li>
                <li>Practice with small problems.</li>
            </ul>

            <p><b>Difficulty:</b> {difficulty}</p>
            """

        elif action == "Quiz":
            answer = f"""
            <h3>🧠 {question} - Mini Quiz</h3>

            <p><b>1. What is {question}?</b></p>
            <p>Try explaining it in your own words.</p>

            <p><b>2. Why is {question} important?</b></p>
            <p>Think about its applications and uses.</p>

            <p><b>Difficulty:</b> {difficulty}</p>
            """
        if not answer:
            answer = f"""
            <h3>📚 {question}</h3>
            <p>
            Please select Explain, Notes, or Quiz and try again.
            </p>
            <p><b>Difficulty:</b> {difficulty}</p>
            """

    return render_template(
            "index.html",
            response=answer,
            question=question
    )
   

if __name__ == "__main__":
    app.run(debug=True)
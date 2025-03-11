
class QAKnowledgeBase:
    """Knowledge base containing ISTQB concepts and testing information"""
    
    def __init__(self):
        # ISTQB categories and topics
        self.categories = {
            "Testing Fundamentals": [
                "Definition of Testing",
                "Testing Objectives",
                "Seven Testing Principles",
                "Test Process",
                "Psychology of Testing"
            ],
            "Testing Throughout SDLC": [
                "Software Development Models",
                "Test Levels",
                "Test Types",
                "Maintenance Testing"
            ],
            "Static Testing": [
                "Review Process",
                "Static Analysis",
                "Review Types"
            ],
            "Test Design Techniques": [
                "Black-box Techniques",
                "White-box Techniques",
                "Experience-based Techniques"
            ],
            "Test Management": [
                "Test Organization",
                "Test Planning and Estimation",
                "Test Monitoring and Control",
                "Risk Management",
                "Defect Management"
            ],
            "Tool Support for Testing": [
                "Test Tool Considerations",
                "Effective Use of Tools"
            ],
            "Test Automation": [
                "Automation Approaches",
                "Test Automation Frameworks",
                "Automation ROI",
                "Continuous Integration/Deployment"
            ]
        }
        
        # Content for each topic
        self.content = {
            "Definition of Testing": "Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do. The benefits of testing include preventing defects, verifying requirements are met, and reducing development costs by identifying bugs early.",
            
            "Testing Objectives": "The main objectives of software testing are: finding defects, gaining confidence about the level of quality, providing information for decision-making, and preventing defects. Testing helps to identify and fix bugs before the product is delivered to customers.",
            
            "Seven Testing Principles": """The seven fundamental principles of testing are:
1. Testing shows the presence of defects, not their absence
2. Exhaustive testing is impossible
3. Early testing saves time and money
4. Defects cluster together
5. Beware of the pesticide paradox (tests lose effectiveness over time)
6. Testing is context dependent
7. Absence of errors is a fallacy""",
            
            "Test Process": """The fundamental test process consists of:
- Test planning and control
- Test analysis and design
- Test implementation and execution
- Evaluating exit criteria and reporting
- Test closure activities""",
            
            "Psychology of Testing": "Testing requires a different mindset than development. Testers need to maintain a critical eye and identify potential issues without being defensive. Good communication between testers and developers is essential for productive collaboration.",
            
            "Software Development Models": """Major development models include:
1. Waterfall Model: Linear sequential flow with distinct phases
2. V-Model: Testing activities parallel to each development phase
3. Incremental Development: System developed and delivered in increments
4. Iterative Development: System developed through repeated cycles
5. Agile: Emphasizes flexibility, customer collaboration, and rapid delivery
6. DevOps: Integrates development and operations with continuous delivery""",
            
            "Test Levels": """The four main levels of testing are:
1. Unit Testing: Testing individual components in isolation
2. Integration Testing: Testing interfaces between components
3. System Testing: Testing the complete integrated system
4. Acceptance Testing: Validating the system meets business requirements and is ready for delivery""",
            
            "Test Types": """Main types of testing include:
1. Functional Testing: Tests what the system does
2. Non-functional Testing: Tests how well the system performs (performance, usability, reliability, etc.)
3. Structural Testing: Tests the internal structure of the software
4. Change-related Testing: Tests after modifications (regression and confirmation testing)""",
            
            "Maintenance Testing": "Maintenance testing is performed on existing software after changes, such as enhancements, corrections, or adaptations to environment changes. It includes regression testing to ensure existing functionality still works.",
            
            "Review Process": """The formal review process includes these activities:
1. Planning: Define scope and criteria
2. Kick-off: Distribute materials and explain objectives
3. Individual preparation: Reviewers examine work products and note potential defects
4. Review meeting: Discuss and document findings
5. Rework: Address identified issues
6. Follow-up: Verify issues were resolved correctly""",
            
            "Static Analysis": "Static analysis involves examining code without executing it, often using automated tools to find defects. It can identify issues such as coding standard violations, memory leaks, security vulnerabilities, and more.",
            
            "Review Types": """Different review types include:
1. Informal Review: No formal process, may be as simple as asking a colleague for feedback
2. Walkthrough: Author leads participants through a work product to gather feedback
3. Technical Review: Documented, structured approach with focus on technical quality
4. Inspection: Formal, rigorous review process with specific roles and metrics""",
            
            "Black-box Techniques": """Black-box testing techniques focus on inputs and outputs without knowledge of internal code structure:
1. Equivalence Partitioning: Dividing input data into valid and invalid partitions
2. Boundary Value Analysis: Testing values at the boundaries of partitions
3. Decision Table Testing: For complex business logic with combinations of conditions
4. State Transition Testing: For systems that exhibit different states based on inputs
5. Use Case Testing: Based on interactions between actors and the system""",
            
            "White-box Techniques": """White-box techniques examine the internal structure of the code:
1. Statement Coverage: Each executable statement is executed at least once
2. Decision Coverage: Each decision (true/false) is executed at least once
3. Condition Coverage: Each condition in a decision is evaluated to true and false
4. Path Coverage: All possible paths through a program are executed""",
            
            "Experience-based Techniques": """Experience-based techniques rely on the tester's knowledge and experience:
1. Error Guessing: Anticipating where errors might occur based on experience
2. Exploratory Testing: Simultaneous learning, test design, and execution
3. Checklist-based Testing: Using checklists developed from experience on similar projects""",
            
            "Test Organization": "Test organization involves deciding on the test team structure, roles and responsibilities, and the degree of independence. Independence can range from having developers test their own code to separate test teams or organizations.",
            
            "Test Planning and Estimation": "Test planning includes determining the scope and objectives of testing, creating test schedules, deciding on test approaches, establishing entry/exit criteria, and estimating resources needed.",
            
            "Test Monitoring and Control": "Test monitoring involves tracking progress against the plan, while test control involves taking actions to meet the objectives. This includes metrics tracking, risk identification, and implementing corrective actions.",
            
            "Risk Management": "Risk management in testing involves identifying what can go wrong (risk), how likely it is (likelihood), and what the impact would be. Testing is prioritized to address the highest-risk areas first.",
            
            "Defect Management": """The defect management process typically includes:
1. Detection: Finding the defect
2. Classification: Categorizing by severity, priority, etc.
3. Reporting: Documenting the defect
4. Analysis: Determining cause and impact
5. Resolution: Fixing the defect
6. Verification: Confirming the fix works
7. Closure: Finalizing the defect report""",
            
            "Test Tool Considerations": "When selecting test tools, consider organizational maturity, compatibility with existing processes, evaluation period needs, pilot projects, vendor support, training requirements, and ROI calculation.",
            
            "Effective Use of Tools": "For effective tool adoption, introduce tools gradually, adapt processes to work with the tools, provide training and mentoring, establish usage guidelines, monitor tool usage and benefits, and provide support for the tool user.",
            
            "Automation Approaches": """Common test automation approaches include:
1. Linear scripting (record and playback)
2. Structured scripting (using procedures/functions)
3. Data-driven testing (separating test data from scripts)
4. Keyword-driven testing (using action keywords)
5. Behavior-driven development (BDD)
6. Model-based testing""",
            
            "Test Automation Frameworks": """Test automation frameworks provide structures that make automation more efficient:
1. Data-driven: Separates test data from test scripts
2. Keyword-driven: Uses action words to represent user interactions
3. Hybrid: Combines multiple framework approaches
4. Page Object Model: Abstracts UI elements into object-oriented classes
5. BDD Frameworks: Uses natural language specifications (e.g., Cucumber, SpecFlow)""",
            
            "Automation ROI": "Return on Investment (ROI) for automation considers initial costs (tool licenses, training, script development) versus long-term savings (reduced manual testing time, earlier defect detection, increased test coverage).",
            
            "Continuous Integration/Deployment": "CI/CD pipelines automate the building, testing, and deployment of applications. Automated tests are essential in these pipelines, providing fast feedback about application quality at each stage."
        }
        
        # Quiz questions for each topic
        self.quizzes = {
            "Testing Fundamentals": [
                {
                    "question": "Which of the following is NOT one of the seven testing principles?",
                    "options": [
                        "Testing shows the presence of defects, not their absence",
                        "Exhaustive testing is impossible",
                        "Testing always improves software quality",
                        "Defects cluster together"
                    ],
                    "correct": 2
                },
                {
                    "question": "What is the main purpose of software testing?",
                    "options": [
                        "To make software completely bug-free",
                        "To demonstrate that software works perfectly",
                        "To find defects and reduce the risk of software failures",
                        "To ensure all requirements are implemented"
                    ],
                    "correct": 2
                }
            ],
            "Test Levels": [
                {
                    "question": "Which test level focuses on testing the interfaces between components?",
                    "options": [
                        "Unit Testing",
                        "Integration Testing",
                        "System Testing",
                        "Acceptance Testing"
                    ],
                    "correct": 1
                },
                {
                    "question": "Who typically performs acceptance testing?",
                    "options": [
                        "Developers",
                        "Testers",
                        "Users/Customers",
                        "Project Managers"
                    ],
                    "correct": 2
                }
            ],
            "Test Design Techniques": [
                {
                    "question": "Which of the following is a black-box testing technique?",
                    "options": [
                        "Statement Coverage",
                        "Path Coverage",
                        "Boundary Value Analysis",
                        "Condition Coverage"
                    ],
                    "correct": 2
                },
                {
                    "question": "In which technique do you test each true/false outcome of every decision?",
                    "options": [
                        "Statement Coverage",
                        "Decision Coverage",
                        "Condition Coverage",
                        "Equivalence Partitioning"
                    ],
                    "correct": 1
                }
            ],
            "Test Automation": [
                {
                    "question": "Which automation approach separates test data from test scripts?",
                    "options": [
                        "Linear scripting",
                        "Structured scripting",
                        "Data-driven testing",
                        "Keyword-driven testing"
                    ],
                    "corsrect": 2
                },
                {
                    "question": "What framework uses action words to represent user interactions?",
                    "options": [
                        "Data-driven",
                        "Keyword-driven",
                        "Linear scripting",
                        "Behavior-driven"
                    ],
                    "correct": 1
                }
            ]
        }

    def get_categories(self):
        return list(self.categories.keys())
    
    def get_topics(self, category):
        return self.categories.get(category, [])
    
    def get_content(self, topic):
        return self.content.get(topic, "Content for this topic is not available.")
    
    def get_quiz(self, category):
        return self.quizzes.get(category, [])

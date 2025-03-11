from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QDialog
)
from PySide6.QtCore import Qt


class QuizDialog(QDialog):
    """Dialog for taking quizzes on QA and testing topics"""

    def __init__(self, quiz_data, category, parent=None):
        super().__init__(parent)
        self.quiz_data = quiz_data
        self.current_question = 0
        self.score = 0
        self.user_answers = []

        self.setWindowTitle(f"Quiz: {category}")
        self.setMinimumSize(500, 400)

        self.setup_ui()
        self.show_question()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Question label
        self.question_label = QLabel()
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet(
            "font-size: 16px; font-weight: bold; margin-bottom: 10px;"
        )
        layout.addWidget(self.question_label)

        # Options
        self.option_buttons = []
        options_layout = QVBoxLayout()

        for i in range(4):
            button = QPushButton()
            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    padding: 10px;
                    margin: 5px;
                    border-radius: 5px;
                    background-color: #f0f0f0;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """
            )
            button.clicked.connect(lambda checked, idx=i: self.select_answer(idx))
            options_layout.addWidget(button)
            self.option_buttons.append(button)

        layout.addLayout(options_layout)

        # Navigation buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.next_button = QPushButton("Next")
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2e86de;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1b4f72;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """
        )
        button_layout.addWidget(self.next_button)

        layout.addLayout(button_layout)
        layout.addStretch()

        self.setLayout(layout)

    def show_question(self):
        if not self.quiz_data or self.current_question >= len(self.quiz_data):
            self.show_results()
            return

        question_data = self.quiz_data[self.current_question]
        self.question_label.setText(
            f"Question {self.current_question + 1}: {question_data['question']}"
        )

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].setText(f"{chr(65 + i)}. {option}")
            self.option_buttons[i].setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    padding: 10px;
                    margin: 5px;
                    border-radius: 5px;
                    background-color: #f0f0f0;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """
            )

        self.next_button.setEnabled(False)

    def select_answer(self, selected_index):
        current_q = self.quiz_data[self.current_question]
        correct_index = current_q["correct"]

        # Save user's answer
        self.user_answers.append(selected_index)

        # Update score if correct
        if selected_index == correct_index:
            self.score += 1

        # Highlight correct and incorrect answers
        for i, button in enumerate(self.option_buttons):
            if i == correct_index:
                button.setStyleSheet(
                    """
                    QPushButton {
                        text-align: left;
                        padding: 10px;
                        margin: 5px;
                        border-radius: 5px;
                        background-color: #27ae60;
                        color: white;
                    }
                """
                )
            elif i == selected_index and i != correct_index:
                button.setStyleSheet(
                    """
                    QPushButton {
                        text-align: left;
                        padding: 10px;
                        margin: 5px;
                        border-radius: 5px;
                        background-color: #e74c3c;
                        color: white;
                    }
                """
                )
            else:
                button.setStyleSheet(
                    """
                    QPushButton {
                        text-align: left;
                        padding: 10px;
                        margin: 5px;
                        border-radius: 5px;
                        background-color: #f0f0f0;
                    }
                """
                )

            # Disable all option buttons
            button.setEnabled(False)

        self.next_button.setEnabled(True)

    def next_question(self):
        self.current_question += 1

        for button in self.option_buttons:
            button.setEnabled(True)

        self.show_question()

    def show_results(self):
        result_text = f"You scored {self.score} out of {len(self.quiz_data)}."
        percentage = (self.score / len(self.quiz_data)) * 100

        if percentage >= 80:
            result_text += "\nExcellent! You have a strong understanding of this topic."
        elif percentage >= 60:
            result_text += "\nGood job! You have a decent grasp of the concepts."
        else:
            result_text += "\nYou might want to review this topic again."

        for i, button in enumerate(self.option_buttons):
            button.setVisible(False)

        self.question_label.setText(result_text)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 18px; margin: 20px;")

        self.next_button.setText("Close")
        self.next_button.clicked.disconnect()
        self.next_button.clicked.connect(self.accept)

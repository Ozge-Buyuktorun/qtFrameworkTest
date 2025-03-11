# ─────────────────────────────────────────────
# 📦 Standard Library Imports
import sys  # System-specific parameters and functions
import random  # Random number generation (used in quizzes, etc.)
import json  # Handling JSON data structures (quiz data, content, etc.)

# ─────────────────────────────────────────────
# 🖼️ PySide6 GUI Framework Imports
from PySide6.QtWidgets import (
    QApplication,  # Main application object
    QWidget,  # Base class for all UI elements
    QPushButton,  # Button widget
    QLabel,  # Text display widget
    QVBoxLayout,  # Vertical layout manager
    QHBoxLayout,  # Horizontal layout manager
    QStackedWidget,  # Stacked view container for switching views
    QComboBox,  # Dropdown selector widget
    QTextEdit,  # Multi-line text input/display area
    QScrollArea,  # Scrollable content area
    QFrame,  # Basic frame widget
    QDialog,  # Dialog window
    QGridLayout,  # Grid layout manager
    QMessageBox,  # Message popup dialogs
)

from PySide6.QtCore import Qt, Signal, Slot, QSize, QObject

# Qt: Contains core enums like AlignCenter, etc.
# Signal/Slot: Event communication mechanism
# QSize: Defines dimensions
# QObject: Base class for all Qt objects

from PySide6.QtGui import QFont, QIcon

# QFont: For font styling
# QIcon: For setting window/app icons

# ─────────────────────────────────────────────
# 📂 Internal Project Imports
from gui.qa import QAKnowledgeBase  # Knowledge base interface for QA topics
from gui.quiz import QuizDialog  # Quiz dialog interface


class MainWindow(QWidget):
    """Main application window for QA & Testing Education App"""

    def __init__(self):
        super().__init__()
        self.knowledge_base = QAKnowledgeBase()
        self.setup_ui()

    def setup_ui(self):
        # Set the window title and minimum size
        self.setWindowTitle("QA & Testing Education App")
        self.setMinimumSize(800, 600)

        # Apply general stylesheet for consistent look and feel
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #333333;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #cccccc;
                border-radius: 5px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                background-color: white;
                padding: 10px;
            }
        """
        )

        # Main vertical layout for the entire window
        main_layout = QVBoxLayout()

        # Header title
        header = QLabel("QA & Testing Education App")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #2c3e50; margin: 10px;"
        )
        main_layout.addWidget(header)

        # Short description below the header
        description = QLabel(
            "Learn about software testing concepts, methodologies, and best practices based on ISTQB syllabus"
        )
        description.setAlignment(Qt.AlignCenter)
        description.setStyleSheet(
            "font-size: 14px; color: #7f8c8d; margin-bottom: 20px;"
        )
        main_layout.addWidget(description)

        # Horizontal layout for sidebar + main content area
        content_layout = QHBoxLayout()

        # Sidebar layout (left panel)
        sidebar = QVBoxLayout()
        sidebar.setContentsMargins(0, 0, 10, 0)

        # Category label
        category_label = QLabel("Categories:")
        category_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        sidebar.addWidget(category_label)

        # Category dropdown selector
        self.category_combo = QComboBox()
        self.category_combo.addItems(self.knowledge_base.get_categories())
        self.category_combo.currentIndexChanged.connect(self.category_changed)
        sidebar.addWidget(self.category_combo)

        # Topic label
        topic_label = QLabel("Topics:")
        topic_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        sidebar.addWidget(topic_label)

        # Topics container frame with custom style
        topics_frame = QFrame()
        topics_frame.setFrameShape(QFrame.StyledPanel)
        topics_frame.setStyleSheet("background-color: white; border-radius: 5px;")
        topics_layout = QVBoxLayout(topics_frame)

        # Create topic buttons dynamically based on selected category
        self.topics_buttons = []
        initial_category = self.category_combo.currentText()
        for topic in self.knowledge_base.get_topics(initial_category):
            button = QPushButton(topic)
            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    border: none;
                    padding: 8px;
                    background-color: transparent;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
                QPushButton:checked {
                    background-color: #e0f7fa;
                    font-weight: bold;
                }
            """
            )
            button.setCheckable(True)
            button.clicked.connect(lambda checked, t=topic: self.show_topic_content(t))
            topics_layout.addWidget(button)
            self.topics_buttons.append(button)

        # Add stretch to push buttons to top
        topics_layout.addStretch()
        sidebar.addWidget(topics_frame)

        # Quiz button at the bottom of sidebar
        self.quiz_button = QPushButton("Take Quiz on Current Category")
        self.quiz_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2e86de;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #1b4f72;
            }
        """
        )
        self.quiz_button.clicked.connect(self.start_quiz)
        sidebar.addWidget(self.quiz_button)

        # Wrap sidebar in a QWidget to set fixed width
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar)
        sidebar_widget.setFixedWidth(250)

        # Add sidebar to the content layout
        content_layout.addWidget(sidebar_widget)

        # Main content area (right side of the layout)
        content_frame = QFrame()
        content_frame.setFrameShape(QFrame.StyledPanel)
        content_frame.setStyleSheet(
            "background-color: white; border-radius: 5px; padding: 20px;"
        )
        content_inner_layout = QVBoxLayout(content_frame)

        # Title of selected topic
        self.content_title = QLabel("Select a topic to begin")
        self.content_title.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px;"
        )
        content_inner_layout.addWidget(self.content_title)

        # Text area for displaying topic content
        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        self.content_text.setStyleSheet("font-size: 14px; line-height: 1.5;")
        content_inner_layout.addWidget(self.content_text)

        # Add content area to content layout
        content_layout.addWidget(content_frame)

        # Add content layout (sidebar + main content) to main layout
        main_layout.addLayout(content_layout)

        # Footer label at the bottom
        footer = QLabel("Created with PySide6 - QA & Testing Knowledge Base")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #95a5a6; margin: 10px;")
        main_layout.addWidget(footer)

        # Set the final layout to the window
        self.setLayout(main_layout)

        # Automatically click the first topic button (if any)
        if self.topics_buttons:
            self.topics_buttons[0].click()

    def category_changed(self):
        category = self.category_combo.currentText()
        topics = self.knowledge_base.get_topics(category)

        # Clear current topic buttons
        for button in self.topics_buttons:
            button.setParent(None)
            button.deleteLater()

        self.topics_buttons = []

        # Add new topic buttons
        topics_layout = self.findChild(QFrame).layout()
        for topic in topics:
            button = QPushButton(topic)
            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    border: none;
                    padding: 8px;
                    background-color: transparent;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
                QPushButton:checked {
                    background-color: #e0f7fa;
                    font-weight: bold;
                }
            """
            )
            button.setCheckable(True)
            button.clicked.connect(lambda checked, t=topic: self.show_topic_content(t))
            topics_layout.insertWidget(topics_layout.count() - 1, button)
            self.topics_buttons.append(button)

        # Select first topic by default
        if self.topics_buttons:
            self.topics_buttons[0].click()

    def show_topic_content(self, topic):
        # Uncheck all other buttons
        for button in self.topics_buttons:
            if button.text() != topic:
                button.setChecked(False)

        content = self.knowledge_base.get_content(topic)
        self.content_title.setText(topic)
        self.content_text.setMarkdown(content)

    def start_quiz(self):
        category = self.category_combo.currentText()
        quiz_data = self.knowledge_base.get_quiz(category)

        if not quiz_data:
            QMessageBox.information(
                self,
                "No Quiz Available",
                f"No quiz questions available for the '{category}' category yet.",
            )
            return

        quiz_dialog = QuizDialog(quiz_data, category, self)
        quiz_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

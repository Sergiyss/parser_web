import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QComboBox, QPushButton, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap
import urllib.request

class WidgetImage(QWidget):
	"""docstring for WidgetImage"""
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		#Window Size
		self.resize(400, 400)
		#Window position
		self.move(300, 300)
		#Window title
		self.setWindowTitle('Parser')
		#show
		self.show()


class Widget(QMainWindow):
	"""docstring for Widget"""
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
	def initUI(self):
		#Window Size
		self.resize(800, 600)
		#Window position
		self.move(300, 300)
		#Window title
		self.setWindowTitle('Parser')

		self.date_publish = QLineEdit(self)
		self.date_publish.move(20, 20)
		self.date_publish.resize(280, 40)
		self.date_publish.setPlaceholderText("дата публикации")
		self.date_publish.setText("text")

		self.author = QLineEdit(self)
		self.author.move(20, 70)
		self.author.resize(280, 40)
		self.author.setPlaceholderText("автор")

		self.original_title_post = QLineEdit(self)
		self.original_title_post.move(20, 120)
		self.original_title_post.resize(280, 40)
		self.original_title_post.setPlaceholderText("оригинальный заголовок статью")

		self.translate_title_yandex_api = QLineEdit(self)
		self.translate_title_yandex_api.move(20, 170)
		self.translate_title_yandex_api.resize(280, 40)
		self.translate_title_yandex_api.setPlaceholderText("перевод заголовка")

		self.category = QComboBox(self)
		self.category.move(20, 220)
		self.category.resize(280, 40)
		self.category.addItems(["category 1", "category 2", "category 3",
								"category 4", "category 5" ]) #сколько хочешь можешь добавить категорий

		self.RAZDEL = QComboBox(self) #RAZDEL :D my ENGLISH is ABZAC
		self.RAZDEL.move(20, 270)
		self.RAZDEL.resize(280, 40)
		self.RAZDEL.addItems(["Articles", "GitHub" ])

		self.likes = QLineEdit(self)
		self.likes.move(20, 320)
		self.likes.resize(280, 40)
		self.likes.setPlaceholderText("0 лайков")

		self.link_original = QLineEdit(self)
		self.link_original.move(20, 370)
		self.link_original.resize(280, 40)
		self.link_original.setPlaceholderText("ссылка на источник")

		self.keys = QLineEdit(self)
		self.keys.move(20, 420)
		self.keys.resize(280, 40)
		self.keys.setPlaceholderText("найденые ключи")

		self.image_url = QLineEdit(self)
		self.image_url.move(20, 470)
		self.image_url.resize(280, 40)
		self.image_url.setPlaceholderText("ссылка на картинку")
		self.image_url.setText("https://image.freepik.com/free-photo/cute-cat-picture_1122-449.jpg")

		self.image_url_button = QPushButton("показать картинку",self)
		self.image_url_button.move(20, 520)
		self.image_url_button.resize(280, 40)
		self.image_url_button.clicked.connect(self.on_click_image)

		self.short_ABZAC = QTextEdit(self) #ABZAC :D
		self.short_ABZAC.move(320, 20)
		self.short_ABZAC.resize(450, 270)
		self.short_ABZAC.setPlaceholderText("краткий абзац статьи")

		self.translate_ABZAC = QTextEdit(self)
		self.translate_ABZAC.move(320, 300)
		self.translate_ABZAC.resize(450, 270)
		self.translate_ABZAC.setPlaceholderText("перевод абзаца")

		self.show()

	
	def on_click_image(self):
		self.image_widget = WidgetImage()
		self.image_data = urllib.request.urlopen(self.image_url.text()).read()
		self.pixmap = QPixmap()
		self.pixmap.loadFromData(self.image_data)
		self.image_widget.image = QLabel(self.image_widget)
		self.image_widget.image.resize(400, 400)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = Widget()
	sys.exit(app.exec_())
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.refresh()
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
		# 해당 웹 사이트를 확인하러 간다
		self.browser.get(self.live_server_url)

		# 웹 페이지 타이틀과 헤더가 ‘To-Do’를 표시하고 있다
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# 그녀는 바로 작업을 추가하기로 한다
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), '작업 아이템 입력')

		# "공작깃털 사기"라고 텍스트 상자에 입력한다
		# (에디스의 취미는 날치 잡이용 그물을 만드는 것이다)
		inputbox.send_keys('공작깃털 사기')

		#엔터키를 치면 페이지가 갱신되고 작업 목록에
		# "1: 공작깃털 사기" 아이템이 추가된다
		inputbox.send_keys(Keys.ENTER)

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: 공작깃털 사기')

		# 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
		# 다시 "공작깃털을 사용해서 그물 만들기"라고 입력한다 
		# (에디스는 매우 체계적인 사람이다)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('공작깃털을 사용해서 그물 만들기')
		inputbox.send_keys(Keys.ENTER)

		# 페이지는 다시 갱신되고, 2개 아이템이 목록에 보여진다
		self.check_for_row_in_list_table('1: 공작깃털 사기')
		self.check_for_row_in_list_table('2: 공작깃털을 사용해서 그물 만들기')

		# 에디스는 사이트가 입력한 목록을 저장하고 있는지 궁금하다.
		# 사이트는 그녀를 위한 특정 URL을 생성해 준다.
		# 이때 URL에 대한 설명도 함께 제공된다.
		self.check_for_row_in_list_table('2: 공작깃털을 사용해서 그물 만들기')
		self.check_for_row_in_list_table('1: 공작깃털 사기')

		# 새로운 사용자인 프란시스가 사이트에 접속한다

		## 새로운 브라우저 세션을 이요해서 에디스의 정보가
		## 쿠키를 통해 유입되는 것을 방지한다
		time.sleep(1)
		self.browser.refresh()
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# 프란시스가 홈페이지에 접속한다
		# 에디스의 리스트는 보이지 않는다
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('공작깃털 사기', page_text)
		self.assertNotIn('그물 만들기', page_text)

		# 프란시스가 새로운 작업 아이템을 입력하기 시작한다
		# 그는 에디스 보다 재미가 없다
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('우유 사기')
		inputbox.send_keys(Keys.ENTER)

		# 프린시스가 전용 URL을 취득한다
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# 에디스가 입력한 흔적이 없다는 것을 확인한다
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('공작깃털 사기', page_text)
		self.assertIn('우유 사기', page_text)

		# 둘다 만족하고 잠자리에 든다.
		self.fail('Finish the test!')

	def test_layout_and_styling(self):
		# 에디스는 메인 페이지를 방문한다
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		# 그녀는 입력 상자가 가운데 배치된 것을 본다
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=10
		)

		self.fail('Finish the test!')

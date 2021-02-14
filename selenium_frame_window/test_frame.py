# *_*coding:utf-8 *_*
from selenium_frame_window.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult") #切换到frame
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame() #切换到父级frame
        self.driver.switch_to.default_content() #切换到默认frame
        print(self.driver.find_element_by_id("submitBTN").text)
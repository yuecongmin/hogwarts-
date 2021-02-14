# *_*coding:utf-8 *_*
from time import sleep

from selenium.webdriver import ActionChains

from selenium_frame_window.base import Base


class Testalert(Base):
    def test_alert(self):
        # 打开网页、切换到frame里面
        # 使用ActionChains的drag和drop方法，执行拖拽
        # 网页弹出alert弹窗，点击弹框中的“确认”
        # 再切换到默认frame，点击“点击运行”按钮，恢复到默认状态
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 打开网页、切换到frame里面
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        # 使用ActionChains的drag和drop方法，执行拖拽
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        # 网页弹出alert弹窗，点击弹框中的“确认”
        self.driver.switch_to.alert.accept()
        sleep(3)
        # 再切换到默认frame，点击“点击运行”按钮，恢复到默认状态
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
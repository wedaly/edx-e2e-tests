"""
Courses page
"""
from bok_choy.page_object import PageObject

from regression.pages.whitelabel.const import URL_WITH_AUTH


class CoursesPage(PageObject):
    """
    Course Page
    """

    url = URL_WITH_AUTH + 'courses'

    def is_browser_on_page(self):
        return self.q(css='.course-name .course-title').visible

    def click_on_the_course(self, course_id):
        """
        click on the desired course id to open course about page

        Arguments:
            course_id(str): Id of the target page.
        """
        self.q(css='article[id="' + course_id + '"]>a').click()

from qa_guru_9_10.pages.profile_page import ProfilePage
from qa_guru_9_10.pages.simple_user_registration_page import SimpleUserRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleUserRegistrationPage()
        self.profile = ProfilePage()


app = Application()

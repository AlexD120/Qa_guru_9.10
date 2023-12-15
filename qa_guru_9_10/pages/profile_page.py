from selene.support.conditions import have

from qa_guru_9_10.data.users import User


class ProfilePage:
    def should_have_data(self, user: User):
        self.full_name.should(have.exact_text(user.full_name))

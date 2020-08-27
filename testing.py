import unittest
import loginclass
import form
import form2
class MyTest(unittest.TestCase):
    def test_login_user(self):
        item = loginclass.Login()
        result = item.login_user('test_email', 'test_password')
        if len(result) > 0:
            actual_result = True
        else:
            actual_result = False

        self.assertTrue(actual_result)
    def test_forget_pw(self):
        order=loginclass.Recover_pw()
        result = order.forget_pw('test_email')
        if len(result) > 0:
            actual_result = True
        else:
            actual_result = False

        self.assertTrue(actual_result)
    def test_answer_match(self):
        ans=loginclass.Answer_match()
        result = ans.update_pw('test_password','test_email')


        self.assertTrue(result)
    def test_check_ans(self):
        ans = loginclass.Answer_match()
        result = ans.check_ans('test_email','test_question','test_answer')

        self.assertTrue(result)
    # def test_register(self):
    #     ans = loginclass.Register()
    #     result = ans.register_entry('test_fname', 'test_lname','test_contact','test_email','test_password','test_question','test_answer')
    #
    #     self.assertFalse(result)


    def test_show_in_tree(self):
        item = form.return_flight()
        result = item.show_in_treeview('test_user_id')

        if len(result) > 0:
            actual_result = True
        else:
            actual_result = False

        self.assertFalse(actual_result)

unittest.main()

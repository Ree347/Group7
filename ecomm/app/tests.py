from django.test import TestCase
from app.forms import CustomerProfileForm, SellerRegistrationForm, SellerProfileForm, CustomerRegistrationForm


# Create your tests here.


#test to make sure 'mobile' is numbers rather than characters
class customer_registration(TestCase):

    def test_customer(self):
        form = CustomerProfileForm(data = {
            'name': 'rui8',
            'locality' : 'test@test',
            'city'    :  'starkville',
            'mobile'   : 'hhhjahsjhf',
            'zipcode'  : '98799',
        }
        )
        
        self.assertFalse(form.is_valid())
        
#test to make sure a field in profile cannot be null      


    def test_customer_null(self):
        form = CustomerProfileForm(data = {
            'name': 'rui8',
            'locality' : 'test@test',
            'city'    :  'starkville',
            'mobile'   : '',
            'zipcode'  : '98799',
        }
        )
        
        self.assertFalse(form.is_valid())
        



class seller_registration(TestCase):

#seller password must be 8 characters or more

    def test_sellerid_length(self):
            form = SellerRegistrationForm(data = {
                'username' :'then22',
                'email'    : 'testtest@test.com',
                'password1': 'eli',
                'password2': 'eli',
                'sellerid' : '6678',
            }
            )
        
            self.assertFalse(form.is_valid())
     
#seller id must be numbers

    def test_sellerid_number(self):
            form = SellerRegistrationForm(data = {
                'username' :'then22',
                'email'    : 'testtest@test.com',
                'password1': 'eli',
                'password2': 'eli',
                'sellerid' : 'jumo77',
            }
            )
        
            self.assertFalse(form.is_valid())

#password must match

    def test_sellerid_passwordmatch(self):
            form = SellerRegistrationForm(data = {
                'username' :'then22',
                'email'    : 'testtest@test.com',
                'password1': 'elijah181',
                'password2': 'elijah181',
                'sellerid' : '3333',
            }
            )
        
            self.assertTrue(form.is_valid())


#email must be valid form
    def test_sellerid_emailcheck(self):
        form = SellerRegistrationForm(data = {
            'username' :'then22',
            'email'    : 'testtestahkfhskjck',
            'password1': 'elijah181',
            'password2': 'elijah181',
            'sellerid' : '3333',
            }
            )
        
        self.assertFalse(form.is_valid())
        
#nothing can be null
    def test_sellerid_nullvalues(self):
        form = SellerRegistrationForm(data = {
            'username' :'',
            'email'    : '',
            'password1': '',
            'password2': '',
            'sellerid' : '',
            }
            )
        
        self.assertFalse(form.is_valid())

#customer email must be in valid form
    def test_customer_nullvalues(self):
        form = CustomerRegistrationForm(data = {
            'username' :'3333333',
            'email'    : 'testem',
            'password1': 'jumping22',
            'password2': 'jumping22',
            }
            )
        
        self.assertFalse(form.is_valid())
        
#customer password must be 8 characters or more

    def test_customer_password(self):
        form = CustomerRegistrationForm(data = {
            'username' :'3333333',
            'email'    : 'testem@gmail.com',
            'password1': 'ju',
            'password2': 'ju',
            }
            )
        
        self.assertFalse(form.is_valid())
        
#customer email must match

    def test_customer_allnullvalues(self):
        form = CustomerRegistrationForm(data = {
            'username' :'',
            'email'    : '',
            'password1': '',
            'password2': '',
            }
            )
        
        self.assertFalse(form.is_valid())
# Create your tests here.

# Create your views here.
"""
Code that should be copy and pasted in to
reg/views.py to as a skeleton for creating
the authentication views
"""
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms



from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from models import UserProfile

class RegistrationForm(forms.Form):
    
      
        
    username = forms.RegexField(regex=r'^\w+$', max_length=30,widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
           
    
    def isValidUsername(self, field_data, all_data):
        try:
            User.objects.get(username=field_data)
        except User.DoesNotExist:
            return
        raise validators.ValidationError('The username "%s" is already taken.' % field_data)
    
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],new_data['email'],new_data['password1'])
        u.is_active = False
        u.save()
        return u


@csrf_exempt
def register(request):
    if request.method=="POST":
       registerform=RegistrationForm(request.POST)

       if request.user.is_authenticated():
        # They already have an account; don't let them register again
             return render_to_response('register.html', {'has_account': True})
    else:
           registerform=RegistrationForm()
    return render_to_response('reg/create_ac.html',{ 'form':registerform})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
               	
        #capturing username and password parameters
        uname=request.POST['username']
        passw=request.POST['password']
        #authenticaing user
        user=authenticate(username=uname,password=passw)
        #checking whether user exists
        if user is not None:
           if user.is_active:
             login(request,user)	
             return HttpResponseRedirect(request.path)
           else:
               return HttpResponse('account can not be verified')
        else:
             form = LoginForm()
             return render_to_response('reg/login.html',{'form': form, 'logged_in': request.user.is_authenticated()})
    else:
        form = LoginForm()
    return render_to_response('reg/login.html', {'form': form, 'logged_in': request.user.is_authenticated(),'users':request.user})
@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/logout.html')









#attrs_dict = { 'class': 'required' }

'''

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', max_length=30,widget=forms.TextInput(attrs=attrs_dict),label=_(u'username'))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs_dict,label=_(u'email address'))
    #password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict),label=_(u'password'))
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict),label=_(u'password (again)'))
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        try:
            user = User.objects.get(username__exact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'This username is already taken. Please choose another.'))
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data


    def save(self, profile_callback=None):
        """
        Create the new ``User`` and ``RegistrationProfile``, and
        returns the ``User``.
        
        This is essentially a light wrapper around
        ``RegistrationProfile.objects.create_inactive_user()``,
        feeding it the form data and a profile callback (see the
        documentation on ``create_inactive_user()`` for details) if
        supplied.
          """
        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
                                                                    password=self.cleaned_data['password1'],
                                                                    email=self.cleaned_data['email'],
                                                                    profile_callback=profile_callback)
        return new_user



'''
